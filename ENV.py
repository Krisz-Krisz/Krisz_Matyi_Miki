"""Environment simulation for a modular autonomous vehicle path-tracking system."""

import math
import time
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, writers

from EKF import KinematicEKF
from MPC import MPCController

class GroundTruthVehicle:
    def __init__(self, dt=0.1, wheelbase=2.5):
        self.dt = dt
        self.L = wheelbase
        self.state = np.array([0.0, 0.0, 0.0, 0.0])

    def step(self, control):
        delta, a = control
        x, y, v, yaw = self.state
        x += v * math.cos(yaw) * self.dt
        y += v * math.sin(yaw) * self.dt
        yaw += v / self.L * math.tan(delta) * self.dt
        v = max(0.0, v + a * self.dt)
        yaw = (yaw + math.pi) % (2.0 * math.pi) - math.pi
        self.state = np.array([x, y, v, yaw])

    def noisy_observation(self):
        x, y, v, _ = self.state
        x_noisy = x + np.random.normal(0.0, 0.4)
        y_noisy = y + np.random.normal(0.0, 0.4)
        v_noisy = v + np.random.normal(0.0, 0.2)
        return np.array([x_noisy, y_noisy, v_noisy])


"""Define main path"""

def create_reference_path():
    x = np.linspace(0.0, 35.0, 351)
    y = 1.8 * np.cos(0.2 * x)
    return np.column_stack((x, y))



def find_local_path(reference, current_position, lookahead=15):
    distances = np.linalg.norm(reference - current_position[:2], axis=1)
    nearest = np.argmin(distances)
    return reference[nearest:nearest + lookahead]


def plot_trajectory(data_frame, reference_path):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(reference_path[:, 0], reference_path[:, 1], 'k--', label='Reference Path')
    ax.plot(data_frame['true_x'], data_frame['true_y'], 'b-', label='True Path')
    ax.plot(data_frame['ekf_x'], data_frame['ekf_y'], 'g-', label='EKF Estimate')
    ax.scatter(data_frame['noisy_x'], data_frame['noisy_y'], c='red', s=8, alpha=0.3, label='Noisy Measurements')
    ax.set_xlabel('X [m]')
    ax.set_ylabel('Y [m]')
    ax.set_title('Autonomous Vehicle Path Tracking')
    ax.legend()
    ax.grid(True)
    fig.tight_layout()
    fig.savefig('trajectory.png')
    plt.close(fig)


def animate_run(data_frame, reference_path):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(reference_path[:, 0], reference_path[:, 1], 'k--', label='Reference Path')
    true_line, = ax.plot([], [], 'b-', label='True Path')
    ekf_line, = ax.plot([], [], 'g-', label='EKF Path')
    noisy_scatter = ax.scatter([], [], c='red', s=10, alpha=0.4, label='Noisy')
    ax.set_xlim(reference_path[:, 0].min() - 2.0, reference_path[:, 0].max() + 2.0)
    y_ext = np.max(np.abs(reference_path[:, 1])) + 3.0
    ax.set_ylim(-y_ext, y_ext)
    ax.set_xlabel('X [m]')
    ax.set_ylabel('Y [m]')
    ax.grid(True)
    ax.legend()

    def update(frame):
        true_line.set_data(data_frame['true_x'][:frame], data_frame['true_y'][:frame])
        ekf_line.set_data(data_frame['ekf_x'][:frame], data_frame['ekf_y'][:frame])
        noisy_scatter.set_offsets(np.column_stack((data_frame['noisy_x'][:frame], data_frame['noisy_y'][:frame])))
        return true_line, ekf_line, noisy_scatter

    animation = FuncAnimation(fig, update, frames=len(data_frame), interval=50, blit=True)
    if writers.is_available('ffmpeg'):
        writer = writers['ffmpeg'](fps=10)
        animation.save('trajectory_animation.mp4', writer=writer, dpi=150)
        print('Saved animation as trajectory_animation.mp4 using ffmpeg.')
    elif writers.is_available('pillow'):
        writer = writers['pillow'](fps=10)
        animation.save('trajectory_animation.gif', writer=writer, dpi=150)
        print('ffmpeg unavailable; saved animation as trajectory_animation.gif using Pillow.')
    else:
        print('No animation writer available: install ffmpeg or pillow to enable animation saving.')
    plt.close(fig)


def main():
    np.random.seed(67)
    reference = create_reference_path()
    vehicle = GroundTruthVehicle(dt=0.1, wheelbase=2.5)
    # Set vehicle to start at the beginning of the reference path
    initial_pos = reference[0]
    initial_yaw = np.arctan2(reference[1][1] - reference[0][1], reference[1][0] - reference[0][0])  # Direction from first two points
    vehicle.state = np.array([initial_pos[0], initial_pos[1], 0.0, initial_yaw])
    ekf = KinematicEKF(dt=0.1, wheelbase=2.5)
    ekf.set_initial_state([initial_pos[0], initial_pos[1], 0.0, initial_yaw])  # Match vehicle start
    mpc = MPCController(horizon=12, dt=0.1, wheelbase=2.5)

    records = []
    previous_control = (0.0, 0.0)

    for step in range(280):
        true_state = vehicle.state.copy()
        noisy_measurement = vehicle.noisy_observation()
        ekf_state = ekf.step(noisy_measurement, previous_control)
        local_reference = find_local_path(reference, ekf_state)
        steering, acceleration, solve_time = mpc.solve(ekf_state, local_reference)

        previous_control = (steering, acceleration)
        vehicle.step(previous_control)

        cross_track_error = np.linalg.norm(true_state[:2] - local_reference[0]) if len(local_reference) > 0 else 0.0
        records.append({
            'time': step * vehicle.dt,
            'true_x': true_state[0],
            'true_y': true_state[1],
            'true_v': true_state[2],
            'true_yaw': true_state[3],
            'noisy_x': noisy_measurement[0],
            'noisy_y': noisy_measurement[1],
            'noisy_v': noisy_measurement[2],
            'ekf_x': ekf_state[0],
            'ekf_y': ekf_state[1],
            'ekf_v': ekf_state[2],
            'ekf_yaw': ekf_state[3],
            'steering': steering,
            'acceleration': acceleration,
            'mpc_solve_time': solve_time,
            'cross_track_error': cross_track_error,
        })

    df = pd.DataFrame(records)
    df.to_csv('simulation_log.csv', index=False)

    rmse = KinematicEKF.rmse(df[['ekf_x', 'ekf_y', 'ekf_v']].values,
                             df[['true_x', 'true_y', 'true_v']].values)
    print(f'RMSE [x, y, v] = {rmse.round(3)}')
    print(f'Average MPC solve time: {df["mpc_solve_time"].mean():.4f} s')
    print(f'Steering variance: {df["steering"].var():.5f}')

    plot_trajectory(df, reference)
    animate_run(df, reference)

if __name__ == '__main__':
    main()

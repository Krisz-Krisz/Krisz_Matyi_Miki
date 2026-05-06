"""MPC controller implementation for a kinematic bicycle model."""

import numpy as np
from scipy.optimize import minimize
import time

class MPCController:
    def __init__(self, horizon=12, dt=0.1, wheelbase=2.5,
                 max_steer=np.deg2rad(25.0), max_acc=2.0):
        self.N = horizon
        self.dt = dt
        self.L = wheelbase
        self.max_steer = max_steer
        self.max_acc = max_acc
        self.last_solution = None

    def _bike_model(self, state, control):
        x, y, v, yaw = state
        delta, a = control
        x_next = x + v * np.cos(yaw) * self.dt
        y_next = y + v * np.sin(yaw) * self.dt
        yaw_next = yaw + v / self.L * np.tan(delta) * self.dt
        v_next = v + a * self.dt
        return np.array([x_next, y_next, v_next, yaw_next])

    def _predict_trajectory(self, state, controls):
        trajectory = [state.copy()]
        for i in range(0, len(controls), 2):
            control = controls[i:i + 2]
            state = self._bike_model(state, control)
            trajectory.append(state.copy())
        return np.array(trajectory)

    def _nearest_reference(self, state, path):
        distances = np.linalg.norm(path - state[:2], axis=1)
        idx = np.argmin(distances)
        return path[idx:idx + self.N + 1]

    def _cost(self, controls, x0, reference):
        trajectory = self._predict_trajectory(x0, controls)
        cost = 0.0
        for i, state in enumerate(trajectory[1:], start=1):
            if i - 1 >= len(reference):
                break
            ref = reference[i - 1]
            dx = state[0] - ref[0]
            dy = state[1] - ref[1]
            cte = np.hypot(dx, dy)
            cost += 5.0 * cte ** 2
            cost += 0.5 * (state[2] - 5.0) ** 2
            cost += 0.1 * np.abs(controls[2 * (i - 1)])
            cost += 0.1 * np.abs(controls[2 * (i - 1) + 1])
        cost += 100.0 * np.sum(np.diff(controls.reshape(-1, 2), axis=0) ** 2)
        return cost

    def solve(self, x_est, path_points):
        x0 = np.asarray(x_est).flatten()
        horizon_reference = self._nearest_reference(x0, np.asarray(path_points))
        if len(horizon_reference) < 2:
            return 0.0, 0.0, 0.0

        initial_guess = np.zeros(self.N * 2)
        bounds = []
        for _ in range(self.N):
            bounds.append((-self.max_steer, self.max_steer))
            bounds.append((-self.max_acc, self.max_acc))

        start_time = time.perf_counter()
        result = minimize(
            lambda u: self._cost(u, x0, horizon_reference),
            initial_guess,
            bounds=bounds,
            method="SLSQP",
            options={"maxiter": 80, "ftol": 1e-4}
        )
        solve_time = time.perf_counter() - start_time
        if result.success:
            self.last_solution = result.x
        controls = self.last_solution if self.last_solution is not None else initial_guess
        steering = float(controls[0])
        acceleration = float(controls[1])
        return steering, acceleration, solve_time

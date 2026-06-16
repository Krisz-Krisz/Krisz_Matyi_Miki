# Autonomous Vehicle Path Tracking Project

This repository implements a modular 2D autonomous vehicle path-tracking simulation in Python. The project is divided into three main functional components:

- `ENV.py`: environment and simulation loop
- `EKF.py`: Extended Kalman Filter for state estimation
- `MPC.py`: Model Predictive Control for command generation

Each component has a clearly defined responsibility, and they communicate in a cycle to simulate a realistic perception-control loop under noise.

## Installation

### Windows

1. Create and activate a Python virtual environment in the repository root:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
2. Upgrade pip and install required packages:
   ```bash
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```
3. Optional: Install ffmpeg for MP4 animation output (Pillow is used automatically for GIF output if ffmpeg is unavailable):
   - Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH, or use Chocolatey: `choco install ffmpeg`

### Debian-based Linux (Ubuntu, Mint, etc.)

1. Create and activate a Python virtual environment in the repository root:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Upgrade pip and install required packages:
   ```bash
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```
3. Optional: Install ffmpeg for MP4 animation output (Pillow is used automatically for GIF output if ffmpeg is unavailable):
   ```bash
   sudo apt update && sudo apt install ffmpeg
   ```

### Arch-based Linux

1. Create and activate a Python virtual environment in the repository root:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Upgrade pip and install required packages:
   ```bash
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```
3. Optional: Install ffmpeg for MP4 animation output (Pillow is used automatically for GIF output if ffmpeg is unavailable):
   ```bash
   sudo pacman -S ffmpeg
   ```

### Fedora-based Linux

1. Create and activate a Python virtual environment in the repository root:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Upgrade pip and install required packages:
   ```bash
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```
3. Optional: Install ffmpeg for MP4 animation output (Pillow is used automatically for GIF output if ffmpeg is unavailable):
   ```bash
   sudo dnf install ffmpeg
   ```

## Project Overview

The simulation follows this timing chain:

1. `ENV.py` updates the true vehicle state using a kinematic bicycle model.
2. `ENV.py` generates noisy sensor data from the true state.
3. `EKF.py` consumes the noisy measurements and the previous control input to estimate the vehicle state.
4. `MPC.py` uses the estimated state and a local reference path to compute the next steering and acceleration commands.
5. `ENV.py` applies those commands to the next time step.

This loop is repeated for each simulation step, and all data are logged for later analysis.

## ENV.py — Environment Simulation

`ENV.py` is the main entry point for the project. Its responsibilities are:

- Define the ground truth vehicle model using a kinematic bicycle approximation.
- Apply steering and acceleration controls to propagate the true vehicle state.
- Create noisy observations for position and velocity.
- Manage the simulation loop and call EKF and MPC at each time step.
- Save the logged results to `simulation_log.csv` and generate visual output.

### Key functions in `ENV.py`

- `GroundTruthVehicle.__init__(dt, wheelbase)`
  - Initializes the vehicle with a time step and wheelbase.
  - Sets the initial state to `[x, y, v, yaw] = [0, 0, 0, 0]`.

- `GroundTruthVehicle.step(control)`
  - Applies the control input `[steering_angle, acceleration]`.
  - Updates position and heading using the kinematic bicycle equations:
    - `x += v * cos(yaw) * dt`
    - `y += v * sin(yaw) * dt`
    - `yaw += v / L * tan(delta) * dt`
    - `v += a * dt`
  - Enforces non-negative speed and normalizes yaw.

- `GroundTruthVehicle.noisy_observation()`
  - Adds Gaussian noise to the true state measurements.
  - Returns noisy `[x, y, v]` used by the EKF.

- `create_reference_path()`
  - Builds a simple sinusoidal reference trajectory for the vehicle to follow.
  - Produces a set of 2D waypoints along the target path.

- `find_local_path(reference, current_position, lookahead)`
  - Finds the nearest index on the global reference path.
  - Extracts a short horizon slice needed by the MPC.

- `plot_trajectory(data_frame, reference_path)`
  - Plots the reference path, true path, EKF trajectory, and noisy measurements.
  - Saves the figure as `trajectory.png`.

- `animate_run(data_frame, reference_path)`
  - Creates an animation from the logged path data.
  - Saves either `trajectory_animation.mp4` using `ffmpeg`, or `trajectory_animation.gif` using Pillow if ffmpeg is unavailable.

### Simulation Loop

- The loop runs for a fixed number of steps.
- Each iteration does:
  - Sample the true state.
  - Generate noisy measurements.
  - Estimate the state using EKF.
  - Compute control commands using MPC.
  - Apply the commands to the true vehicle.
  - Log the results.

The logged file includes:

- true state: `true_x`, `true_y`, `true_v`, `true_yaw`
- noisy measurements: `noisy_x`, `noisy_y`, `noisy_v`
- EKF estimates: `ekf_x`, `ekf_y`, `ekf_v`, `ekf_yaw`
- control outputs: `steering`, `acceleration`
- solver information: `mpc_solve_time`
- tracking quality: `cross_track_error`

## EKF.py — Extended Kalman Filter

`EKF.py` is responsible for converting noisy sensor data into a smooth, estimated vehicle state.

### What it estimates

The filter maintains the state vector:

- `x`: position along the x-axis
- `y`: position along the y-axis
- `v`: forward speed
- `yaw`: vehicle heading

It uses both prediction and update steps to combine control inputs and measurements.

### Key functions in `EKF.py`

- `KinematicEKF.__init__(dt, wheelbase)`
  - Initializes the state vector, covariance matrices, process noise `Q`, and observation noise `R`.
  - Sets the observation matrix `H` so the filter directly measures `x`, `y`, and `v`.

- `KinematicEKF.set_initial_state(x0)`
  - Sets the starting estimate and reduces initial covariance for the known starting state.

- `KinematicEKF.predict(u)`
  - Uses the vehicle bicycle model to predict the next state based on control inputs.
  - Updates the state transition Jacobian `F` to propagate uncertainty.
  - Applies process noise `Q` to the covariance.

- `KinematicEKF.update(z)`
  - Incorporates noisy sensor measurements into the estimate.
  - Computes the Kalman gain `K` from the current covariance and measurement noise `R`.
  - Updates the state estimate and covariance.
  - Normalizes the heading angle after correction.

- `KinematicEKF.step(z, u)`
  - Runs `predict()` followed by `update()` in one call.
  - Returns the filtered state.

- `KinematicEKF.rmse(estimates, ground_truths)`
  - Computes the Root Mean Square Error between estimated and true state values.
  - Used for evaluating filter performance.

### Why EKF is used

The Extended Kalman Filter is needed because the motion model is nonlinear due to heading and steering dynamics. EKF linearizes this model around the current estimate and updates uncertainty using measured position and speed.

## MPC.py — Model Predictive Control

`MPC.py` generates smooth control actions that drive the estimated vehicle state toward the reference path.

### Its responsibilities

- Predict future vehicle motion over a finite horizon.
- Minimize cross-track error to the path.
- Penalize deviations from a target speed.
- Reduce control effort and avoid abrupt steering or acceleration changes.

### Key functions in `MPC.py`

- `MPCController.__init__(horizon, dt, wheelbase, max_steer, max_acc)`
  - Configures the planning horizon and vehicle dimensions.
  - Sets actuator limits for steering and acceleration.

- `MPCController._bike_model(state, control)`
  - Defines the discrete kinematic bicycle model for prediction.
  - Computes the next state from current state and control input.

- `MPCController._predict_trajectory(state, controls)`
  - Simulates the vehicle forward through the entire control sequence.
  - Produces a state trajectory used by the cost function.

- `MPCController._nearest_reference(state, path)`
  - Finds the nearest waypoint on the reference path.
  - Extracts a local reference segment for the horizon.

- `MPCController._cost(controls, x0, reference)`
  - Computes a scalar objective including:
    - squared cross-track error
    - speed tracking error
    - control magnitude penalty
    - smoothness penalty for control changes
  - This cost encourages accurate, smooth path following.

- `MPCController.solve(x_est, path_points)`
  - Uses `scipy.optimize.minimize` with bounds on steering and acceleration.
  - Returns the first control command from the optimized sequence.
  - Also returns solve time for performance logging.

### Why MPC is used

MPC is valuable because it plans control actions over multiple future steps, allowing the vehicle to anticipate the path shape and avoid jerky corrections. Here, it balances tracking performance with smooth actuator usage.

## Usage

1. Make sure the virtual environment is activated:
   ```bash
   source .venv/bin/activate
   ```
2. Run the main environment simulation:
   ```bash
   python ENV.py
   ```
3. After the simulation finishes, check the generated files:
   - `simulation_log.csv`
   - `trajectory.png`
   - `trajectory_animation.mp4` or `trajectory_animation.gif`

## Outputs

- `simulation_log.csv`: all logged values for offline analysis
- `trajectory.png`: static plot of reference, true, EKF, and noisy data
- `trajectory_animation.mp4` or `trajectory_animation.gif`: animation of the simulation

## What to Expect

- `ENV.py` is the orchestrator and runs the full perception-control loop.
- `EKF.py` cleans noisy sensor data and estimates the vehicle state.
- `MPC.py` computes the next best steering and acceleration commands.
- The system logs both metrics and state trajectories for validation and reporting.

## Notes

- The architecture is intentionally modular so each major function can be improved independently.
- `ENV.py` preserves the golden loop order specified in the project rules.
- All three modules are designed to work together in a real-time simulation context.

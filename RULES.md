# GitHub Copilot System Context: Autonomous Vehicle Path Tracking Project

## Project Overview
You are assisting a team of three students building a modular, 2D simulation of an autonomous vehicle. The project focuses on advanced path tracking in a noisy environment using Python. The system is split across three core Python files, each handling a specific domain: Control, State Estimation, and Environment Simulation.

## The Architecture & Golden Rule
* **The Loop:** The simulation runs on a central time-step loop inside `ENV.py`.
* **Execution Order:** 
  1. `ENV.py` updates ground truth physics and generates noisy sensor readings.
  2. `EKF.py` takes the noisy readings and outputs a clean state estimate.
  3. `MPC.py` takes the clean estimate and the target path, and calculates the next steering/acceleration commands.
  4. The commands are sent back to `ENV.py` for the next time step.

## File-Specific Guidelines

### 1. `MPC.py` (Model Predictive Control)
* **Goal:** Calculate optimal steering angle and acceleration to track a reference path smoothly, avoiding sudden jerks.
* **Libraries:** `numpy`, `scipy.optimize`, or `cvxpy`.
* **Inputs:** Estimated state `[x, y, velocity, yaw]` from `EKF.py`, and local reference path coordinates.
* **Outputs:** Optimal control commands `[steering_angle, acceleration]`.
* **Metrics to Log:** Cross-track error, computation time per loop, and steering angle variance.
* **AI Instruction:** When generating code here, focus on matrix constraints, receding horizon logic, and kinematic bicycle model equations for prediction. 

### 2. `EKF.py` (Extended Kalman Filter)
* **Goal:** Filter noisy GPS and velocity data to estimate the true state of the vehicle.
* **Libraries:** `numpy` (heavy reliance on matrix operations).
* **Inputs:** Noisy sensor readings `[x_noisy, y_noisy, v_noisy]` from `ENV.py` and previous control commands `[steering_angle, acceleration]` from `MPC.py`.
* **Outputs:** Cleaned state estimate `[x_est, y_est, v_est, yaw_est]`.
* **Metrics to Log:** Root Mean Square Error (RMSE) between true state and estimated state.
* **AI Instruction:** Ensure state transition Jacobians and observation Jacobians are properly derived for a kinematic bicycle model.

### 3. `ENV.py` (Environment & Simulation)
* **Goal:** Act as the "ground truth" architect. Maintain the true physical state of the car, generate mathematical noise, and animate the simulation.
* **Libraries:** `matplotlib.animation`, `numpy`, `math`, `pandas` (for data logging).
* **Inputs:** Control commands `[steering_angle, acceleration]` from `MPC.py`.
* **Outputs:** Updated true state `[x, y, v, yaw]`, noisy simulated sensors to feed `EKF.py`, and the visual render loop.
* **AI Instruction:** Start with a simple main loop moving a point. Implement a standard kinematic bicycle model for the physics update step. Ensure all data (True Path, Noisy Path, EKF Path) is logged/saved for post-simulation graphing.
Idea 2: The Advanced Control & Noisy Reality (Control + State Estimation)

Best for a team of 2 or 3 (Control Heavy)

In the real world, sensors are noisy. A car never knows exactly where it is. This project focuses heavily on advanced mathematics and control theory, making it perfect for MATLAB or Python.

    Theme 1: Control (Member A): Implement Model Predictive Control (MPC). MPC is a fantastic, advanced control method that looks into the future to optimize steering and acceleration while respecting constraints (e.g., "don't turn the steering wheel faster than physically possible").

    Theme 2: State Estimation (Member B): Implement an Extended Kalman Filter (EKF). You simulate a car driving, but intentionally corrupt its GPS and speed data with random mathematical noise. The EKF cleans this noisy data to estimate the car's true position.

    Theme 3 (If 3 members): Simulation & Obstacles: Add dynamic, moving obstacles that the MPC has to dodge in real-time.

    How to get your Quantitative Results:

        Graph the "True Path" vs. "Noisy Sensor Path" vs. "EKF Cleaned Path" (this looks great in a 20-page report).

        Compare the smoothness of MPC versus a basic PID controller.

        Measure the computational delay of MPC with different prediction horizons (e.g., looking 10 steps ahead vs. 50 steps ahead).

Member 1: The Controller (Model Predictive Control)

Core Responsibility: Build the brain that drives the car. MPC looks at a reference path, simulates a few steps into the future, and calculates the optimal steering angle and acceleration to stay on the path while avoiding sudden, jerky movements.

    Python Toolkit: numpy (for arrays), scipy.optimize or cvxpy (to solve the optimization problem at each time step).

    The Interface:

        Takes In: The car's current estimated state (X, Y, Velocity, Heading) and the coordinates of the target path ahead.

        Spits Out: The optimal steering angle (δ) and acceleration (a) for the next time step.

    Quantitative Metrics to Gather: * Cross-track error (how far the car is from the center line).

        Computation time per loop (MPC is heavy; prove it runs fast enough).

        Control effort (plot the steering angles to show how smooth it is compared to a basic controller).

Member 2: The Estimator (Extended Kalman Filter)

Core Responsibility: Build the "filter" that cleans up the messy real world. In reality, sensors drift and have static. This member writes the math that takes noisy GPS and speed data and calculates where the car actually is.

    Python Toolkit: numpy (EKF is pure matrix multiplication and Jacobian matrices).

    The Interface:

        Takes In: Noisy sensor readings (simulated GPS X/Y coordinates, noisy velocity) and the control commands (steering/acceleration) that Member 1 just applied.

        Spits Out: The cleaned-up, highly accurate estimate of the car's state (X, Y, Velocity, Heading).

    Quantitative Metrics to Gather:

        Plot the "True Path" vs. "Noisy GPS Path" vs. "EKF Filtered Path" on a single graph.

        Calculate the Root Mean Square Error (RMSE) between the true position and the EKF estimate.

Member 3: The Architect (Simulation & Environment)

Core Responsibility: Build the world, the vehicle physics, and the visualization. This person writes the "ground truth" simulation, generates the fake sensor noise to confuse Member 2, and animates the whole thing so you have visual proof for your presentation.

    Python Toolkit: matplotlib (specifically matplotlib.animation), numpy, and math.

    The Interface:

        Takes In: The steering and acceleration commands from Member 1.

        Spits Out: The updated "true" position of the car (based on a kinematic bicycle model), the "noisy" sensor readings to feed to Member 2, and the visual animation.

    Quantitative Metrics to Gather:

        This member is responsible for generating the visual plots and saving the data logs (e.g., to a CSV) that the other two members will use to generate their graphs.

        Bonus for the grade: Add static obstacles (just X/Y circles) that the car has to drive around, or introduce "wind" (a constant push off the path) to see how the system reacts.

How to Integrate (The Golden Rule)

To make this work, Member 3 needs to build a very basic "dummy" version of the simulation first. This means writing a simple loop that moves a dot on a screen. Once that loop exists:

    Member 2 plugs their EKF into the loop to track the dot.

    Member 1 plugs their MPC into the loop to drive the dot.
"""Extended Kalman Filter implementation for a kinematic bicycle model."""

import numpy as np

class KinematicEKF:
    def __init__(self, dt=0.1, wheelbase=2.5):
        self.dt = dt
        self.L = wheelbase
        self.x = np.zeros((4, 1))
        self.P = np.diag([1.0, 1.0, 1.0, np.deg2rad(20.0)]) ** 2
        self.Q = np.diag([0.05, 0.05, 0.1, np.deg2rad(2.0)]) ** 2
        self.R = np.diag([0.5, 0.5, 0.3]) ** 2
        self.H = np.array([[1.0, 0.0, 0.0, 0.0],
                           [0.0, 1.0, 0.0, 0.0],
                           [0.0, 0.0, 1.0, 0.0]])

    def set_initial_state(self, x0):
        x0 = np.asarray(x0).reshape(4, 1)
        self.x = x0.copy()
        self.P = np.diag([0.1, 0.1, 0.1, np.deg2rad(2.0)]) ** 2

    @staticmethod
    def _normalize_angle(angle):
        return (angle + np.pi) % (2.0 * np.pi) - np.pi

    def predict(self, u):
        delta, a = u
        x, y, v, yaw = self.x.flatten()
        x_pred = x + v * np.cos(yaw) * self.dt
        y_pred = y + v * np.sin(yaw) * self.dt
        yaw_pred = yaw + v / self.L * np.tan(delta) * self.dt
        v_pred = v + a * self.dt

        self.x = np.array([[x_pred], [y_pred], [v_pred], [self._normalize_angle(yaw_pred)]])

        F = np.eye(4)
        F[0, 2] = np.cos(yaw) * self.dt
        F[0, 3] = -v * np.sin(yaw) * self.dt
        F[1, 2] = np.sin(yaw) * self.dt
        F[1, 3] = v * np.cos(yaw) * self.dt
        F[3, 2] = np.tan(delta) / self.L * self.dt

        self.P = F @ self.P @ F.T + self.Q

    def update(self, z):
        z = np.asarray(z).reshape(3, 1)
        y = z - self.H @ self.x
        S = self.H @ self.P @ self.H.T + self.R
        K = self.P @ self.H.T @ np.linalg.inv(S)
        self.x = self.x + K @ y
        self.x[3, 0] = self._normalize_angle(self.x[3, 0])
        self.P = (np.eye(4) - K @ self.H) @ self.P

    def step(self, z, u):
        self.predict(u)
        self.update(z)
        return self.x.flatten()

    @staticmethod
    def rmse(estimates, ground_truths):
        estimates = np.asarray(estimates)
        ground_truths = np.asarray(ground_truths)
        error = estimates - ground_truths
        mse = np.mean(error ** 2, axis=0)
        return np.sqrt(mse)

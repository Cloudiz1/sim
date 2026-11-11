import numpy as np
import math

def euler_to_rotation(
    phi: float, theta: float, psi: float
) -> np.ndarray[tuple[int, int], np.dtype[np.floating]]:
    # rotates body frame to inertial frame
    # precompute sins and coss
    c_phi = math.cos(phi)
    s_phi = math.sin(phi)
    c_theta = math.cos(theta)
    s_theta = math.sin(theta)
    c_psi = math.cos(psi)
    s_psi = math.sin(psi)

    R_roll = np.array([
        [1, 0, 0],
        [0, c_phi, s_phi],
        [0, -s_phi, c_phi]
    ])

    R_pitch = np.array([
        [c_theta, 0, -s_theta],
        [0, 1, 0],
        [s_theta, 0, c_theta]
    ])

    R_yaw = np.array([
        [c_psi, s_psi, 0],
        [-s_psi, c_psi, 0],
        [0, 0, 1]
    ])

    return R_yaw @ R_pitch @ R_roll

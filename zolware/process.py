# -*- coding: utf-8 -*-
import numbers
import numpy as np
from filterpy.common import Q_discrete_white_noise


class Process:
    """The Process class discretized continuous-time kinematic filters
           :param dim: The dimension.
    """
    def __init__(self, sensors, state):
        """
        """
        self.F = np.array([[1, sensors.dt],
                           [0, 1]])
        self.Q = Q_discrete_white_noise(dim=state.dim, dt=sensors.dt, var=2.35)
        self.B = 0.0
        self.u = 0.0
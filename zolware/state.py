# -*- coding: utf-8 -*-
import numpy as np
from .utils import Utils


class State:
    """The State class
    """
    def __init__(self, x0, P0):
        """The state vector x and covariance matrix P are initialized here.
            :param x0: The initial state vector (mean)
            :param P0: The initial state covariance matrix
        """
        dimx = len(x0)
        dimP = len(P0)
        if dimx==dimP:
            dim = len(x0)
        else:
            raise ValueError("The state vector dimension "+
                             "can't be defined.")
        if Utils.checkDimension(dim):
            self.dim = dim
            self.x = np.array(x0)
            self.P = np.array(P0)

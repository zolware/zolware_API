# -*- coding: utf-8 -*-
import numpy as np
from .utils import Utils


class Measurement:
    """The Measurement class
           :param dim: The dimension.
    """
    def __init__(self, sensors):
        """The measurement mean z and covariance R
        are initialized here.
        """
        self.H = np.array([[1., 0.]])
        self.R = np.array([[5.]])


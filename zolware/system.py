# -*- coding: utf-8 -*-
import numpy as np
from .utils import Utils


class System:
    """The Measurement class
       Define the H and R matrices.
           :param dim: The dimension.
    """
    def __init__(self):
        """The measurement mean z and covariance R
        are initialized here.
        """
        self.H = np.array([[1., 0.]])
        self.R = np.array([[5.]])


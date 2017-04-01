# -*- coding: utf-8 -*-
import numpy as np
from .utils import Utils


class Measurement:
    """The Measurement class
           :param dim: The dimension.
    """
    def __init__(self, dim=3):
        """The measurement mean z and covariance R
        are initialized here.
        """
        if Utils.checkDimension(dim):
            self.dim = dim
            self.z = np.zeros(dim)
            self.R = np.identity(dim)

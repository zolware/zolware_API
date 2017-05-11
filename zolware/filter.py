# -*- coding: utf-8 -*-
import numpy as np
from filterpy.kalman import KalmanFilter
from .measurements import Measurements
from .state import State
from .process import Process
from .system import System

class Filter:
    """The Filter class:
       Get the x, and P prior and 
       get the F, Q, H, R matrices
    """
    def __init__(self, state, signal, mode=''):
        self.process = Process(self.signal.dt,
                               self.state)
        self.measurement = System()
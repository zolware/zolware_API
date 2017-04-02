# -*- coding: utf-8 -*-
import os
import numpy as np
from .utils import SIG_FILE_NAME, Utils


class Sensors:
    """The Signal class
    """
    def __init__(self, filename=SIG_FILE_NAME):
        """The state vector x and covariance matrix P are initialized here.
            :param dt: The uniform timestep
            :param filename: The file countaining the data
        """
        self.signals = []
        self.loadSignal(filename)

    def loadSignal(self, filename):
        """
        """
        if not os.path.exists(SIG_FILE_NAME):
            # If the data file doesn't exist create it.
            Utils.generateSignal(0.2, 0.2, 11, 1.0, True)
        with open(SIG_FILE_NAME, 'r') as f:
            dtstr = f.readline()
        self.dt = float(dtstr.split("dt=")[1])
        signals = np.loadtxt(filename).T
        if (len(signals.shape)==1):
            self.dim = 1
            self.signals = signals.reshape(1,11)
        else:
            self.dim = signals.shape[0]
            for s in signals:
                self.signals.append(s)

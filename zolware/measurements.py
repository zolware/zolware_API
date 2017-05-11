# -*- coding: utf-8 -*-
import os
import numpy as np
#from .utils import SIG_FILE_NAME, Utils


class Measurements:
    """The Signal class:
       Signal is either, Temperature, load, frequency or pattern.  
       Condition the raw data from a sensor or
       multiple sensors to generate a signal
       usable by the model.
    """
    def __init__(self, filename='', stype='Temperature',
                 sensors=[]):
        """
        """
        self.z = []
        self.sensors = sensors # from structure.sensors[]
        self.type = stype 
        #self.filename = filename

    def condition_raw_data(self):
        """Take raw data from sensors and generate the signal
        """
        pass
        #self.loadSignal(self.filename) # temporary
"""
    def loadSignal(self, filename):
        if not os.path.exists(SIG_FILE_NAME):
            # If the data file doesn't exist create it.
            Utils.generateSignal(0.2, 0.2, 11, 1.0, True)
        with open(SIG_FILE_NAME, 'r') as f:
            dtstr = f.readline()
        self.dt = float(dtstr.split("dt=")[1])
        signals = np.loadtxt(filename).T
        if (len(signals.shape)==1):
            self.dim = 1
            self.z = signals.reshape(1,11)
        else:
            self.dim = signals.shape[0]
            for s in signals:
                self.z.append(s)
"""
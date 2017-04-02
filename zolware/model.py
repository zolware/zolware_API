# -*- coding: utf-8 -*-
import os
import json
import numpy as np
from filterpy.kalman import predict
from filterpy.kalman import update
from filterpy.kalman import KalmanFilter
from .utils import DATA_DIR, CONFIG_FILE_NAME, Utils
from .state import State
from .sensors import Sensors
from .process import Process
from .measurement import Measurement


class Model:
    """The model class
    """
    def __init__(self):
        self.sensors = Sensors()
        self.loadSettings()
        self.process = Process(self.sensors,
                               self.state)
        self.measurement = Measurement(self.sensors)

    def loadSettings(self):
        """Load settings from JSON file.
        """
        if not os.path.exists(CONFIG_FILE_NAME):
            # If the configuration file doesn't exist create one.
            Utils.writeDefaultConfig()
        with open(CONFIG_FILE_NAME) as json_file:  
            settings = json.load(json_file)
        self.settings = settings
        self.name = self.settings['name']
        self.state = State(self.settings['x0'],
                           self.settings['P0'])

    def compute(self):
        """Compute
        """
        kf = KalmanFilter(dim_x=self.state.dim, dim_z=self.sensors.dim)
        kf.x = self.state.x  # location and velocity
        kf.P[:] = self.state.P  # covariance matrix 
        kf.F = self.process.F  # state transition matrix
        kf.Q[:] = self.process.Q
        kf.H = self.measurement.H  # Measurement function
        kf.R[:] = self.measurement.R  # measurement uncertainty
        xs , cov = [], []
        zs = self.sensors.signals[0]
        for z in zs:
            kf.predict()
            kf.update(z)
            xs.append(kf.x)
            cov.append(kf.P)
        xs, cov = np.array(xs), np.array(cov)
        return {'xs':xs, 'cov': cov}
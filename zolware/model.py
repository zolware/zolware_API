# -*- coding: utf-8 -*-
import os
import json
import numpy as np
from filterpy.common import Q_discrete_white_noise
from filterpy.kalman import predict
from filterpy.kalman import update
from filterpy.kalman import KalmanFilter
from .utils import DATA_DIR, CONFIG_FILE_NAME, Utils
from .state import State


class Model:
    """The model class
    """
    def __init__(self):
        self.loadSettings()
        # timestep
        self.dt = 0.1
        # dimension state vector
        self.dim_x = 2
        # dimension measurements vector (number of sensors)
        self.dim_z = 1

        # Process
        # process model
        self.F = np.array([[1, self.dt],
                           [0, 1]])
        # process noise
        self.Q = Q_discrete_white_noise(dim=2, dt=1., var=2.35)
        # Control model function
        self.B = 0.
        # control input
        self.u = 0

        # Measurements
        # measurement function
        self.H = np.array([[1., 0.]])
        # measurement covariance
        self.R = np.array([[5.]])
        # measurements
        self.exact, self.z = Utils.generateData(0, 0, 50, self.dt)


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
        kf = KalmanFilter(dim_x=self.dim_x, dim_z=self.dim_z)
        kf.x = self.state.x  # location and velocity
        kf.P[:] = self.state.P  # covariance matrix 
        kf.F = self.F  # state transition matrix
        kf.Q[:] = self.Q
        kf.H = self.H  # Measurement function
        kf.R[:] = self.R  # measurement uncertainty
        xs , cov = [], []
        for z in self.z:
            kf.predict()
            kf.update(z)
            xs.append(kf.x)
            cov.append(kf.P)
        xs, cov = np.array(xs), np.array(cov)
        return {'xs':xs, 'cov': cov}
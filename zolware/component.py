# -*- coding: utf-8 -*-
from .filter import Filter
from .measurements import Measurements
from filterpy.kalman import predict
from filterpy.kalman import update

class Component:
    """The Component class:
       Component type is: temperature, load or frequency
       Filter type is: Linear,
                       Unscented,
                       Extended,
                       GPB2,
                       IMM
        For GPB2 and IMM, more than one filter is used.
        Each filter represents a mode, e.g. constant velocity,
        constant acceleration, etc. 
    """
    def __init__(self, signal, ftype='Linear'):
        self.signal = signal
        self.ctype = signal.type  # T, f or L
        self.ftype = ftype
        self.filters = []  # contains the parameters for each mode

    def learn_parameters(self):
        """scipy.optimize.newton
           likelihood can be obtained by filter.L
           use the parameters class for the EM process
        """
        pass

    def compute(self):
        """Compute
        """
        pass
        #kf = KalmanFilter(dim_x=self.state.dim, dim_z=self.signal.dim)
        #kf.x = self.state.x  # location and velocity
        #kf.P[:] = self.state.P  # covariance matrix 
        #kf.F = self.process.F  # state transition matrix
        #kf.Q[:] = self.process.Q
        #kf.H = self.measurement.H  # Measurement function
        #kf.R[:] = self.measurement.R  # measurement uncertainty
        #xs , cov = [], []
        #zs = self.signal.z[0]
        #for z in zs:
        #    kf.predict()
        #    kf.update(z)
        #    xs.append(kf.x)
        #    cov.append(kf.P)
        #xs, cov = np.array(xs), np.array(cov)
        #return {'xs':xs, 'cov': cov}

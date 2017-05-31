# -*- coding: utf-8 -*-
import numpy as np
from scipy import optimize
from scipy.misc import derivative

class Parameters:
    """The Parameters class:
       param: x the list of parameters.
    """
    def __init__(self, x):
      self.x = x

    def flike(self, ind):
        """Simulates loglikelihood
           ind is the indice of the varying parameter
        """
        if ind==1:
            # simulates filter.l for the given parameter and other kept constant
            return lambda x: -self.x[0]  + 0.5 * (self.x[0] - x)**3 - 1.0
        else:
            return lambda x: -x  + 0.5 * (x - self.x[1])**3 - 1.0

    def jac(self, x):
        """Gives the jacobian of f(x0, x1) 
        """
        j0=derivative(self.flike(0), x[0], dx=1e-6)
        j1=derivative(self.flike(1), x[1], dx=1e-6)
        return [j0, j1]

    def max(self):
      """Gives the maximum loglikelihood for parameters x
      """
      sol = optimize.root(self.jac, self.x, method='hybr')
      return sol.x
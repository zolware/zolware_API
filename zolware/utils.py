# -*- coding: utf-8 -*-
import os
import sys
import numbers
import subprocess
import click
import json
import math
import numpy as np
from datetime import date, datetime, timedelta
from numpy.random import randn
from unipath import Path
from . import __version__


"""PATHS AND FILES:
"""
BASE_DIR = Path(__file__).ancestor(2)
DATA_DIR = BASE_DIR.child("data")
CONFIG_FILE_NAME = BASE_DIR.child('config.json')
SIG_FILE_NAME = DATA_DIR.child('data.txt')

"""DEFAULT_SETTINGS:
"""
DEFAULT_SETTINGS = {'name': 'MyModel',
                    'x0': [10.0, 4.5],
                    'P0': [500, 49],
                    }


class Utils:
    """UTIL:
    """
    def __init__(self):
        pass

    @staticmethod
    def generateSignal(z_var, process_var, count=1, dt=1., save=False):
        """save a txt file containing the time series and
           returns the exact and simulated signals.
               :param z_var: sensor variance
               :param process_var: process variance
               :param count: length of the time series
               :param dt: uniform timestep
               :param save: True if saving a file
               :returns: The exact and simulated signals
        """
        x, xdot = 0., 1.
        z_std = math.sqrt(z_var) 
        p_std = math.sqrt(process_var)
        xs, zs = [], []
        for _ in range(count):
            v = xdot + (randn() * p_std * dt)
            x += v*dt       
            xs.append(x)
            zs.append(x + randn() * z_std)
        if save:
            if not os.path.exists(DATA_DIR):
                os.makedirs(DATA_DIR)
            np.savetxt(SIG_FILE_NAME, np.array(zs).T, header="dt={0}".format(dt))
        return np.array(xs), np.array(zs)
    
    @staticmethod
    def validate_signal(ctx, param, values):
        """
        """
        if not values:
            return
        message = "\nThe arguments must be positive numbers in the "+\
                  "following format:\nfloat var_z, float var_p, int l, float dt."
        for v in values:
            if(isinstance(v, numbers.Real) and v>=0):
                pass
            else:
                raise click.BadParameter(message)
        if(values[2]==0):
            length = 1
        else:
            length = int(values[2])
        if(values[3]==0.0):
            dt = 1.0
        else:
            dt = values[3]
        return [values[0], values[1], length, dt]


    @staticmethod
    def print_version(ctx, param, value):
        """
        Prints the version and exits the program in the callback.
            :param click.context ctx: Click internal object that holds state
                                  relevant for the script execution.
            :param click.core.option param: The option.
            :param bool value: Close the programm without printing the version if
                               False.
        """
        if not value or ctx.resilient_parsing:
            return
        click.echo('zolware {0} (Python {1})'.format(
            __version__,
            sys.version[:3]
        ))
        ctx.exit()

    @staticmethod
    def editConfig():
        """
        Launch VI and allow editing the configuration file.
        VI is the default text editor in Unix systems.
        :param filename: The name of the configuration file.
        """
        subprocess.call(['vi', CONFIG_FILE_NAME])

    @staticmethod
    def writeDefaultConfig():
        '''Write default configuration file.
        '''
        settings = DEFAULT_SETTINGS
        Utils.writeConfig(settings)

    @staticmethod
    def writeConfig(settings):
        '''Write or overwrite config.json using the provided settings.
        '''
        with open(BASE_DIR.child("config.json"),'w') as cfgfile:
            json.dump(settings, cfgfile)

    @staticmethod
    def checkPositiveInteger(value,
                             message='The entered value '+
                                     'must be a positive '+
                                     'integer.'):
        """
        """
        if not isinstance(value, numbers.Integral):
            raise ValueError(message)
        else:
            if value <= 0.0:
                raise ValueError(message)
        return True

    @staticmethod
    def checkPositiveReal(value,
                          message='The entered value '+
                                     'must be a positive '+
                                     'real number.'):
        """
        """
        if not isinstance(value, numbers.Real):
            raise ValueError(message)
        else:
            if value <= 0.0:
                raise ValueError(message)
        return True

    @staticmethod
    def generate_temperature_data(mu, sigma,
                                  start,
                                  end,
                                  delta={'minutes':30}):
        '''Simulated temperatures
            param: mu mean
            param: sigma standard deviation 
        '''
        data = {'timestamps':[], 'temperatures':[]}
        for dt in Utils.datetime_range(start, end, delta):
            data['timestamps'].append(dt)
            data['temperatures'].append(np.random.normal(mu, sigma))
        return data
    
    @staticmethod
    def datetime_range(start, end, delta):
        current = start
        if not isinstance(delta, timedelta):
            delta = timedelta(**delta)
        while current < end:
            yield current
            current += delta
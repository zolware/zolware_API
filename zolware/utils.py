# -*- coding: utf-8 -*-
import os
import sys
import numbers
import subprocess
import click
import json
import math
import numpy as np
from numpy.random import randn
from unipath import Path
from . import __version__


"""PATHS AND FILES:
"""
BASE_DIR = Path(__file__).ancestor(2)
DATA_DIR = BASE_DIR.child("data")
CONFIG_FILE_NAME = BASE_DIR.child('config.json')

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
    def generateData(z_var, process_var, count=1, dt=1.):
        "returns track, measurements 1D ndarrays"
        x, vel = 0., 1.
        z_std = math.sqrt(z_var) 
        p_std = math.sqrt(process_var)
        xs, zs = [], []
        for _ in range(count):
            v = vel + (randn() * p_std * dt)
            x += v*dt        
            xs.append(x)
            zs.append(x + randn() * z_std)        
        return np.array(xs), np.array(zs)

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
    def checkDimension(dim):
        """Check if the dimension is a positive integer.
        """
        message = 'The dimension must be a positive integer.'
        if not isinstance(dim, numbers.Integral):
            raise ValueError(message)
        else:
            if dim <= 0.0:
                raise ValueError(message)
        return True
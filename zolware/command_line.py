# -*- coding: utf-8 -*-
import os
import click
import numpy as np
from .utils import BASE_DIR, DATA_DIR, CONFIG_FILE_NAME, SIG_FILE_NAME, Utils
from .model import Model


@click.command()
@click.option('-c', '--config', is_flag=True,
              help="Edit configuration file and exit.")
@click.option('-r', '--reset', is_flag=True,
              help="Reset configuration file to default and exit.")
@click.option('-g', '--gui', is_flag=True,
              help="Use the graphical user interface.")
@click.option('-s','--signal', nargs=4, type=float, callback=Utils.validate_signal,
              help="Generate a linear time series (slope dt) with random noise and exit. "+
                   "Usage: zolware -s var_z var_p l dt. If l or dt are zero a default\n"+
                   "value of l=1 and dt=1.0 will be assigned to the parameters.")
@click.option(
    '-v', '--version',
    is_flag=True, help='Show version information and exit.',
    callback=Utils.print_version, expose_value=False, is_eager=True,
)
def main(gui, config, reset, signal):
    """
    ZOLWARE: API for Structural Health Monitoring.
    """
    if not os.path.exists(CONFIG_FILE_NAME):
        # If the configuration file doesn't exist create one.
        Utils.writeDefaultConfig()
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    if reset:
        # Reset the configuration file and exit.
        print("Reseting the configuration file to default values.")
        Utils.writeDefaultConfig()
    elif config:
        # Edit the configuration file in terminal with vi and exit.
        Utils.editConfig()
    elif gui:
        # Edit the configuration file using the GUI.
        print("This functionality hasn't been implemented yet.")
    elif signal:
        # Generate dummy signal and exit.
        print("Generating a dummy signal.")
        Utils.generateSignal(*signal, True)
        print("The data are saved in {0}.".format(SIG_FILE_NAME))
    else:  # compute and save the solution for the specified parameters.
        m = Model()
        sol = m.compute()
        output = m.name+".txt"
        # save the solution file
        try:
            # save output
            sim = m.sensors.signals[0]
            exact = sol['xs'].T[0]
            estimated = sol['xs'].T[1]
            np.savetxt(DATA_DIR.child(output) , np.vstack((exact, sim, estimated)).T,
                       header="exact    simulated    estimated")
        except:
            raise IOError("can't save the file")

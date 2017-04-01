# -*- coding: utf-8 -*-
import os
import click
from .utils import BASE_DIR, DATA_DIR, CONFIG_FILE_NAME, Utils
from .model import Model


@click.command()
@click.option('-c', '--config', is_flag=True,
              help="Edit configuration file and exit.")
@click.option('-r', '--reset', is_flag=True,
              help="Reset configuration file to default and exit.")
@click.option('-g', '--gui', is_flag=True,
              help="Use the graphical user interface.")
@click.option(
    '-v', '--version',
    is_flag=True, help='Show version information and exit.',
    callback=Utils.print_version, expose_value=False, is_eager=True,
)
def main(gui, config, reset):
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
        Utils.writeDefaultConfig()
    elif config:
        # Edit the configuration file in terminal with vi and exit.
        Utils.editConfig()
    elif gui:
        # Edit the configuration file using the GUI.
        print("This functionality hasn't been implemented yet.")
    else:  # compute and save the solution for the specified parameters.
        m = Model()
        sol = m.compute()
        output = m.name+".txt"
        # save the solution file
        if not os.path.exists(os.path.dirname(output)):
            try:
                os.makedirs(os.path.dirname(output))
            except:
                pass
        print(sol.get('xs'))

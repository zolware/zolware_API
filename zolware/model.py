# -*- coding: utf-8 -*-
import os
import json
from .utils import DATA_DIR, CONFIG_FILE_NAME, Utils



class Model:
    """The model class:
       Assemble the components to create the global matrices.
    """
    def __init__(self):
        pass


    def loadSettings(self):
        """Load settings from JSON file.
        """
        if not os.path.exists(CONFIG_FILE_NAME):
            # If the configuration file doesn't exist create one.
            Utils.writeDefaultConfig()
        with open(CONFIG_FILE_NAME) as json_file:  
            settings = json.load(json_file)


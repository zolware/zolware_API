# -*- coding: utf-8 -*-
from .sensor import Sensor


class Structure:
    """The Stucture class (DB Model):
    Contains the structure information and
    the timestamps obtained from the redis db.
    """
    def __init__(self, server={}, name='', timestamps=[], sensors=[]):
        """
        """
        self.server = server
        self.name = name
        self.timestamps = timestamps
        self.sensors = sensors

    def add_sensor(self, sensor):
        """
        """
        self.sensors.append(sensor)

    def add_timestamps(self, timestamps):
        """
        """
        self.timestamps.append(timestamps)

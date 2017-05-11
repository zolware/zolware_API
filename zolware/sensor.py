# -*- coding: utf-8 -*-
class Sensor:
    """The Sensor class (DB Model):
       Contains the sensor information and raw_data
       obtained from the redis db.
    """
    def __init__(self, label, stype, units, raw_data,
                 **kwargs):
        """
        """
        if kwargs is not None:
            self.location = ''
            self.properties = {}
            if 'location' in kwargs:
                self.location = kwargs['location']
            if 'properties' in kwargs:
                self.properties = kwargs['properties']
        self.label = label
        self.type = stype
        self.units = units
        self.raw_data = raw_data

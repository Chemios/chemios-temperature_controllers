# -*- coding: utf-8 -*-

"""Base Class for Temperature Controllers"""

from abc import ABC

class TemperatureControllers(ABC):
    '''Base Class for Temperature Controllers
    '''
    def get_current_temperature(self):
        ''' Method to get the current temperature
        Returns:
            update: dict

            update = {
                       'temp_set_point': setpoint in °C,
                       'current_temp': temperature in °C
                    }
        '''

    def set_temperature(self, temp_set_point):
        ''' Method to set the temperature
        Args:
            temp_set_point (float): temperature setpoint in °C
        Returns:
            update: dict

            update = {
                       'temp_set_point': setpoint in °C,
                       'current_temp': temperature in °C
                    }
        '''

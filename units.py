# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 22:05:38 2020.

@author: Tomas Adamek
"""


class Time():
    """
    Define time units.

    val = number
    unit = stirng, ('s' = seconds, 'min' = minutes, 'h' = hours)
    """

    def __init__(self, val, unit='s'):
        """Class return number with unit."""
        if unit == 's':
            self.unit = unit
        elif unit == 'min':
            self.unit = unit
        elif unit == 'h':
            self.unit = 'h'
        else:
            raise Exception('non-specific unit.')
        self.val = val

    def __str__(self):
        """For print and string."""
        return str(self.val) + self.unit

    def __int__(self):
        """For int() function."""
        return int(round(self.val))

    def __float__(self):
        """For float() function."""
        return float(self.val)

    def increase(self):
        """Increase uint."""
        if self.unit == 's':
            self.val /= 60
            self.unit = 'min'
        elif self.unit == 'min':
            self.val /= 60
            self.unit = 'h'
        else:
            raise Exception('Not possible increase unit.')

    def reduce(self):
        """Reduce unit."""
        if self.unit == 'h':
            self.val *= 60
            self.unit = 'min'
        elif self.unit == 'min':
            self.val *= 60
            self.unit = 'h'
        else:
            raise Exception('Not possible reduce unit.')

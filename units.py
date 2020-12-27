# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 22:05:38 2020.

@author: Tomas Adamek
"""
import math


# %% SI units
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
            self.unit = unit
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


class Length():
    """
    Define lenght units.

    val = number
    unit = string, ('m' = meters, 'km' = kilometers, 'dm' = decimeters,
                    'cm' = centimeters, 'mm' = milimeters)
    """

    def __init__(self, val, unit='m'):
        """Class return number with unit."""
        if unit == 'm':
            self.unit = unit
        elif unit == 'km':
            self.unit = unit
        elif unit == 'dm':
            self.unit = unit
        elif unit == 'cm':
            self.unit = unit
        elif unit == 'mm':
            self.unit = unit
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
        if self.unit == 'km':
            self.val /= 1000
            self.unit = 'm'
        elif self.unit == 'm':
            self.val /= 10
            self.unit = 'dm'
        elif self.unit == 'dm':
            self.val /= 10
            self.unit = 'cm'
        elif self.unit == 'cm':
            self.val /= 10
            self.unit = 'mm'
        else:
            raise Exception('Not possible increase unit.')

    def reduce(self):
        """Reduce unit."""
        if self.unit == 'mm':
            self.val *= 10
            self.unit = 'cm'
        elif self.unit == 'cm':
            self.val *= 10
            self.unit = 'dm'
        elif self.unit == 'dm':
            self.val *= 10
            self.unit = 'm'
        elif self.unit == 'm':
            self.val *= 1000
            self.unit = 'km'
        else:
            raise Exception('Not possible reduce unit.')


class Mass():
    """
    Define mass units.

    val = number
    unit = string, ('kg' = kilograms, 't' = tuns, 'g' = grams)
    """

    def __init__(self, val, unit='kg'):
        """Class return number with unit."""
        if unit == 'kg':
            self.unit = unit
        elif unit == 't':
            self.unit = unit
        elif unit == 'g':
            self.unit = unit
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
        if self.unit == 't':
            self.val /= 1000
            self.unit = 'kg'
        elif self.unit == 'kg':
            self.val /= 1000
            self.unit = 'g'
        else:
            raise Exception('Not possible increase unit.')

    def reduce(self):
        """Reduce unit."""
        if self.unit == 'g':
            self.val *= 1000
            self.unit = 'kg'
        elif self.unit == 'kg':
            self.val *= 1000
            self.unit = 't'
        else:
            raise Exception('Not possible reduce unit.')


# %% other units
class Angle():
    """
    Define rotation units.

    val = number
    unit = string, ('rad' = radians, 'deg' = degrees)
    """

    def __init__(self, val, unit='rad'):
        """Class return number with unit."""
        if unit == 'rad':
            self.unit = unit
        elif unit == 'deg':
            self.unit = unit
        elif unit == 'g':
            self.unit = unit
        else:
            raise Exception('non-specific unit.')
        self.val = val

    def __str__(self):
        """For print and string."""
        if self.unit == 'deg':
            return str(self.val) + "\xb0"
        else:
            return str(self.val) + self.unit

    def __int__(self):
        """For int() function."""
        return int(round(self.val))

    def __float__(self):
        """For float() function."""
        return float(self.val)

    def toRad(self):
        """Convert to radians."""
        if self.unit == 'deg':
            self.val = math.radians(self.val)
            self.unit = 'rad'
        elif self.unit == 'rad':
            pass
        else:
            raise Exception('Not possible convert.')

    def toDeg(self):
        """Convert to degrees."""
        if self.unit == 'rad':
            self.val = math.degrees(self.val)
        elif self.unit == 'deg':
            pass
        else:
            raise Exception('Not possible convert.')

    def sin(self):
        """Sinus."""
        if self.unit == 'deg':
            return math.sin(math.radians(self.val))
        elif self.unit == 'rad':
            return math.sin(self.val)
        else:
            raise Exception('Unsupported format.')

    def cos(self):
        """Cosinus."""
        if self.unit == 'deg':
            return math.cos(math.radians(self.val))
        elif self.unit == 'rad':
            return math.cos(self.val)
        else:
            raise Exception('Unsupported format.')

    @staticmethod
    def asin(sin, unit):
        """Create rotation unit from sinus."""
        val = math.acos(sin)
        unit = unit
        if unit == 'deg':
            val = round(math.degrees(val), 13)
        return Angle(val, unit)

    @staticmethod
    def acos(cos, unit='rad'):
        """Create rotation unit from cosinus."""
        val = math.acos(cos)
        unit = unit
        if unit == 'deg':
            val = round(math.degrees(val), 13)
        return Angle(val, unit)

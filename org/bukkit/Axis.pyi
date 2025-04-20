"""
Represents a mutually perpendicular axis in 3D Cartesian coordinates. In
Minecraft the x, z axes lie in the horizontal plane, whilst the y axis points
upwards.
"""
from enum import Enum

class Axis(Enum):
    """
    The x axis.
    """
    X = 1
    """
    The y axis.
    """
    Y = 2
    """
    The z axis.
    """
    Z = 3
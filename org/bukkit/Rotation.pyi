from typing import List
from enum import Enum

class Rotation(Enum):
    """
    An enum to specify a rotation based orientation, like that on a clock.
    It represents how something is viewed, as opposed to cardinal directions.
    """
    """
    No rotation
    """
    NONE = 0
    """
    Rotated clockwise by 45 degrees
    """
    CLOCKWISE_45 = 1
    """
    Rotated clockwise by 90 degrees
    """
    CLOCKWISE = 2
    """
    Rotated clockwise by 135 degrees
    """
    CLOCKWISE_135 = 3
    """
    Flipped upside-down, a 180 degree rotation
    """
    FLIPPED = 4
    """
    Flipped upside-down + 45 degree rotation
    """
    FLIPPED_45 = 5
    """
    Rotated counter-clockwise by 90 degrees
    """
    COUNTER_CLOCKWISE = 6
    """
    Rotated counter-clockwise by 45 degrees
    """
    COUNTER_CLOCKWISE_45 = 7

    rotations: List['Rotation'] = list(Rotation)

    def rotateClockwise(self) -> 'Rotation':
        """
        Rotate clockwise by 90 degrees.
        :return: the relative rotation
        """
        ...

    def rotateCounterClockwise(self) -> 'Rotation':
        """
        Rotate counter-clockwise by 90 degrees.
        :return: the relative rotation
        """
        ...
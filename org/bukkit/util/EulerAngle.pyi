from typing import Any

class EulerAngle:
    """
    EulerAngle is used to represent 3 angles, one for each
    axis (x, y, z). The angles are in radians
    """
    
    ZERO: 'EulerAngle'

    def __init__(self: 'EulerAngle', x: float, y: float, z: float) -> None:
        """
        Creates a EularAngle with each axis set to the
        passed angle in radians

        :param x: the angle for the x axis in radians
        :param y: the angle for the y axis in radians
        :param z: the angle for the z axis in radians
        """
        ...

    def get_x(self: 'EulerAngle') -> float:
        """
        Returns the angle on the x axis in radians

        :return: the angle in radians
        """
        ...

    def get_y(self: 'EulerAngle') -> float:
        """
        Returns the angle on the y axis in radians

        :return: the angle in radians
        """
        ...

    def get_z(self: 'EulerAngle') -> float:
        """
        Returns the angle on the z axis in radians

        :return: the angle in radians
        """
        ...

    def set_x(self: 'EulerAngle', x: float) -> 'EulerAngle':
        """
        Return a EulerAngle which is the result of changing
        the x axis to the passed angle

        :param x: the angle in radians
        :return: the resultant EulerAngle
        """
        ...

    def set_y(self: 'EulerAngle', y: float) -> 'EulerAngle':
        """
        Return a EulerAngle which is the result of changing
        the y axis to the passed angle

        :param y: the angle in radians
        :return: the resultant EulerAngle
        """
        ...

    def set_z(self: 'EulerAngle', z: float) -> 'EulerAngle':
        """
        Return a EulerAngle which is the result of changing
        the z axis to the passed angle

        :param z: the angle in radians
        :return: the resultant EulerAngle
        """
        ...

    def add(self: 'EulerAngle', x: float, y: float, z: float) -> 'EulerAngle':
        """
        Creates a new EulerAngle which is the result of adding
        the x, y, z components to this EulerAngle

        :param x: the angle to add to the x axis in radians
        :param y: the angle to add to the y axis in radians
        :param z: the angle to add to the z axis in radians
        :return: the resultant EulerAngle
        """
        ...

    def subtract(self: 'EulerAngle', x: float, y: float, z: float) -> 'EulerAngle':
        """
        Creates a new EulerAngle which is the result of subtracting
        the x, y, z components to this EulerAngle

        :param x: the angle to subtract to the x axis in radians
        :param y: the angle to subtract to the y axis in radians
        :param z: the angle to subtract to the z axis in radians
        :return: the resultant EulerAngle
        """
        ...

    def __eq__(self: 'EulerAngle', o: Any) -> bool:
        ...

    def __hash__(self: 'EulerAngle') -> int:
        ...
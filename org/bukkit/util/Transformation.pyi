from typing import Any
from org.joml import AxisAngle4f, Quaternionf, Vector3f

class Transformation:
    """
    Represents an arbitrary affine transformation.
    """

    def __init__(self, translation: Vector3f, leftRotation: AxisAngle4f, scale: Vector3f, rightRotation: AxisAngle4f) -> None:
        """
        Initializes a Transformation with the given parameters.

        :param translation: The translation component.
        :param leftRotation: The left rotation component as an AxisAngle4f.
        :param scale: The scale component.
        :param rightRotation: The right rotation component as an AxisAngle4f.
        """
        ...

    def __init__(self, translation: Vector3f, leftRotation: Quaternionf, scale: Vector3f, rightRotation: Quaternionf) -> None:
        """
        Initializes a Transformation with the given parameters.

        :param translation: The translation component.
        :param leftRotation: The left rotation component as a Quaternionf.
        :param scale: The scale component.
        :param rightRotation: The right rotation component as a Quaternionf.
        """
        ...

    def get_translation(self) -> Vector3f:
        """
        Gets the translation component of this transformation.

        :return: translation component
        """
        ...

    def get_left_rotation(self) -> Quaternionf:
        """
        Gets the left rotation component of this transformation.

        :return: left rotation component
        """
        ...

    def get_scale(self) -> Vector3f:
        """
        Gets the scale component of this transformation.

        :return: scale component
        """
        ...

    def get_right_rotation(self) -> Quaternionf:
        """
        Gets the right rotation component of this transformation.

        :return: right rotation component
        """
        ...

    def __hash__(self) -> int:
        ...
    
    def __eq__(self, obj: Any) -> bool:
        ...
    
    def __str__(self) -> str:
        ...
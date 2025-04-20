from org.bukkit import DyeColor
from org.jetbrains.annotations import Nullable
from typing import Protocol

class Colorable(Protocol):
    """
    An object that can be colored.
    """

        def get_color(self) -> DyeColor:
        """
        Gets the color of this object.
        <br>
        This may be null to represent the default color of an object, if the
        object has a special default color (e.g Shulkers).

        @return: The DyeColor of this object.
        """
        ...

    def set_color(self, color: DyeColor) -> None:
        """
        Sets the color of this object to the specified DyeColor.
        <br>
        This may be null to represent the default color of an object, if the
        object has a special default color (e.g Shulkers).

        @param color: The color of the object, as a DyeColor.
        @raises NullPointerException: if argument is null and this implementation does not support null
        """
        ...
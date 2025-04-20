from typing import List
from org.bukkit import Color
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.jetbrains.annotations import ApiStatus, NotNull

"""
Represents a component which adds custom model data.
"""
class CustomModelDataComponent(ConfigurationSerializable):

    """
    Gets a list of the floats for the range_dispatch model type.

    @return: unmodifiable list
    """
        def get_floats(self) -> List[float]:
        ...

    """
    Sets a list of the floats for the range_dispatch model type.

    @param floats: new list
    """
    def set_floats(self, floats: List[float]) -> None:
        ...

    """
    Gets a list of the booleans for the condition model type.

    @return: unmodifiable list
    """
        def get_flags(self) -> List[bool]:
        ...

    """
    Sets a list of the booleans for the condition model type.

    @param flags: new list
    """
    def set_flags(self, flags: List[bool]) -> None:
        ...

    """
    Gets a list of strings for the select model type.

    @return: unmodifiable list
    """
        def get_strings(self) -> List[str]:
        ...

    """
    Sets a list of strings for the select model type.

    @param strings: new list
    """
    def set_strings(self, strings: List[str]) -> None:
        ...

    """
    Gets a list of colors for the model type's tints.

    @return: unmodifiable list
    """
        def get_colors(self) -> List[Color]:
        ...

    """
    Sets a list of colors for the model type's tints.

    @param colors: new list
    """
    def set_colors(self, colors: List[Color]) -> None:
        ...
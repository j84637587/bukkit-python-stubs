from typing import Set
from org.bukkit import Axis
from org.bukkit.block.data import BlockData

class Orientable(BlockData):
    """
    'axis' represents the axis along whilst this block is oriented.
    <br>
    Some blocks such as the portal block may not be able to be placed in all
    orientations, use {@link #getAxes()} to retrieve all possible such
    orientations.
    """

    def get_axis(self) -> Axis:
        """
        Gets the value of the 'axis' property.

        @return the 'axis' value
        """
        ...

    def set_axis(self, axis: Axis) -> None:
        """
        Sets the value of the 'axis' property.

        @param axis the new 'axis' value
        """
        ...

    def get_axes(self) -> Set[Axis]:
        """
        Gets the axes which are applicable to this block.

        @return the allowed 'axis' values
        """
        ...
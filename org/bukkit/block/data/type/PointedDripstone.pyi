from typing import Set
from org.bukkit.block import BlockFace
from org.bukkit.block.data import Waterlogged
from org.jetbrains.annotations import NotNull

"""
'thickness' represents the dripstone thickness.
<br>
'vertical_direction' represents the dripstone orientation.
<br>
Some blocks may not be able to face in all directions, use
{@link #getVerticalDirections()} to get all possible directions for this
block.
"""
class PointedDripstone(Waterlogged):
    """
    Gets the value of the 'vertical_direction' property.

    @return: the 'vertical_direction' value
    """
        def getVerticalDirection(self) -> BlockFace: ...

    """
    Sets the value of the 'vertical_direction' property.

    @param direction: the new 'vertical_direction' value
    """
    def setVerticalDirection(self, direction: BlockFace) -> None: ...

    """
    Gets the faces which are applicable to this block.

    @return: the allowed 'vertical_direction' values
    """
        def getVerticalDirections(self) -> Set[BlockFace]: ...

    """
    Gets the value of the 'thickness' property.

    @return: the 'thickness' value
    """
        def getThickness(self) -> 'PointedDripstone.Thickness': ...

    """
    Sets the value of the 'thickness' property.

    @param thickness: the new 'thickness' value
    """
    def setThickness(self, thickness: 'PointedDripstone.Thickness') -> None: ...

    """
    Represents the thickness of the dripstone, corresponding to its position
    within a multi-block dripstone formation.
    """
    class Thickness:
        """
        Extended tip.
        """
        TIP_MERGE = ...  # type: ignore

        """
        Just the tip.
        """
        TIP = ...  # type: ignore

        """
        Top section.
        """
        FRUSTUM = ...  # type: ignore

        """
        Middle section.
        """
        MIDDLE = ...  # type: ignore

        """
        Base.
        """
        BASE = ...  # type: ignore
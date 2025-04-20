from typing import Set
from org.bukkit.block.data import BlockData
from org.jetbrains.annotations import NotNull

class BrewingStand(BlockData):
    """
    Interface to the 'has_bottle_0', 'has_bottle_1', 'has_bottle_2' flags on a
    brewing stand which indicate which bottles are rendered on the outside.
    <br>
    Stand may have 0, 1... {@link #getMaximumBottles()}-1 bottles.
    """

    def has_bottle(self, bottle: int) -> bool:
        """
        Checks if the stand has the following bottle

        @param bottle to check
        @return if bottle is present
        """
        ...

    def set_bottle(self, bottle: int, has: bool) -> None:
        """
        Set whether the stand has this bottle present.

        @param bottle to set
        @param has bottle
        """
        ...

        def get_bottles(self) -> Set[int]:
        """
        Get the indexes of all the bottles present on this block.

        @return set of all bottles
        """
        ...

    def get_maximum_bottles(self) -> int:
        """
        Get the maximum amount of bottles present on this stand.

        @return maximum bottle count
        """
        ...
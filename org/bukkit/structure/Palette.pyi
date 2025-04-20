from typing import List
from org.bukkit.block import BlockState
from org.jetbrains.annotations import NotNull

class Palette:
    """
    Represent a variation of a structure.

    Most structures, like the ones generated with structure blocks, only have a
    single variant.
    """

        def get_blocks(self) -> List[BlockState]:
        """
        Gets a copy of the blocks this Palette is made of.

        The {@link BlockState#getLocation() positions} of the returned block
        states are offsets relative to the structure's position that is provided
        once the structure is placed into the world.

        @return The blocks in this palette
        """
        ...

    def get_block_count(self) -> int:
        """
        Gets the number of blocks stored in this palette.

        @return The number of blocks in this palette
        """
        ...
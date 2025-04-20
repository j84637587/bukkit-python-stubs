from typing import List
from org.bukkit.block import Block, BlockState
from org.bukkit.entity import Player
from org.bukkit.inventory import ItemStack
from org.jetbrains.annotations import NotNull

class BlockPlaceEvent:
    def __init__(self, block: Block, block_state: BlockState, clicked: Block, item_in_hand: ItemStack, the_player: Player, can_build: bool) -> None:
        ...

class BlockMultiPlaceEvent(BlockPlaceEvent):
    states: List[BlockState]

    def __init__(self, states: List[BlockState], clicked: Block, item_in_hand: ItemStack, the_player: Player, can_build: bool) -> None:
        """
        Fired when a single block placement action of a player triggers the
        creation of multiple blocks(e.g. placing a bed block). The block returned
        by {@link #getBlockPlaced()} and its related methods is the block where
        the placed block would exist if the placement only affected a single
        block.
        """
        ...

        def get_replaced_block_states(self) -> List[BlockState]:
        """
        Gets a list of blockstates for all blocks which were replaced by the
        placement of the new blocks. Most of these blocks will just have a
        Material type of AIR.

        @return: immutable list of replaced BlockStates
        """
        ...
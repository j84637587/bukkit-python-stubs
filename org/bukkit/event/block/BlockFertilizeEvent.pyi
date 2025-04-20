from typing import List, Optional
from org.bukkit.block import Block, BlockState
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.event.block import BlockEvent
from org.jetbrains.annotations import NotNull, Nullable

class BlockFertilizeEvent(BlockEvent, Cancellable):
    """
    Called with the block changes resulting from a player fertilizing a given
    block with bonemeal. Will be called after the applicable
    {@link StructureGrowEvent}.
    """

    handlers: HandlerList

    def __init__(self, the_block: Block, player: Optional[Player], blocks: List[BlockState]) -> None:
        ...

        def getPlayer(self) -> Optional[Player]:
        """
        Gets the player that triggered the fertilization.

        @return triggering player, or null if not applicable
        """
        ...

        def getBlocks(self) -> List[BlockState]:
        """
        Gets a list of all blocks changed by the fertilization.

        @return list of all changed blocks
        """
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancelled: bool) -> None:
        ...

        def getHandlers(self) -> HandlerList:
        ...

        @staticmethod
    def getHandlerList() -> HandlerList:
        ...
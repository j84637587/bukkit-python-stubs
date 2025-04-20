from typing import List
from org.bukkit.block import Block
from org.bukkit.block import BlockState
from org.bukkit.entity import Item
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.jetbrains.annotations import NotNull

class BlockDropItemEvent(BlockEvent, Cancellable):
    """
    Called if a block broken by a player drops an item.

    If the block break is cancelled, this event won't be called.

    If isDropItems in BlockBreakEvent is set to false, this event won't be
    called.

    This event will also be called if the player breaks a multi block structure,
    for example a torch on top of a stone. Both items will have an event call.

    The Block is already broken as this event is called, so #getBlock() will be
    AIR in most cases. Use #getBlockState() for more Information about the broken
    block.
    """

    def __init__(self, block: NotNull[Block], blockState: NotNull[BlockState], player: NotNull[Player], items: NotNull[List[Item]]) -> None:
        ...

        def getPlayer(self) -> Player:
        ...

        def getBlockState(self) -> BlockState:
        ...

        def getItems(self) -> List[Item]:
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...

        def getHandlers(self) -> HandlerList:
        ...

        @staticmethod
    def getHandlerList() -> HandlerList:
        ...
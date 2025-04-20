from org.bukkit.block import Block
from org.bukkit.block import BlockState
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.jetbrains.annotations import ApiStatus
from org.jetbrains.annotations import NotNull

"""
Called when a block is brushed by a player.
"""
class BlockBrushEvent(BlockEvent, Cancellable):

    handlers: HandlerList = HandlerList()
    player: Player
    newState: BlockState
    cancel: bool

    def __init__(self, theBlock: Block, newState: BlockState, player: Player) -> None:
        ...

    """
    Gets the Player that is brushing the block involved in this event.

    @return The Player that is brushing the block involved in this event
    """
        def getPlayer(self) -> Player:
        ...

    """
    Gets the state of the block that this block will turn into.

    @return The block state that the block will become
    """
        def getNewState(self) -> BlockState:
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
from typing import List
from org.bukkit.Material import Material
from org.bukkit.block.Block import Block
from org.bukkit.block.BlockState import BlockState
from org.bukkit.event.Cancellable import Cancellable
from org.bukkit.event.HandlerList import HandlerList
from org.bukkit.event.block.BlockEvent import BlockEvent
from org.jetbrains.annotations import NotNull

class SpongeAbsorbEvent(BlockEvent, Cancellable):
    """
    Called when a sponge absorbs water from the world.
    <br>
    The world will be in its previous state, and {@link #getBlocks()} will
    represent the changes to be made to the world, if the event is not cancelled.
    <br>
    As this is a physics based event it may be called multiple times for "the
    same" changes.
    """

    handlers: HandlerList = ...
    cancelled: bool
    blocks: List[BlockState]

    def __init__(self, block: Block, waterblocks: List[BlockState]) -> None:
        ...

    """
    Get a list of all blocks to be removed by the sponge.
    <br>
    This list is mutable and contains the blocks in their removed state, i.e.
    having a type of {@link Material#AIR}.

    @return list of the to be removed blocks.
    """
        def getBlocks(self) -> List[BlockState]:
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
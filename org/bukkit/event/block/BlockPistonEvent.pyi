from org.bukkit.Material import Material
from org.bukkit.block.Block import Block
from org.bukkit.block.BlockFace import BlockFace
from org.bukkit.event.Cancellable import Cancellable
from org.bukkit.event.block.BlockEvent import BlockEvent
from typing import Any

class BlockPistonEvent(BlockEvent, Cancellable):
    """
    Called when a piston block is triggered
    """

    def __init__(self, block: Block, direction: BlockFace) -> None:
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancelled: bool) -> None:
        ...

    def isSticky(self) -> bool:
        """
        Returns true if the Piston in the event is sticky.

        @return: stickiness of the piston
        """
        ...

    def getDirection(self) -> BlockFace:
        """
        Return the direction in which the piston will operate.

        @return: direction of the piston
        """
        ...
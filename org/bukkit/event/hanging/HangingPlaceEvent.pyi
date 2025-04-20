from org.bukkit.block import Block
from org.bukkit.block import BlockFace
from org.bukkit.entity import Hanging
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.inventory import EquipmentSlot
from org.bukkit.inventory import ItemStack
from typing import Optional

class HangingPlaceEvent(HangingEvent, Cancellable):
    """
    Triggered when a hanging entity is created in the world
    """
    
    handlers: HandlerList

    def __init__(self, hanging: Hanging, player: Optional[Player], block: Block, blockFace: BlockFace, hand: Optional[EquipmentSlot], itemStack: Optional[ItemStack] = None) -> None:
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        ...

    def getPlayer(self) -> Optional[Player]:
        """
        Returns the player placing the hanging entity

        @return: the player placing the hanging entity
        """
        ...

    def getBlock(self) -> Block:
        """
        Returns the block that the hanging entity was placed on

        @return: the block that the hanging entity was placed on
        """
        ...

    def getBlockFace(self) -> BlockFace:
        """
        Returns the face of the block that the hanging entity was placed on

        @return: the face of the block that the hanging entity was placed on
        """
        ...

    def getHand(self) -> Optional[EquipmentSlot]:
        """
        Returns the hand that was used to place the hanging entity, or null
        if a player did not place the hanging entity.

        @return: the hand
        """
        ...

    def getItemStack(self) -> Optional[ItemStack]:
        """
        Gets the item from which the hanging entity originated

        @return: the item from which the hanging entity originated
        """
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...

    def getHandlers(self) -> HandlerList:
        ...
from org.bukkit.block import Block
from org.bukkit.block import BlockFace
from org.bukkit.entity import Entity
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.inventory import EquipmentSlot
from typing import Optional

class EntityPlaceEvent(EntityEvent, Cancellable):
    """
    Triggered when a entity is created in the world by a player "placing" an item
    on a block.
    <br>
    Note that this event is currently only fired for four specific placements:
    armor stands, boats, minecarts, and end crystals.
    """

    handlers: HandlerList

    def __init__(self, entity: Entity, player: Optional[Player], block: Block, blockFace: BlockFace, hand: EquipmentSlot) -> None:
        ...

    @classmethod
    def getHandlerList(cls) -> HandlerList:
        ...

    @Deprecated(since="1.19.2")
    def __init__(self, entity: Entity, player: Optional[Player], block: Block, blockFace: BlockFace) -> None:
        ...

    def getPlayer(self) -> Optional[Player]:
        """
        Returns the player placing the entity

        @return: the player placing the entity
        """
        ...

    def getBlock(self) -> Block:
        """
        Returns the block that the entity was placed on

        @return: the block that the entity was placed on
        """
        ...

    def getBlockFace(self) -> BlockFace:
        """
        Returns the face of the block that the entity was placed on

        @return: the face of the block that the entity was placed on
        """
        ...

    def getHand(self) -> EquipmentSlot:
        """
        Get the hand used to place the entity.

        @return: the hand
        """
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...

    def getHandlers(self) -> HandlerList:
        ...
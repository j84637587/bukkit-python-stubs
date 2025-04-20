from org.bukkit.Material import Material
from org.bukkit.entity.Entity import Entity
from org.bukkit.entity.Player import Player
from org.bukkit.event.Cancellable import Cancellable
from org.bukkit.event.HandlerList import HandlerList
from org.bukkit.inventory.EquipmentSlot import EquipmentSlot
from org.bukkit.inventory.ItemStack import ItemStack
from typing import Any

class PlayerShearEntityEvent(PlayerEvent, Cancellable):
    """
    Called when a player shears an entity
    """

    handlers: HandlerList = HandlerList()
    cancel: bool
    what: Entity
    item: ItemStack
    hand: EquipmentSlot

    def __init__(self, who: Player, what: Entity, item: ItemStack, hand: EquipmentSlot) -> None:
        ...

    @classmethod
    def getHandlerList(cls) -> HandlerList:
        ...

    @Deprecated(since="1.15.2")
    def __init__(self, who: Player, what: Entity) -> None:
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...

    def getEntity(self) -> Entity:
        """
        Gets the entity the player is shearing

        :return: the entity the player is shearing
        """
        ...

    def getItem(self) -> ItemStack:
        """
        Gets the item used to shear the entity.

        :return: the shears
        """
        ...

    def getHand(self) -> EquipmentSlot:
        """
        Gets the hand used to shear the entity.

        :return: the hand
        """
        ...

    def getHandlers(self) -> HandlerList:
        ...
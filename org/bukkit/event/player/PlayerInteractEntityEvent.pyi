from org.bukkit.entity import Entity
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.inventory import EquipmentSlot
from typing import Any

class PlayerInteractEntityEvent(PlayerEvent, Cancellable):
    """
    Represents an event that is called when a player right clicks an entity.
    """

    handlers: HandlerList = HandlerList()
    clickedEntity: Entity
    cancelled: bool
    hand: EquipmentSlot

    def __init__(self, who: Player, clickedEntity: Entity) -> None:
        ...

    def __init__(self, who: Player, clickedEntity: Entity, hand: EquipmentSlot) -> None:
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...

    """
    Gets the entity that was right-clicked by the player.

    @return entity right clicked by player
    """
    def getRightClicked(self) -> Entity:
        ...

    """
    The hand used to perform this interaction.

    @return the hand used to interact
    """
    def getHand(self) -> EquipmentSlot:
        ...

    def getHandlers(self) -> HandlerList:
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        ...
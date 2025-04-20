from org.bukkit.entity import Entity
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import Event
from org.bukkit.event import HandlerList
from org.bukkit.inventory import EquipmentSlot
from typing import Literal

class PlayerLeashEntityEvent(Event, Cancellable):
    """
    Called immediately prior to a creature being leashed by a player.
    """
    
    handlers: HandlerList
    leashHolder: Entity
    entity: Entity
    cancelled: bool
    player: Player
    hand: EquipmentSlot

    def __init__(self, what: Entity, leashHolder: Entity, leasher: Player, hand: EquipmentSlot) -> None:
        ...

    @classmethod
    def __init__(self, what: Entity, leashHolder: Entity, leasher: Player) -> None:
        ...

    def getLeashHolder(self) -> Entity:
        """
        Returns the entity that is holding the leash.

        @return: The leash holder
        """
        ...

    def getEntity(self) -> Entity:
        """
        Returns the entity being leashed.

        @return: The entity
        """
        ...

    def getPlayer(self) -> Player:
        """
        Returns the player involved in this event

        @return: Player who is involved in this event
        """
        ...

    def getHand(self) -> EquipmentSlot:
        """
        Returns the hand used by the player to leash the entity.

        @return: the hand
        """
        ...

    def getHandlers(self) -> HandlerList:
        ...

    @classmethod
    def getHandlerList(cls) -> HandlerList:
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...
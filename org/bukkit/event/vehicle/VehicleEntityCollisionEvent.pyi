from org.bukkit.entity import Entity
from org.bukkit.entity import Vehicle
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.vehicle import VehicleCollisionEvent
from typing import Any

class VehicleEntityCollisionEvent(VehicleCollisionEvent, Cancellable):
    """
    Raised when a vehicle collides with an entity.
    """
    handlers: HandlerList

    def __init__(self, vehicle: Vehicle, entity: Entity) -> None:
        ...

    def getEntity(self) -> Entity:
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...

    def isPickupCancelled(self) -> bool:
        ...

    def setPickupCancelled(self, cancel: bool) -> None:
        ...

    def isCollisionCancelled(self) -> bool:
        ...

    def setCollisionCancelled(self, cancel: bool) -> None:
        ...

    def getHandlers(self) -> HandlerList:
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        ...
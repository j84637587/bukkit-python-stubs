from org.bukkit.entity import Entity
from org.bukkit.entity import Vehicle
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.vehicle import VehicleEvent
from typing import Any

class VehicleEnterEvent(VehicleEvent, Cancellable):
    """
    Raised when an entity enters a vehicle.
    """

    handlers: HandlerList = HandlerList()
    cancelled: bool
    entered: Entity

    def __init__(self, vehicle: Vehicle, entered: Entity) -> None:
        """
        Initializes a new VehicleEnterEvent.

        :param vehicle: The vehicle that is being entered.
        :param entered: The entity that entered the vehicle.
        """
        ...

    def getEntered(self) -> Entity:
        """
        Gets the Entity that entered the vehicle.

        :return: the Entity that entered the vehicle
        """
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
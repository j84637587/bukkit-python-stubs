from org.bukkit.entity import LivingEntity
from org.bukkit.entity import Vehicle
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.vehicle import VehicleEvent
from typing import Any

class VehicleExitEvent(VehicleEvent, Cancellable):
    """
    Raised when a living entity exits a vehicle.
    """
    
    handlers: HandlerList = HandlerList()
    cancelled: bool
    exited: LivingEntity

    def __init__(self, vehicle: Vehicle, exited: LivingEntity) -> None:
        """
        Initialize the VehicleExitEvent.

        :param vehicle: The vehicle from which the entity exited.
        :param exited: The living entity that exited the vehicle.
        """
        ...

    def getExited(self) -> LivingEntity:
        """
        Get the living entity that exited the vehicle.

        :return: The entity.
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
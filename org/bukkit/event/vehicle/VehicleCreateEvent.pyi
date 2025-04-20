from org.bukkit.entity import Vehicle
from org.bukkit.event import Cancellable, HandlerList
from typing import Any

class VehicleCreateEvent(VehicleEvent, Cancellable):
    """
    Raised when a vehicle is created.
    """
    
    handlers: HandlerList = HandlerList()
    cancelled: bool

    def __init__(self, vehicle: Vehicle) -> None:
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancelled: bool) -> None:
        ...

    def getHandlers(self) -> HandlerList:
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        ...
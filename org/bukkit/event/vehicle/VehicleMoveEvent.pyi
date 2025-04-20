from org.bukkit.Location import Location
from org.bukkit.entity.Vehicle import Vehicle
from org.bukkit.event.HandlerList import HandlerList
from org.bukkit.event.vehicle.VehicleEvent import VehicleEvent
from typing import Any

class VehicleMoveEvent(VehicleEvent):
    """
    Raised when a vehicle moves.
    """

    handlers: HandlerList = HandlerList()
    from: Location
    to: Location

    def __init__(self, vehicle: Vehicle, from_: Location, to: Location) -> None:
        super().__init__(vehicle)
        self.from = from_
        self.to = to

    """
    Get the previous position.

    @return: Old position.
    """
    def getFrom(self) -> Location:
        ...

    """
    Get the next position.

    @return: New position.
    """
    def getTo(self) -> Location:
        ...

    def getHandlers(self) -> HandlerList:
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        ...
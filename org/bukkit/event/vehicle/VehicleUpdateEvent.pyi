from org.bukkit.entity import Vehicle
from org.bukkit.event import HandlerList
from typing import Any

class VehicleUpdateEvent(VehicleEvent):
    """
    Called when a vehicle updates
    """

    handlers: HandlerList = HandlerList()

    def __init__(self, vehicle: Vehicle) -> None:
        super().__init__(vehicle)

    def get_handlers(self) -> HandlerList:
        return self.handlers

    @staticmethod
    def get_handler_list() -> HandlerList:
        return VehicleUpdateEvent.handlers
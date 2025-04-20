from org.bukkit.event import HandlerList
from org.bukkit.map import MapView
from typing import Any

class MapInitializeEvent(ServerEvent):
    """
    Called when a map is initialized.
    """

    handlers: HandlerList = HandlerList()
    mapView: MapView

    def __init__(self, mapView: MapView) -> None:
        self.mapView = mapView

    """
    Gets the map initialized in this event.

    @return Map for this event
    """
    def get_map(self) -> MapView:
        ...

    @staticmethod
    def get_handler_list() -> HandlerList:
        ...
    
    def get_handlers(self) -> HandlerList:
        ...
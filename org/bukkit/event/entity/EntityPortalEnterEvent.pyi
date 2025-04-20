from org.bukkit.Location import Location
from org.bukkit.entity.Entity import Entity
from org.bukkit.event.HandlerList import HandlerList
from org.bukkit.event.entity.EntityEvent import EntityEvent
from typing import Any

class EntityPortalEnterEvent(EntityEvent):
    """
    Called when an entity comes into contact with a portal
    """

    handlers: HandlerList = HandlerList()
    location: Location

    def __init__(self, entity: Entity, location: Location) -> None:
        super().__init__(entity)
        self.location = location

    """
    Gets the portal block the entity is touching

    @return: The portal block the entity is touching
    """
    def getLocation(self) -> Location:
        ...

    def getHandlers(self) -> HandlerList:
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        ...
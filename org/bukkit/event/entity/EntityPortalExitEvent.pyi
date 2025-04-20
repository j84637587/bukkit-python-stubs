from org.bukkit.Location import Location
from org.bukkit.entity.Entity import Entity
from org.bukkit.event.HandlerList import HandlerList
from org.bukkit.util.Vector import Vector
from typing import Any
from org.bukkit.event.entity.EntityTeleportEvent import EntityTeleportEvent
from typing import Optional

class EntityPortalExitEvent(EntityTeleportEvent):
    """
    Called before an entity exits a portal.
    <p>
    This event allows you to modify the velocity of the entity after they have
    successfully exited the portal.
    """

    handlers: HandlerList

    def __init__(self, entity: Entity, from_location: Location, to_location: Location, before: Vector, after: Vector) -> None:
        ...

    """
    Gets a copy of the velocity that the entity has before entering the
    portal.

    @return velocity of entity before entering the portal
    """
    def get_before(self) -> Vector:
        ...

    """
    Gets a copy of the velocity that the entity will have after exiting the
    portal.

    @return velocity of entity after exiting the portal
    """
    def get_after(self) -> Vector:
        ...

    """
    Sets the velocity that the entity will have after exiting the portal.

    @param after the velocity after exiting the portal
    """
    def set_after(self, after: Vector) -> None:
        ...

    @Override
    def get_handlers(self) -> HandlerList:
        ...

    @staticmethod
    def get_handler_list() -> HandlerList:
        ...
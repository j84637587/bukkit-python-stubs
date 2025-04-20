from org.bukkit.entity import Entity
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.event.entity import EntityEvent
from typing import Any

class EntityMountEvent(EntityEvent, Cancellable):
    """
    Called when an entity attempts to ride another entity.
    """

    handlers: HandlerList = HandlerList()
    cancelled: bool
    mount: Entity

    def __init__(self, what: Entity, mount: Entity) -> None:
        """
        Initializes the EntityMountEvent.

        :param what: The entity that is attempting to ride.
        :param mount: The entity which will be ridden.
        """
        ...

    def get_mount(self) -> Entity:
        """
        Gets the entity which will be ridden.

        :return: mounted entity
        """
        ...

    def is_cancelled(self) -> bool:
        ...
    
    def set_cancelled(self, cancel: bool) -> None:
        ...
    
    def get_handlers(self) -> HandlerList:
        ...
    
    @staticmethod
    def get_handler_list() -> HandlerList:
        ...
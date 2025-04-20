from org.bukkit.entity import Entity
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.event.entity import EntityEvent
from typing import Any

class EntityDismountEvent(EntityEvent, Cancellable):
    """
    Called when an entity stops riding another entity.
    """

    handlers: HandlerList = HandlerList()
    cancelled: bool
    dismounted: Entity

    def __init__(self, what: Entity, dismounted: Entity) -> None:
        """
        Initializes the EntityDismountEvent.

        :param what: The entity that is dismounting.
        :param dismounted: The entity that is being dismounted.
        """
        ...

    def get_dismounted(self) -> Entity:
        """
        Gets the entity which will no longer be ridden.

        :return: dismounted entity
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
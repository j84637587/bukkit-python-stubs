from org.bukkit.entity import AnimalTamer, LivingEntity
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.event.entity import EntityEvent
from typing import Any

class EntityTameEvent(EntityEvent, Cancellable):
    """
    Thrown when a LivingEntity is tamed
    """
    handlers: HandlerList = HandlerList()
    cancelled: bool
    owner: AnimalTamer

    def __init__(self, entity: LivingEntity, owner: AnimalTamer) -> None:
        super().__init__(entity)
        self.owner = owner

    def get_entity(self) -> LivingEntity:
        return self.entity  # type: ignore

    def is_cancelled(self) -> bool:
        return self.cancelled

    def set_cancelled(self, cancel: bool) -> None:
        self.cancelled = cancel

    """
    Gets the owning AnimalTamer

    @return: the owning AnimalTamer
    """
    def get_owner(self) -> AnimalTamer:
        return self.owner

    def get_handlers(self) -> HandlerList:
        return self.handlers

    @staticmethod
    def get_handler_list() -> HandlerList:
        return EntityTameEvent.handlers
from org.bukkit.entity import Item
from org.bukkit.entity import LivingEntity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from typing import Any

class EntityPickupItemEvent(EntityEvent, Cancellable):
    """
    Thrown when a entity picks an item up from the ground
    """
    
    handlers: HandlerList = HandlerList()
    item: Item
    cancel: bool
    remaining: int

    def __init__(self, entity: LivingEntity, item: Item, remaining: int) -> None:
        ...

    def getEntity(self) -> LivingEntity:
        ...

    """
    Gets the Item picked up by the entity.

    @return Item
    """
    def getItem(self) -> Item:
        ...

    """
    Gets the amount remaining on the ground, if any

    @return amount remaining on the ground
    """
    def getRemaining(self) -> int:
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
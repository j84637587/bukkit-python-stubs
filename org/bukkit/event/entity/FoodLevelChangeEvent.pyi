from org.bukkit.entity import HumanEntity
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.inventory import ItemStack
from typing import Optional

class FoodLevelChangeEvent(EntityEvent, Cancellable):
    """
    Called when a human entity's food level changes
    """

    handlers: HandlerList = HandlerList()
    cancel: bool
    level: int
    item: Optional[ItemStack]

    def __init__(self, what: HumanEntity, level: int, item: Optional[ItemStack] = None) -> None:
        ...

    def getEntity(self) -> HumanEntity:
        ...

    """
    Gets the item that triggered this event, if any.

    @return an ItemStack for the item being consumed
    """
    def getItem(self) -> Optional[ItemStack]:
        ...

    """
    Gets the resultant food level that the entity involved in this event
    should be set to.
    <p>
    Where 20 is a full food bar and 0 is an empty one.

    @return The resultant food level
    """
    def getFoodLevel(self) -> int:
        ...

    """
    Sets the resultant food level that the entity involved in this event
    should be set to

    @param level the resultant food level that the entity involved in this
        event should be set to
    """
    def setFoodLevel(self, level: int) -> None:
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
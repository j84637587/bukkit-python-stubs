from typing import List
from org.bukkit.entity import HumanEntity
from org.bukkit.event import Event, HandlerList
from org.bukkit.inventory import Inventory, InventoryView
from org.jetbrains.annotations import NotNull

class InventoryEvent(Event):
    """
    Represents a player related inventory event
    """

    handlers: HandlerList

    def __init__(self, transaction: InventoryView) -> None:
        self.transaction = transaction

    /**
     * Gets the primary Inventory involved in this transaction
     *
     * @return The upper inventory.
     */
        def getInventory(self) -> Inventory:
        ...

    /**
     * Gets the list of players viewing the primary (upper) inventory involved
     * in this event
     *
     * @return A list of people viewing.
     */
        def getViewers(self) -> List[HumanEntity]:
        ...

    /**
     * Gets the view object itself
     *
     * @return InventoryView
     */
        def getView(self) -> InventoryView:
        ...

        def getHandlers(self) -> HandlerList:
        ...

        @staticmethod
    def getHandlerList() -> HandlerList:
        ...
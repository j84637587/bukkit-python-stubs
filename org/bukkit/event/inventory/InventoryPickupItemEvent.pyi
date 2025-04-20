from org.bukkit.entity import Item
from org.bukkit.event import Cancellable, Event, HandlerList
from org.bukkit.inventory import Inventory
from typing import Any

class InventoryPickupItemEvent(Event, Cancellable):
    """
    Called when a hopper or hopper minecart picks up a dropped item.
    """

    handlers: HandlerList

    def __init__(self, inventory: Inventory, item: Item) -> None:
        """
        Initializes the InventoryPickupItemEvent.

        :param inventory: The Inventory that picked up the item
        :param item: The Item entity that was picked up
        """
        ...

    def getInventory(self) -> Inventory:
        """
        Gets the Inventory that picked up the item.

        :return: Inventory
        """
        ...

    def getItem(self) -> Item:
        """
        Gets the Item entity that was picked up.

        :return: Item
        """
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
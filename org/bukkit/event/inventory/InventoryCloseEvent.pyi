from org.bukkit.entity import HumanEntity
from org.bukkit.event import HandlerList
from org.bukkit.inventory import InventoryView
from typing import Any

class InventoryCloseEvent(InventoryEvent):
    """
    Represents a player related inventory event
    """

    handlers: HandlerList = HandlerList()

    def __init__(self, transaction: InventoryView) -> None:
        super().__init__(transaction)

    """
    Returns the player involved in this event

    @return Player who is involved in this event
    """
    def getPlayer(self) -> HumanEntity:
        ...

    def getHandlers(self) -> HandlerList:
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        ...
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.inventory import ItemStack
from typing import Any

class PlayerItemBreakEvent(PlayerEvent):
    """
    Fired when a player's item breaks (such as a shovel or flint and steel).
    <p>
    After this event, the item's amount will be set to {@code item amount - 1}
    and its durability will be reset to 0.
    """

    handlers: HandlerList = HandlerList()
    brokenItem: ItemStack

    def __init__(self, player: Player, brokenItem: ItemStack) -> None:
        super().__init__(player)
        self.brokenItem = brokenItem

    """
    Gets the item that broke

    @return The broken item
    """
    def getBrokenItem(self) -> ItemStack:
        ...

    def getHandlers(self) -> HandlerList:
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        ...
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.inventory import ItemStack
from typing import Any

class PlayerItemDamageEvent(PlayerEvent, Cancellable):
    """
    Called when an item used by the player takes durability damage as a result of
    being used.
    """

    handlers: HandlerList = HandlerList()
    item: ItemStack
    damage: int
    cancelled: bool = False

    def __init__(self, player: Player, what: ItemStack, damage: int) -> None:
        """
        Initializes the PlayerItemDamageEvent.

        :param player: The player involved in the event.
        :param what: The item being damaged.
        :param damage: The amount of damage.
        """
        ...

    def getItem(self) -> ItemStack:
        """
        Gets the item being damaged.

        :return: the item
        """
        ...

    def getDamage(self) -> int:
        """
        Gets the amount of durability damage this item will be taking.

        :return: durability change
        """
        ...

    def setDamage(self, damage: int) -> None:
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
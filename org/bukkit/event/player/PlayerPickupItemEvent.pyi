from org.bukkit.entity import Item
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import EntityPickupItemEvent
from typing import Any

class PlayerPickupItemEvent(PlayerEvent, Cancellable):
    """
    Thrown when a player picks an item up from the ground
    @deprecated {@link EntityPickupItemEvent}
    """
    
    handlers: HandlerList = HandlerList()
    item: Item
    cancel: bool
    remaining: int

    def __init__(self, player: Player, item: Item, remaining: int) -> None:
        """
        Initializes the PlayerPickupItemEvent.

        :param player: The player who picked up the item.
        :param item: The item that was picked up.
        :param remaining: The amount remaining on the ground.
        """
        ...

    def getItem(self) -> Item:
        """
        Gets the Item picked up by the player.

        :return: Item
        """
        ...

    def getRemaining(self) -> int:
        """
        Gets the amount remaining on the ground, if any.

        :return: amount remaining on the ground
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
from org.bukkit.entity import Item
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.player import PlayerEvent
from typing import Any

class PlayerDropItemEvent(PlayerEvent, Cancellable):
    """
    Thrown when a player drops an item from their inventory
    """

    handlers: HandlerList = HandlerList()
    drop: Item
    cancel: bool

    def __init__(self, player: Player, drop: Item) -> None:
        """
        Initializes the PlayerDropItemEvent.

        :param player: The player who dropped the item.
        :param drop: The item that was dropped.
        """
        ...

    def get_item_drop(self) -> Item:
        """
        Gets the ItemDrop created by the player.

        :return: ItemDrop created by the player.
        """
        ...

    def is_cancelled(self) -> bool:
        """
        Checks if the event is cancelled.

        :return: True if the event is cancelled, False otherwise.
        """
        ...

    def set_cancelled(self, cancel: bool) -> None:
        """
        Sets the cancellation state of the event.

        :param cancel: True to cancel the event, False to allow it.
        """
        ...

    def get_handlers(self) -> HandlerList:
        """
        Gets the handler list for this event.

        :return: The handler list.
        """
        ...

    @staticmethod
    def get_handler_list() -> HandlerList:
        """
        Gets the static handler list for this event.

        :return: The static handler list.
        """
        ...
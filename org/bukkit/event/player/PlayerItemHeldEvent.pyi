from org.bukkit.entity import Player
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.event.player import PlayerEvent
from typing import Final

class PlayerItemHeldEvent(PlayerEvent, Cancellable):
    """
    Fired when a player changes their currently held item
    """

    handlers: Final[HandlerList] = HandlerList()
    cancel: bool
    previous: int
    current: int

    def __init__(self, player: Player, previous: int, current: int) -> None:
        """
        Initializes the PlayerItemHeldEvent.

        :param player: The player involved in the event.
        :param previous: The previous held slot index.
        :param current: The new held slot index.
        """
        ...

    def get_previous_slot(self) -> int:
        """
        Gets the previous held slot index.

        :return: Previous slot index.
        """
        ...

    def get_new_slot(self) -> int:
        """
        Gets the new held slot index.

        :return: New slot index.
        """
        ...

    def is_cancelled(self) -> bool:
        ...
    
    def set_cancelled(self, cancel: bool) -> None:
        ...

    def get_handlers(self) -> HandlerList:
        ...

    @staticmethod
    def get_handler_list() -> HandlerList:
        ...
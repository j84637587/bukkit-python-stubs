from org.bukkit.block import Lectern
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.inventory import ItemStack
from typing import Optional

class PlayerTakeLecternBookEvent(PlayerEvent, Cancellable):
    """
    This event is called when a player clicks the button to take a book of a
    Lectern. If this event is cancelled the book remains on the lectern.
    """

    handlers: HandlerList

    def __init__(self, who: Player, lectern: Lectern) -> None:
        ...

    def get_lectern(self) -> Lectern:
        """
        Gets the lectern involved.

        :return: the Lectern
        """
        ...

    def get_book(self) -> Optional[ItemStack]:
        """
        Gets the current ItemStack on the lectern.

        :return: the ItemStack on the Lectern
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
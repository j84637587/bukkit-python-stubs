from org.bukkit.entity import HumanEntity
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.inventory import InventoryView
from typing import Final

class InventoryOpenEvent(InventoryEvent, Cancellable):
    """
    Represents a player related inventory event
    """

    handlers: Final[HandlerList]

    def __init__(self, transaction: InventoryView) -> None:
        """
        Initializes the InventoryOpenEvent with the given InventoryView.

        :param transaction: The InventoryView associated with this event.
        """
        ...

    @property
    def player(self) -> HumanEntity:
        """
        Returns the player involved in this event.

        :return: Player who is involved in this event.
        """
        ...

    def is_cancelled(self) -> bool:
        """
        Gets the cancellation state of this event. A cancelled event will not
        be executed in the server, but will still pass to other plugins.
        If an inventory open event is cancelled, the inventory screen will not
        show.

        :return: true if this event is cancelled.
        """
        ...

    def set_cancelled(self, cancel: bool) -> None:
        """
        Sets the cancellation state of this event. A cancelled event will not
        be executed in the server, but will still pass to other plugins.
        If an inventory open event is cancelled, the inventory screen will not
        show.

        :param cancel: true if you wish to cancel this event.
        """
        ...

    @classmethod
    def get_handlers(cls) -> HandlerList:
        """
        Returns the handler list for this event.

        :return: HandlerList for this event.
        """
        ...

    @classmethod
    def get_handler_list(cls) -> HandlerList:
        """
        Returns the static handler list for this event.

        :return: Static HandlerList for this event.
        """
        ...
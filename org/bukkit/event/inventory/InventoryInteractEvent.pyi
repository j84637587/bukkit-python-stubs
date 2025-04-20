from org.bukkit.entity import HumanEntity
from org.bukkit.event import Cancellable
from org.bukkit.inventory import InventoryView
from org.bukkit.event import Event
from typing import Literal

class InventoryInteractEvent(Event, Cancellable):
    """
    An abstract base class for events that describe an interaction between a
    HumanEntity and the contents of an Inventory.
    """

    def __init__(self, transaction: InventoryView) -> None:
        ...

    @property
    def who_clicked(self) -> HumanEntity:
        """
        Gets the player who performed the click.

        Returns:
            The clicking player.
        """
        ...

    def set_result(self, new_result: Literal['ALLOW', 'DENY', 'DEFAULT']) -> None:
        """
        Sets the result of this event. This will change whether or not this
        event is considered cancelled.

        Args:
            new_result: the new Result for this event
        """
        ...

    @property
    def result(self) -> Literal['ALLOW', 'DENY', 'DEFAULT']:
        """
        Gets the Result of this event. The Result describes the
        behavior that will be applied to the inventory in relation to this
        event.

        Returns:
            The Result of this event.
        """
        ...

    def is_cancelled(self) -> bool:
        """
        Gets whether or not this event is cancelled. This is based off of the
        Result value returned by getResult(). Result.ALLOW and
        Result.DEFAULT will result in a returned value of false, but
        Result.DENY will result in a returned value of true.

        Returns:
            Whether the event is cancelled.
        """
        ...

    def set_cancelled(self, to_cancel: bool) -> None:
        """
        Proxy method to setResult for the Cancellable
        interface. setResult is preferred, as it allows
        you to specify the Result beyond Result.DENY and Result.ALLOW.

        Args:
            to_cancel: result becomes DENY if true, ALLOW if false
        """
        ...
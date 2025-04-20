from org.bukkit.entity import Strider
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import EntityEvent
from typing import Any

class StriderTemperatureChangeEvent(EntityEvent, Cancellable):
    """
    Called when a {@link Strider}'s temperature has changed as a result of
    entering or exiting blocks it considers warm.
    """

    handlers: HandlerList

    def __init__(self, what: Strider, shivering: bool) -> None:
        """
        Initialize the StriderTemperatureChangeEvent.

        :param what: The Strider involved in the event.
        :param shivering: The new shivering state of the Strider.
        """
        ...

    def getEntity(self) -> Strider:
        """
        Get the Strider involved in the event.

        :return: The Strider.
        """
        ...

    def isShivering(self) -> bool:
        """
        Get the Strider's new shivering state.

        :return: The new shivering state.
        """
        ...

    def isCancelled(self) -> bool:
        """
        Check if the event is cancelled.

        :return: True if the event is cancelled, otherwise False.
        """
        ...

    def setCancelled(self, cancelled: bool) -> None:
        """
        Set the cancellation state of the event.

        :param cancelled: True to cancel the event, otherwise False.
        """
        ...

    def getHandlers(self) -> HandlerList:
        """
        Get the handler list for the event.

        :return: The handler list.
        """
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        """
        Get the static handler list for the event.

        :return: The static handler list.
        """
        ...
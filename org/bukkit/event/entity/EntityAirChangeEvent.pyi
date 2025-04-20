from org.bukkit.entity import Entity
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.event.entity import EntityEvent
from typing import Any

class EntityAirChangeEvent(EntityEvent, Cancellable):
    """
    Called when the amount of air an entity has remaining changes.
    """

    handlers: HandlerList = HandlerList()
    amount: int
    cancelled: bool

    def __init__(self, what: Entity, amount: int) -> None:
        """
        Initializes the EntityAirChangeEvent with the specified entity and amount of air.

        :param what: The entity that is changing air.
        :param amount: The amount of air remaining.
        """
        ...

    def getAmount(self) -> int:
        """
        Gets the amount of air the entity has left (measured in ticks).

        :return: amount of air remaining
        """
        ...

    def setAmount(self, amount: int) -> None:
        """
        Sets the amount of air remaining for the entity (measured in ticks).

        :param amount: amount of air remaining
        """
        ...

    def isCancelled(self) -> bool:
        """
        Checks if the event is cancelled.

        :return: True if the event is cancelled, False otherwise.
        """
        ...

    def setCancelled(self, cancelled: bool) -> None:
        """
        Sets the cancelled state of the event.

        :param cancelled: True to cancel the event, False to allow it.
        """
        ...

    def getHandlers(self) -> HandlerList:
        """
        Gets the handler list for this event.

        :return: the handler list
        """
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        """
        Gets the static handler list for this event.

        :return: the static handler list
        """
        ...
from org.bukkit.entity import Entity
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.event.entity import EntityEvent
from typing import Literal

class EntityCombustEvent(EntityEvent, Cancellable):
    """
    Called when an entity combusts.
    <p>
    If an Entity Combust event is cancelled, the entity will not combust.
    """
    
    handlers: HandlerList = HandlerList()
    duration: float
    cancel: bool

    def __init__(self, combustee: Entity, duration: float) -> None:
        """
        Initializes the EntityCombustEvent with the combustee and duration.

        :param combustee: The entity that is combusting.
        :param duration: The duration for which the entity should be alight.
        """
        ...

    @Deprecated(since="1.21")
    def __init__(self, combustee: Entity, duration: int) -> None:
        """
        Initializes the EntityCombustEvent with the combustee and duration.

        :param combustee: The entity that is combusting.
        :param duration: The duration for which the entity should be alight.
        """
        ...

    def isCancelled(self) -> bool:
        """
        Returns whether the event is cancelled.

        :return: True if the event is cancelled, False otherwise.
        """
        ...

    def setCancelled(self, cancel: bool) -> None:
        """
        Sets the cancellation state of the event.

        :param cancel: True to cancel the event, False otherwise.
        """
        ...

    def getDuration(self) -> float:
        """
        Returns the amount of time (in seconds) the combustee should be alight for.

        :return: The duration in seconds.
        """
        ...

    def setDuration(self, duration: float) -> None:
        """
        Sets the duration for which the combustee should be alight.

        :param duration: The time in seconds to be alight for.
        """
        ...

    @Deprecated(since="1.21", forRemoval=True)
    def setDuration(self, duration: int) -> None:
        """
        Sets the duration for which the combustee should be alight.

        :param duration: The time in seconds to be alight for.
        @see #setDuration(float)
        """
        ...

    def getHandlers(self) -> HandlerList:
        """
        Returns the handler list for this event.

        :return: The handler list.
        """
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        """
        Returns the static handler list for this event.

        :return: The static handler list.
        """
        ...
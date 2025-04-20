from org.bukkit.entity import Sheep
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.event.entity import EntityEvent
from typing import Any

class SheepRegrowWoolEvent(EntityEvent, Cancellable):
    """
    Called when a sheep regrows its wool
    """

    handlers: HandlerList = HandlerList()
    cancel: bool

    def __init__(self, sheep: Sheep) -> None:
        """
        :param sheep: The sheep that regrows its wool
        """
        ...

    def isCancelled(self) -> bool:
        """
        :return: True if the event is cancelled, False otherwise
        """
        ...

    def setCancelled(self, cancel: bool) -> None:
        """
        :param cancel: True to cancel the event, False to allow it
        """
        ...

    def getEntity(self) -> Sheep:
        """
        :return: The sheep associated with this event
        """
        ...

    def getHandlers(self) -> HandlerList:
        """
        :return: The handler list for this event
        """
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        """
        :return: The static handler list for this event
        """
        ...
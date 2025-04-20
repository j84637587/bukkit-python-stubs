from org.bukkit.entity import Slime
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.event.entity import EntityEvent
from typing import Any

class SlimeSplitEvent(EntityEvent, Cancellable):
    """
    Called when a Slime splits into smaller Slimes upon death
    """

    handlers: HandlerList = HandlerList()
    cancel: bool
    count: int

    def __init__(self, slime: Slime, count: int) -> None:
        """
        Initializes the SlimeSplitEvent.

        :param slime: The Slime that is splitting.
        :param count: The number of smaller slimes to spawn.
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
        Sets whether the event is cancelled.

        :param cancel: True to cancel the event, False otherwise.
        """
        ...

    def getEntity(self) -> Slime:
        """
        Gets the Slime that is splitting.

        :return: The Slime entity.
        """
        ...

    def getCount(self) -> int:
        """
        Gets the amount of smaller slimes to spawn.

        :return: The amount of slimes to spawn.
        """
        ...

    def setCount(self, count: int) -> None:
        """
        Sets how many smaller slimes will spawn on the split.

        :param count: The amount of slimes to spawn.
        """
        ...

    def getHandlers(self) -> HandlerList:
        """
        Gets the handler list for this event.

        :return: The handler list.
        """
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        """
        Gets the static handler list for this event.

        :return: The static handler list.
        """
        ...
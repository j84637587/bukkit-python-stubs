from org.bukkit import World
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.event.weather import WeatherEvent
from typing import Literal

class ThunderChangeEvent(WeatherEvent, Cancellable):
    """
    Stores data for thunder state changing in a world
    """
    handlers: HandlerList = HandlerList()
    canceled: bool
    to: bool

    def __init__(self, world: World, to: bool) -> None:
        """
        Initializes a ThunderChangeEvent.

        :param world: The world where the thunder state is changing.
        :param to: The state to which the thunder is changing.
        """
        ...

    def isCancelled(self) -> bool:
        """
        Checks if the event is cancelled.

        :return: True if the event is cancelled, false otherwise.
        """
        ...

    def setCancelled(self, cancel: bool) -> None:
        """
        Sets the cancellation state of the event.

        :param cancel: True to cancel the event, false otherwise.
        """
        ...

    def toThunderState(self) -> bool:
        """
        Gets the state of thunder that the world is being set to.

        :return: True if the weather is being set to thundering, false otherwise.
        """
        ...

    def getHandlers(self) -> HandlerList:
        """
        Gets the handlers for this event.

        :return: The handler list for this event.
        """
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        """
        Gets the static handler list for this event.

        :return: The static handler list for this event.
        """
        ...
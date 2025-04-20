from org.bukkit.World import World
from org.bukkit.entity.LightningStrike import LightningStrike
from org.bukkit.event.Cancellable import Cancellable
from org.bukkit.event.HandlerList import HandlerList
from typing import Literal, Final

class LightningStrikeEvent(WeatherEvent, Cancellable):
    handlers: Final[HandlerList]
    canceled: bool
    bolt: LightningStrike
    cause: 'LightningStrikeEvent.Cause'

    def __init__(self, world: World, bolt: LightningStrike, cause: 'LightningStrikeEvent.Cause') -> None:
        """
        Initializes a LightningStrikeEvent.

        :param world: The world where the lightning strike occurs.
        :param bolt: The lightning strike entity.
        :param cause: The cause of the lightning strike.
        """
        ...

    @classmethod
    def getHandlerList(cls) -> HandlerList:
        """
        Gets the handler list for this event.

        :return: The handler list.
        """
        ...

    def isCancelled(self) -> bool:
        """
        Checks if the event is cancelled.

        :return: True if the event is cancelled, False otherwise.
        """
        ...

    def setCancelled(self, cancel: bool) -> None:
        """
        Sets the cancellation state of the event.

        :param cancel: True to cancel the event, False to allow it.
        """
        ...

    def getLightning(self) -> LightningStrike:
        """
        Gets the bolt which is striking the earth.

        :return: lightning entity.
        """
        ...

    def getCause(self) -> 'LightningStrikeEvent.Cause':
        """
        Gets the cause of this lightning strike.

        :return: strike cause.
        """
        ...

    def getHandlers(self) -> HandlerList:
        """
        Gets the handler list for this event.

        :return: The handler list.
        """
        ...

    class Cause:
        """
        Enum for the cause of the lightning strike.
        """
        COMMAND: Literal['COMMAND']
        CUSTOM: Literal['CUSTOM']
        SPAWNER: Literal['SPAWNER']
        TRIDENT: Literal['TRIDENT']
        TRAP: Literal['TRAP']
        WEATHER: Literal['WEATHER']
        ENCHANTMENT: Literal['ENCHANTMENT']
        UNKNOWN: Literal['UNKNOWN']
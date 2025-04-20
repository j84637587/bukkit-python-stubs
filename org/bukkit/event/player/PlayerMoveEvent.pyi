from typing import Optional
from org.bukkit.Location import Location
from org.bukkit.entity.Player import Player
from org.bukkit.event.Cancellable import Cancellable
from org.bukkit.event.HandlerList import HandlerList
from google.common.base import Preconditions
from org.jetbrains.annotations import NotNull, Nullable

class PlayerMoveEvent(PlayerEvent, Cancellable):
    """
    Holds information for player movement events
    """

    handlers: HandlerList = HandlerList()
    cancel: bool
    from: Location
    to: Optional[Location]

    def __init__(self, player: Player, from: Location, to: Optional[Location]) -> None:
        """
        Initializes a new PlayerMoveEvent.

        :param player: The player involved in the event.
        :param from: The location the player moved from.
        :param to: The location the player moved to.
        """
        ...

    def isCancelled(self) -> bool:
        """
        Gets the cancellation state of this event. A cancelled event will not
        be executed in the server, but will still pass to other plugins.
        If a move or teleport event is cancelled, the player will be moved or
        teleported back to the Location as defined by getFrom(). This will not
        fire an event.

        :return: true if this event is cancelled.
        """
        ...

    def setCancelled(self, cancel: bool) -> None:
        """
        Sets the cancellation state of this event. A cancelled event will not
        be executed in the server, but will still pass to other plugins.
        If a move or teleport event is cancelled, the player will be moved or
        teleported back to the Location as defined by getFrom(). This will not
        fire an event.

        :param cancel: true if you wish to cancel this event.
        """
        ...

        def getFrom(self) -> Location:
        """
        Gets the location this player moved from.

        :return: Location the player moved from.
        """
        ...

    def setFrom(self, from: Location) -> None:
        """
        Sets the location to mark as where the player moved from.

        :param from: New location to mark as the player's previous location.
        """
        ...

        def getTo(self) -> Optional[Location]:
        """
        Gets the location this player moved to.

        :return: Location the player moved to.
        """
        ...

    def setTo(self, to: Location) -> None:
        """
        Sets the location that this player will move to.

        :param to: New Location this player will move to.
        """
        ...

    def validateLocation(self, loc: Location) -> None:
        """
        Validates the given location.

        :param loc: The location to validate.
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
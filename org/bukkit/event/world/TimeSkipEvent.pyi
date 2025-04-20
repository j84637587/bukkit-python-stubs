from org.bukkit import World
from org.bukkit.event import Cancellable, HandlerList
from org.jetbrains.annotations import NotNull

class TimeSkipEvent(WorldEvent, Cancellable):
    """
    Called when the time skips in a world.
    <p>
    If the event is cancelled the time will not change.
    """

    handlers: HandlerList = HandlerList()
    cancelled: bool
    skipReason: 'SkipReason'
    skipAmount: int

    def __init__(self, world: World, skipReason: 'SkipReason', skipAmount: int) -> None:
        ...

        def getSkipReason(self) -> 'SkipReason':
        """
        Gets the reason why the time has skipped.

        @return a SkipReason value detailing why the time has skipped
        """
        ...

    def getSkipAmount(self) -> int:
        """
        Gets the amount of time that was skipped.

        @return Amount of time skipped
        """
        ...

    def setSkipAmount(self, skipAmount: int) -> None:
        """
        Sets the amount of time to skip.

        @param skipAmount Amount of time to skip
        """
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...

        def getHandlers(self) -> HandlerList:
        ...

        @staticmethod
    def getHandlerList() -> HandlerList:
        ...

class SkipReason:
    """
    An enum specifying the reason the time skipped.
    """
    COMMAND = ...
    CUSTOM = ...
    NIGHT_SKIP = ...
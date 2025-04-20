from typing import Any
from org.bukkit import Raid, World
from org.bukkit.event import HandlerList
from org.jetbrains.annotations import NotNull

class RaidStopEvent(RaidEvent):
    """
    Called when a {@link Raid} is stopped.
    """

    handlers: HandlerList = HandlerList()
    reason: 'Reason'

    def __init__(self, raid: Raid, world: World, reason: 'Reason') -> None:
        super().__init__(raid, world)
        self.reason = reason

        def getReason(self) -> 'Reason':
        """
        Returns the stop reason.

        @return Reason
        """
        ...

        def getHandlers(self) -> HandlerList:
        ...

        @staticmethod
    def getHandlerList() -> HandlerList:
        ...

    class Reason:
        """
        Enum for the reasons a raid can be stopped.
        """
        PEACE = ...
        TIMEOUT = ...
        FINISHED = ...
        UNSPAWNABLE = ...
        NOT_IN_VILLAGE = ...
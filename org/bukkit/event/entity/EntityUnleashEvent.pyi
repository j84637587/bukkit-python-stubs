from typing import Any
from org.bukkit.entity import Entity
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import EntityEvent
from org.jetbrains.annotations import NotNull

class EntityUnleashEvent(EntityEvent):
    """
    Called immediately prior to an entity being unleashed.
    """

    handlers: HandlerList = HandlerList()
    reason: 'EntityUnleashEvent.UnleashReason'

    def __init__(self, entity: Entity, reason: 'EntityUnleashEvent.UnleashReason') -> None:
        super().__init__(entity)
        self.reason = reason

        def getReason(self) -> 'EntityUnleashEvent.UnleashReason':
        """
        Returns the reason for the unleashing.

        @return The reason
        """
        ...

        def getHandlers(self) -> HandlerList:
        ...

        @staticmethod
    def getHandlerList() -> HandlerList:
        ...

    class UnleashReason:
        """
        Enum for the reasons an entity can be unleashed.
        """
        HOLDER_GONE = ...
        PLAYER_UNLEASH = ...
        DISTANCE = ...
        UNKNOWN = ...
from org.bukkit.entity import LivingEntity
from org.bukkit.event import Cancellable, HandlerList
from org.jetbrains.annotations import NotNull

class EntityToggleSwimEvent(EntityEvent, Cancellable):
    """
    Sent when an entity's swimming status is toggled.
    """

    handlers: HandlerList = HandlerList()

    def __init__(self, who: NotNull[LivingEntity], isSwimming: bool) -> None:
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...

    """
    Returns true if the entity is now swims or
    false if the entity stops swimming.

    @return new swimming state
    """
    def isSwimming(self) -> bool:
        ...

        def getHandlers(self) -> HandlerList:
        ...

        @staticmethod
    def getHandlerList() -> HandlerList:
        ...
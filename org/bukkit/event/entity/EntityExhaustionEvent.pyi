from org.bukkit.entity import HumanEntity
from org.bukkit.event import Cancellable, HandlerList
from org.jetbrains.annotations import NotNull

class EntityExhaustionEvent(EntityEvent, Cancellable):
    """
    Called when a human entity experiences exhaustion.

    An exhaustion level greater than 4.0 causes a decrease in saturation by 1.
    """

    handlers: HandlerList = ...
    exhaustionReason: 'ExhaustionReason'
    exhaustion: float
    cancel: bool

    def __init__(self, who: NotNull[HumanEntity], exhaustionReason: NotNull['ExhaustionReason'], exhaustion: float) -> None:
        ...

        def getExhaustionReason(self) -> 'ExhaustionReason':
        ...

    def getExhaustion(self) -> float:
        ...

    def setExhaustion(self, exhaustion: float) -> None:
        ...

        def getEntity(self) -> NotNull[HumanEntity]:
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...

    class ExhaustionReason:
        """
        The reason for why a PlayerExhaustionEvent takes place
        """
        BLOCK_MINED = ...
        HUNGER_EFFECT = ...
        DAMAGED = ...
        ATTACK = ...
        JUMP_SPRINT = ...
        JUMP = ...
        SWIM = ...
        WALK_UNDERWATER = ...
        WALK_ON_WATER = ...
        SPRINT = ...
        CROUCH = ...
        WALK = ...
        REGEN = ...
        UNKNOWN = ...

        def getHandlers(self) -> HandlerList:
        ...

        @staticmethod
    def getHandlerList() -> HandlerList:
        ...
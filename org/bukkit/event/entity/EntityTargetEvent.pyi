from org.bukkit.entity import Entity
from org.bukkit.event import Cancellable, HandlerList
from org.jetbrains.annotations import NotNull, Nullable

"""
Called when a creature targets or untargets another entity
"""
class EntityTargetEvent(EntityEvent, Cancellable):
    handlers: HandlerList = HandlerList()
    cancel: bool
    target: Entity
    reason: 'TargetReason'

    def __init__(self, entity: Entity, target: Nullable[Entity], reason: TargetReason) -> None:
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...

    """
    Returns the reason for the targeting

    @return The reason
    """
        def getReason(self) -> TargetReason:
        ...

    """
    Get the entity that this is targeting.
    <p>
    This will be null in the case that the event is called when the mob
    forgets its target.

    @return The entity
    """
        def getTarget(self) -> Nullable[Entity]:
        ...

    """
    Set the entity that you want the mob to target instead.
    <p>
    It is possible to be null, null will cause the entity to be
    target-less.
    <p>
    This is different from cancelling the event. Cancelling the event will
    cause the entity to keep an original target, while setting to be null
    will cause the entity to be reset.

    @param target The entity to target
    """
    def setTarget(self, target: Nullable[Entity]) -> None:
        ...

        def getHandlers(self) -> HandlerList:
        ...

        @staticmethod
    def getHandlerList() -> HandlerList:
        ...

    """
    An enum to specify the reason for the targeting
    """
    class TargetReason:
        TARGET_DIED = ...
        CLOSEST_PLAYER = ...
        TARGET_ATTACKED_ENTITY = ...
        PIG_ZOMBIE_TARGET = ...
        FORGOT_TARGET = ...
        TARGET_ATTACKED_OWNER = ...
        OWNER_ATTACKED_TARGET = ...
        RANDOM_TARGET = ...
        DEFEND_VILLAGE = ...
        TARGET_ATTACKED_NEARBY_ENTITY = ...
        REINFORCEMENT_TARGET = ...
        COLLISION = ...
        CUSTOM = ...
        CLOSEST_ENTITY = ...
        FOLLOW_LEADER = ...
        TEMPT = ...
        UNKNOWN = ...
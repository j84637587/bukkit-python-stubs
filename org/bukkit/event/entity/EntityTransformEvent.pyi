from typing import List
from org.bukkit.entity import Entity
from org.bukkit.event import Cancellable, HandlerList
from org.jetbrains.annotations import NotNull

"""
Called when an entity is about to be replaced by another entity.
"""
class EntityTransformEvent(EntityEvent, Cancellable):
    handlers: HandlerList

    def __init__(self, original: Entity, converted_list: List[Entity], transform_reason: 'TransformReason') -> None:
        ...

    """
    Gets the entity that the original entity was transformed to.

    This returns the first entity in the transformed entity list.

    @return The transformed entity.
    @see #getTransformedEntities()
    """
        def get_transformed_entity(self) -> Entity:
        ...

    """
    Gets the entities that the original entity was transformed to.

    @return The transformed entities.
    """
        def get_transformed_entities(self) -> List[Entity]:
        ...

    """
    Gets the reason for the conversion that has occurred.

    @return The reason for conversion that has occurred.
    """
        def get_transform_reason(self) -> 'TransformReason':
        ...

    def is_cancelled(self) -> bool:
        ...

    def set_cancelled(self, cancel: bool) -> None:
        ...

        def get_handlers(self) -> HandlerList:
        ...

        @staticmethod
    def get_handler_list() -> HandlerList:
        ...

    class TransformReason:
        """
        When a zombie gets cured and a villager is spawned.
        """
        CURED = ...

        """
        When an entity is shaking in Powder Snow and a new entity spawns.
        """
        FROZEN = ...

        """
        When a villager gets infected and a zombie villager spawns.
        """
        INFECTION = ...

        """
        When an entity drowns in water and a new entity spawns.
        """
        DROWNED = ...

        """
        When a mooshroom (or MUSHROOM_COW) is sheared and a cow spawns.
        """
        SHEARED = ...

        """
        When lightning strikes a entity.
        """
        LIGHTNING = ...

        """
        When a slime splits into multiple smaller slimes.
        """
        SPLIT = ...

        """
        When a piglin (or hoglin) converts to a zombified version from overworld presence.
        """
        PIGLIN_ZOMBIFIED = ...

        """
        When a tadpole converts to a frog
        """
        METAMORPHOSIS = ...

        """
        When reason is unknown.
        """
        UNKNOWN = ...
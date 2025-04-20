from org.bukkit.entity import Entity
from org.bukkit.entity import LivingEntity
from org.bukkit.util import Vector
from org.jetbrains.annotations import NotNull
from org.bukkit.event.entity import EntityKnockbackEvent
from typing import Literal

class EntityKnockbackByEntityEvent(EntityKnockbackEvent):
    """
    Called when an entity receives knockback from another entity.
    """

    def __init__(self, entity: LivingEntity, source: Entity, cause: Literal['KnockbackCause'], force: float, raw_knockback: Vector, knockback: Vector) -> None:
        ...

        def get_source_entity(self) -> Entity:
        """
        Get the entity that has caused knockback to the defender.

        :return: entity that caused knockback
        """
        ...
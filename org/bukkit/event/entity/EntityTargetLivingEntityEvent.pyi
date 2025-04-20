from org.bukkit.entity import Entity
from org.bukkit.entity import LivingEntity
from org.bukkit.event.entity import EntityTargetEvent
from typing import Optional

class EntityTargetLivingEntityEvent(EntityTargetEvent):
    """
    Called when an Entity targets a {@link LivingEntity} and can only target
    LivingEntity's.
    """

    def __init__(self, entity: Entity, target: Optional[LivingEntity], reason: Optional['TargetReason']) -> None:
        ...

    def get_target(self) -> Optional[LivingEntity]:
        ...

    def set_target(self, target: Optional[Entity]) -> None:
        ...
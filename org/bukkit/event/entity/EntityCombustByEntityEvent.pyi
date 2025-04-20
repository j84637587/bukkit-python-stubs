from org.bukkit.entity import Entity
from typing import Optional

class EntityCombustEvent:
    pass

class EntityCombustByEntityEvent(EntityCombustEvent):
    """
    Called when an entity causes another entity to combust.
    """
    def __init__(self, combuster: Entity, combustee: Entity, duration: float) -> None:
        ...

    @classmethod
    def deprecated_init(cls, combuster: Entity, combustee: Entity, duration: int) -> None:
        ...

    def get_combuster(self) -> Entity:
        """
        Get the entity that caused the combustion event.

        :return: the Entity that set the combustee alight.
        """
        ...
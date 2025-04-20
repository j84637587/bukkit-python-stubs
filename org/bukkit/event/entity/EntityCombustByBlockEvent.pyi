from org.bukkit.block import Block
from org.bukkit.entity import Entity
from typing import Optional

class EntityCombustEvent:
    """Base class for entity combustion events."""
    def __init__(self, combustee: Entity, duration: float) -> None:
        ...

class EntityCombustByBlockEvent(EntityCombustEvent):
    """
    Called when a block causes an entity to combust.
    """
    def __init__(self, combuster: Optional[Block], combustee: Entity, duration: float) -> None:
        ...

    @Deprecated(since="1.21")
    def __init__(self, combuster: Optional[Block], combustee: Entity, duration: int) -> None:
        ...

    """
    The combuster can be lava or a block that is on fire.
    WARNING: block may be null.

    @return: the Block that set the combustee alight.
    """
    def get_combuster(self) -> Optional[Block]:
        ...
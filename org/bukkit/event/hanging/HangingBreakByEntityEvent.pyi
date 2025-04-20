from org.bukkit.entity import Entity
from org.bukkit.entity import Hanging
from org.bukkit.event.hanging import HangingBreakEvent
from typing import Optional

class HangingBreakByEntityEvent(HangingBreakEvent):
    """
    Triggered when a hanging entity is removed by an entity
    """

    def __init__(self, hanging: Hanging, remover: Optional[Entity] = None) -> None:
        ...

    def __init__(self, hanging: Hanging, remover: Optional[Entity], cause: HangingBreakEvent.RemoveCause) -> None:
        ...

    """
    Gets the entity that removed the hanging entity.
    May be null, for example when broken by an explosion.

    @return: the entity that removed the hanging entity
    """
    def get_remover(self) -> Optional[Entity]:
        ...
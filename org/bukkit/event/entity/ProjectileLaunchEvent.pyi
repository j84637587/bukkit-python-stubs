from org.bukkit.entity import Entity
from org.bukkit.entity import Projectile
from org.bukkit.event import Cancellable
from org.bukkit.event.entity import EntitySpawnEvent
from typing import Any

class ProjectileLaunchEvent(EntitySpawnEvent, Cancellable):
    """
    Called when a projectile is launched.
    """

    def __init__(self, what: Entity) -> None:
        ...

    def is_cancelled(self) -> bool:
        ...

    def set_cancelled(self, cancel: bool) -> None:
        ...

    def get_entity(self) -> Projectile:
        ...
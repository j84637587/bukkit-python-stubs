from org.bukkit.block import Block
from org.bukkit.block import BlockFace
from org.bukkit.entity import AreaEffectCloud
from org.bukkit.entity import Entity
from org.bukkit.entity import ThrownPotion
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import ProjectileHitEvent
from typing import Optional

class LingeringPotionSplashEvent(ProjectileHitEvent, Cancellable):
    """
    Called when a splash potion hits an area
    """
    handlers: HandlerList

    def __init__(self, potion: ThrownPotion, entity: AreaEffectCloud) -> None:
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        ...

    def __init__(self, potion: ThrownPotion, hitEntity: Optional[Entity], hitBlock: Optional[Block], hitFace: Optional[BlockFace], entity: AreaEffectCloud) -> None:
        ...

    def getEntity(self) -> ThrownPotion:
        ...

    def getAreaEffectCloud(self) -> AreaEffectCloud:
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...

    def getHandlers(self) -> HandlerList:
        ...
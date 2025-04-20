from typing import Collection, Dict
from org.bukkit.block import Block
from org.bukkit.block import BlockFace
from org.bukkit.entity import Entity
from org.bukkit.entity import LivingEntity
from org.bukkit.entity import ThrownPotion
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import ProjectileHitEvent
from google.common.base import Preconditions
from typing import Optional

class PotionSplashEvent(ProjectileHitEvent, Cancellable):
    """
    Called when a splash potion hits an area
    """
    
    handlers: HandlerList
    cancelled: bool
    affectedEntities: Dict[LivingEntity, float]

    def __init__(self, potion: ThrownPotion, affectedEntities: Dict[LivingEntity, float]) -> None:
        """
        @deprecated since = "1.20.2"
        """
        ...

    def __init__(self, potion: ThrownPotion, hitEntity: Optional[Entity], hitBlock: Optional[Block], hitFace: Optional[BlockFace], affectedEntities: Dict[LivingEntity, float]) -> None:
        ...

    def getEntity(self) -> ThrownPotion:
        """
        @return The thrown potion entity
        """
        ...

    def getPotion(self) -> ThrownPotion:
        """
        Gets the potion which caused this event

        @return The thrown potion entity
        """
        ...

    def getAffectedEntities(self) -> Collection[LivingEntity]:
        """
        Retrieves a list of all effected entities

        @return A fresh copy of the affected entity list
        """
        ...

    def getIntensity(self, entity: LivingEntity) -> float:
        """
        Gets the intensity of the potion's effects for given entity; This
        depends on the distance to the impact center

        @param entity Which entity to get intensity for
        @return intensity relative to maximum effect; 0.0: not affected; 1.0:
            fully hit by potion effects
        """
        ...

    def setIntensity(self, entity: LivingEntity, intensity: float) -> None:
        """
        Overwrites the intensity for a given entity

        @param entity For which entity to define a new intensity
        @param intensity relative to maximum effect
        """
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...

    def getHandlers(self) -> HandlerList:
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        ...
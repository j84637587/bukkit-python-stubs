from org.bukkit.entity import LivingEntity
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.inventory import EquipmentSlot
from typing import Optional

class EntityResurrectEvent(EntityEvent, Cancellable):
    """
    Called when an entity dies and may have the opportunity to be resurrected.
    Will be called in a cancelled state if the entity does not have a totem
    equipped.
    """

    handlers: HandlerList

    def __init__(self, what: LivingEntity, hand: Optional[EquipmentSlot] = None) -> None:
        ...

    @classmethod
    def getHandlerList(cls) -> HandlerList:
        ...

    @Deprecated(since="1.19.2")
    def __init__(self, what: LivingEntity) -> None:
        ...

    def getEntity(self) -> LivingEntity:
        ...

    """
    Get the hand in which the totem of undying was found, or null if the
    entity did not have a totem of undying.

    @return the hand, or null
    """
    def getHand(self) -> Optional[EquipmentSlot]:
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancelled: bool) -> None:
        ...

    def getHandlers(self) -> HandlerList:
        ...
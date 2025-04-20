from typing import List
from org.bukkit.entity import AreaEffectCloud, LivingEntity
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.event.entity import EntityEvent
from org.jetbrains.annotations import NotNull

class AreaEffectCloudApplyEvent(EntityEvent, Cancellable):
    """
    Called when a lingering potion applies its effects. Happens
    once every 5 ticks
    """

    handlers: HandlerList = HandlerList()
    affectedEntities: List[LivingEntity]
    cancelled: bool = False

    def __init__(self, entity: NotNull[AreaEffectCloud], affectedEntities: NotNull[List[LivingEntity]]) -> None:
        super().__init__(entity)
        self.affectedEntities = affectedEntities

    def isCancelled(self) -> bool:
        return self.cancelled

    def setCancelled(self, cancel: bool) -> None:
        self.cancelled = cancel

        def getEntity(self) -> AreaEffectCloud:
        return super().getEntity()  # type: ignore

    """
    Retrieves a mutable list of the effected entities
    <p>
    It is important to note that not every entity in this list
    is guaranteed to be effected. The cloud may die during the
    application of its effects due to the depletion of {@link AreaEffectCloud#getDurationOnUse()}
    or {@link AreaEffectCloud#getRadiusOnUse()}

    @return: the affected entity list
    """
        def getAffectedEntities(self) -> List[LivingEntity]:
        return self.affectedEntities

        def getHandlers(self) -> HandlerList:
        return self.handlers

        @staticmethod
    def getHandlerList() -> HandlerList:
        return AreaEffectCloudApplyEvent.handlers
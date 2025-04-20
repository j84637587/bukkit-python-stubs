from typing import List
from org.bukkit.PortalType import PortalType
from org.bukkit.block.BlockState import BlockState
from org.bukkit.entity.LivingEntity import LivingEntity
from org.bukkit.event.Cancellable import Cancellable
from org.bukkit.event.HandlerList import HandlerList
from org.bukkit.event.entity.EntityEvent import EntityEvent
from org.jetbrains.annotations import NotNull

"""
Thrown when a Living Entity creates a portal in a world.

@deprecated Use {@link PortalCreateEvent}
"""
class EntityCreatePortalEvent(EntityEvent, Cancellable):
    handlers: HandlerList

    def __init__(self, what: LivingEntity, blocks: List[BlockState], type: PortalType) -> None:
        ...

        def getEntity(self) -> LivingEntity:
        ...

    """
    Gets a list of all blocks associated with the portal.

    @return List of blocks that will be changed.
    """
        def getBlocks(self) -> List[BlockState]:
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...

    """
    Gets the type of portal that is trying to be created.

    @return Type of portal.
    """
        def getPortalType(self) -> PortalType:
        ...

        def getHandlers(self) -> HandlerList:
        ...

        @staticmethod
    def getHandlerList() -> HandlerList:
        ...
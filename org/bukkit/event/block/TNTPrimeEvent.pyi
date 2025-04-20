from org.bukkit.block import Block
from org.bukkit.entity import Entity
from org.bukkit.event import Cancellable, HandlerList
from typing import Optional

"""
Called when a block of TNT in the world become primed.
If a TNT Prime event is cancelled, the block of TNT will not become primed.
"""
class TNTPrimeEvent(BlockEvent, Cancellable):
    handlers: HandlerList

    def __init__(self, block: Block, ignite_cause: 'TNTPrimeEvent.PrimeCause', priming_entity: Optional[Entity], priming_block: Optional[Block]) -> None:
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...

    """
    Get the cause of the TNT becoming primed.
    
    @return: the cause
    """
    def getCause(self) -> 'TNTPrimeEvent.PrimeCause':
        ...

    """
    Get the entity that caused the TNT to be primed.
    
    @return: the entity that caused the TNT to be primed, or None if it was
    not caused by an entity.
    """
    def getPrimingEntity(self) -> Optional[Entity]:
        ...

    """
    Get the block that caused the TNT to be primed.
    
    @return: the block that caused the TNT to be primed, or None if it was not
    caused by a block.
    """
    def getPrimingBlock(self) -> Optional[Block]:
        ...

    def getHandlers(self) -> HandlerList:
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        ...

    """
    An enum to represent the cause of a TNT block becoming primed.
    """
    class PrimeCause:
        FIRE = ...
        REDSTONE = ...
        PLAYER = ...
        EXPLOSION = ...
        PROJECTILE = ...
        BLOCK_BREAK = ...
        DISPENSER = ...
from org.bukkit.GameEvent import GameEvent
from org.bukkit.block.Block import Block
from org.bukkit.entity.Entity import Entity
from org.bukkit.event.Cancellable import Cancellable
from org.bukkit.event.HandlerList import HandlerList
from typing import Optional

class BlockReceiveGameEvent(BlockEvent, Cancellable):
    """
    Called when a Sculk sensor receives a game event and hence might activate.

    Will be called cancelled if the block's default behavior is to ignore the
    event.
    """

    handlers: HandlerList = ...
    event: GameEvent
    entity: Optional[Entity]
    cancelled: bool

    def __init__(self, event: GameEvent, block: Block, entity: Optional[Entity]) -> None:
        ...

    """
    Get the underlying event.

    @return the event
    """
    def get_event(self) -> GameEvent:
        ...

    """
    Get the entity which triggered this event, if present.

    @return triggering entity or null
    """
    def get_entity(self) -> Optional[Entity]:
        ...

    def set_cancelled(self, cancel: bool) -> None:
        ...

    def is_cancelled(self) -> bool:
        ...

    def get_handlers(self) -> HandlerList:
        ...

    @staticmethod
    def get_handler_list() -> HandlerList:
        ...
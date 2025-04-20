from org.bukkit.block import Block
from org.bukkit.block import BlockFace
from org.bukkit.entity import Entity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.block import BlockEvent
from typing import Optional

class BellRingEvent(BlockEvent, Cancellable):
    """
    Called when a bell is being rung.
    """

    handlers: HandlerList

    def __init__(self, the_block: Block, direction: BlockFace, entity: Optional[Entity]) -> None:
        ...

    def get_direction(self) -> BlockFace:
        """
        Get the direction in which the bell was rung.

        :return: the direction
        """
        ...

    def get_entity(self) -> Optional[Entity]:
        """
        Get the {@link Entity} that rang the bell (if there was one).

        :return: the entity
        """
        ...

    def set_cancelled(self, cancelled: bool) -> None:
        ...

    def is_cancelled(self) -> bool:
        ...

    def get_handlers(self) -> HandlerList:
        ...

    @staticmethod
    def get_handler_list() -> HandlerList:
        ...
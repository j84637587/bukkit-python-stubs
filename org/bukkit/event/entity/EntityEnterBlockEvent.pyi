from org.bukkit.block import Block
from org.bukkit.entity import Entity
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.event.entity import EntityEvent
from typing import Any

class EntityEnterBlockEvent(EntityEvent, Cancellable):
    """
    Called when an `Entity` enters a block and is stored in that block.
    This event is called for bees entering a bee hive.
    It is not called when a silverfish "enters" a stone block. For that listen to
    the `EntityChangeBlockEvent`.
    """

    handlers: HandlerList

    def __init__(self, entity: Entity, block: Block) -> None:
        """
        Initialize the event with the given entity and block.

        :param entity: The entity that is entering the block.
        :param block: The block that the entity will enter.
        """
        ...

    def get_block(self) -> Block:
        """
        Get the block the entity will enter.

        :return: the block
        """
        ...

    def is_cancelled(self) -> bool:
        """
        Check if the event is cancelled.

        :return: True if the event is cancelled, False otherwise.
        """
        ...

    def set_cancelled(self, cancel: bool) -> None:
        """
        Set whether the event is cancelled.

        :param cancel: True to cancel the event, False to allow it.
        """
        ...

    def get_handlers(self) -> HandlerList:
        """
        Get the handler list for this event.

        :return: the handler list
        """
        ...

    @staticmethod
    def get_handler_list() -> HandlerList:
        """
        Get the static handler list for this event.

        :return: the static handler list
        """
        ...
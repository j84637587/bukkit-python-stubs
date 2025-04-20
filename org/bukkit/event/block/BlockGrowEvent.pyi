from org.bukkit.block import Block
from org.bukkit.block import BlockState
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.block import BlockEvent
from typing import Any

class BlockGrowEvent(BlockEvent, Cancellable):
    """
    Called when a block grows naturally in the world.
    <p>
    Examples:
    <ul>
    <li>Wheat
    <li>Sugar Cane
    <li>Cactus
    <li>Watermelon
    <li>Pumpkin
    <li>Turtle Egg
    </ul>
    <p>
    If a Block Grow event is cancelled, the block will not grow.
    """

    handlers: HandlerList

    def __init__(self, block: Block, new_state: BlockState) -> None:
        """
        Initializes a BlockGrowEvent.

        :param block: The block that is growing.
        :param new_state: The new state of the block.
        """
        ...

    def get_new_state(self) -> BlockState:
        """
        Gets the state of the block where it will form or spread to.

        :return: The block state for this events block
        """
        ...

    def is_cancelled(self) -> bool:
        """
        Checks if the event is cancelled.

        :return: True if the event is cancelled, otherwise False.
        """
        ...

    def set_cancelled(self, cancel: bool) -> None:
        """
        Sets the cancellation state of the event.

        :param cancel: True to cancel the event, otherwise False.
        """
        ...

    def get_handlers(self) -> HandlerList:
        """
        Gets the handler list for this event.

        :return: The handler list for this event.
        """
        ...

    @staticmethod
    def get_handler_list() -> HandlerList:
        """
        Gets the static handler list for this event.

        :return: The static handler list for this event.
        """
        ...
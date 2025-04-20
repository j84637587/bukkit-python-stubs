from org.bukkit.block import Block
from org.bukkit.block import BlockState
from org.bukkit.event import HandlerList
from org.bukkit.event.block import BlockFormEvent
from typing import Any

class BlockSpreadEvent(BlockFormEvent):
    """
    Called when a block spreads based on world conditions.
    <p>
    Use {@link BlockFormEvent} to catch blocks that "randomly" form instead of
    actually spread.
    <p>
    Examples:
    <ul>
    <li>Mushrooms spreading.
    <li>Fire spreading.
    </ul>
    <p>
    If a Block Spread event is cancelled, the block will not spread.
    
    @see BlockFormEvent
    """

    handlers: HandlerList

    def __init__(self, block: Block, source: Block, new_state: BlockState) -> None:
        """
        Initializes a BlockSpreadEvent.

        :param block: The block that is spreading.
        :param source: The source block involved in this event.
        :param new_state: The new state of the block.
        """
        ...

    def get_source(self) -> Block:
        """
        Gets the source block involved in this event.

        :return: the Block for the source block involved in this event.
        """
        ...

    def get_handlers(self) -> HandlerList:
        ...
    
    @staticmethod
    def get_handler_list() -> HandlerList:
        ...
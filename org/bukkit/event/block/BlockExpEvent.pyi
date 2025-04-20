from org.bukkit.block import Block
from org.bukkit.event import HandlerList
from org.bukkit.event.block import BlockEvent
from typing import Any

class BlockExpEvent(BlockEvent):
    """
    An event that's called when a block yields experience.
    """
    
    handlers: HandlerList = HandlerList()
    exp: int

    def __init__(self, block: Block, exp: int) -> None:
        super().__init__(block)
        self.exp = exp

    """
    Get the experience dropped by the block after the event has processed

    @return The experience to drop
    """
    def get_exp_to_drop(self) -> int:
        ...

    """
    Set the amount of experience dropped by the block after the event has
    processed

    @param exp 1 or higher to drop experience, else nothing will drop
    """
    def set_exp_to_drop(self, exp: int) -> None:
        ...

    @Override
    def get_handlers(self) -> HandlerList:
        ...

    @staticmethod
    def get_handler_list() -> HandlerList:
        ...
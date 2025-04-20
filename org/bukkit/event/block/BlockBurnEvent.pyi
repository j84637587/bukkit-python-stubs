from org.bukkit.block import Block
from org.bukkit.event import Cancellable, HandlerList
from typing import Optional

class BlockBurnEvent(BlockEvent, Cancellable):
    """
    Called when a block is destroyed as a result of being burnt by fire.
    <p>
    If a Block Burn event is cancelled, the block will not be destroyed as a
    result of being burnt by fire.
    """

    handlers: HandlerList

    def __init__(self, block: Block, igniting_block: Optional[Block] = None) -> None:
        ...

    @staticmethod
    def get_handler_list() -> HandlerList:
        ...

        def get_igniting_block(self) -> Optional[Block]:
        ...

    def is_cancelled(self) -> bool:
        ...

    def set_cancelled(self, cancel: bool) -> None:
        ...

        def get_handlers(self) -> HandlerList:
        ...
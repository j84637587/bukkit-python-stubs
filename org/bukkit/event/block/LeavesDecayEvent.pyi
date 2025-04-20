from org.bukkit.block import Block
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.event.block import BlockEvent
from typing import Any

class LeavesDecayEvent(BlockEvent, Cancellable):
    """
    Called when leaves are decaying naturally.
    <p>
    If a Leaves Decay event is cancelled, the leaves will not decay.
    """

    handlers: HandlerList = HandlerList()
    cancel: bool = False

    def __init__(self, block: Block) -> None:
        super().__init__(block)

    def isCancelled(self) -> bool:
        return self.cancel

    def setCancelled(self, cancel: bool) -> None:
        self.cancel = cancel

    def getHandlers(self) -> HandlerList:
        return self.handlers

    @staticmethod
    def getHandlerList() -> HandlerList:
        return LeavesDecayEvent.handlers
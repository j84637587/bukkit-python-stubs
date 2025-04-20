from org.bukkit.Chunk import Chunk
from org.bukkit.event.HandlerList import HandlerList
from org.bukkit.generator.BlockPopulator import BlockPopulator
from typing import Any

class ChunkLoadEvent(ChunkEvent):
    """
    Called when a chunk is loaded
    """

    handlers: HandlerList = HandlerList()
    newChunk: bool

    def __init__(self, chunk: Chunk, newChunk: bool) -> None:
        super().__init__(chunk)
        self.newChunk = newChunk

    """
    Gets if this chunk was newly created or not.
    <p>
    <b>Note:</b> Do not use this to generated blocks in a newly generated chunk.
    Use a {@link BlockPopulator} instead.

    @return true if the chunk is new, otherwise false
    """
    def isNewChunk(self) -> bool:
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        ...

    def getHandlers(self) -> HandlerList:
        ...
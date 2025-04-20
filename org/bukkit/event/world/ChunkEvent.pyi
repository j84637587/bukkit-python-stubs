from org.bukkit.Chunk import Chunk
from org.bukkit.event.world.WorldEvent import WorldEvent
from typing import Any
from typing import Optional

class ChunkEvent(WorldEvent):
    """
    Represents a Chunk related event
    """

    chunk: Chunk

    def __init__(self, chunk: Chunk) -> None:
        super().__init__(chunk.getWorld())
        self.chunk = chunk

    """
    Gets the chunk being loaded/unloaded

    @return Chunk that triggered this event
    """
    def getChunk(self) -> Chunk:
        ...
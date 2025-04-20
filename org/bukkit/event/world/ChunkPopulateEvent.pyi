from org.bukkit.Chunk import Chunk
from org.bukkit.event.HandlerList import HandlerList
from org.bukkit.generator.BlockPopulator import BlockPopulator
from typing import Any
from org.bukkit.event.world.ChunkEvent import ChunkEvent
from org.jetbrains.annotations import NotNull

class ChunkPopulateEvent(ChunkEvent):
    """
    Thrown when a newly generated chunk has finished being populated.
    <p>
    <b>Note:</b> Do not use this to generated blocks in a newly generated chunk.
    Use a {@link BlockPopulator} instead.
    """

    handlers: HandlerList = HandlerList()

    def __init__(self, chunk: NotNull[Chunk]) -> None:
        super().__init__(chunk)

        def get_handlers(self) -> HandlerList:
        ...

        @staticmethod
    def get_handler_list() -> HandlerList:
        ...
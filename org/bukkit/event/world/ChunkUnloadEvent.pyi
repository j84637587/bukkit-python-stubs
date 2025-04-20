from org.bukkit.Chunk import Chunk
from org.bukkit.event.HandlerList import HandlerList
from org.jetbrains.annotations import NotNull

class ChunkEvent:
    pass  # Placeholder for the parent class

class ChunkUnloadEvent(ChunkEvent):
    """
    Called when a chunk is unloaded
    """

    handlers: HandlerList = HandlerList()
    saveChunk: bool

    def __init__(self, chunk: NotNull[Chunk]) -> None:
        self.__init__(chunk, True)

    def __init__(self, chunk: NotNull[Chunk], save: bool) -> None:
        super().__init__(chunk)
        self.saveChunk = save

    """
    Return whether this chunk will be saved to disk.

    @return chunk save status
    """
    def is_save_chunk(self) -> bool:
        ...

    """
    Set whether this chunk will be saved to disk.

    @param saveChunk chunk save status
    """
    def set_save_chunk(self, saveChunk: bool) -> None:
        ...

        def get_handlers(self) -> HandlerList:
        ...

        @staticmethod
    def get_handler_list() -> HandlerList:
        ...
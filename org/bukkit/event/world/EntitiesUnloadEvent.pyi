from typing import List
from org.bukkit.Chunk import Chunk
from org.bukkit.entity.Entity import Entity
from org.bukkit.event.HandlerList import HandlerList
from org.jetbrains.annotations import NotNull

class EntitiesUnloadEvent(ChunkEvent):
    """
    Called when entities are unloaded.

    The provided chunk may or may not be loaded.
    """

    handlers: HandlerList = HandlerList()
    entities: List[Entity]

    def __init__(self, chunk: NotNull[Chunk], entities: NotNull[List[Entity]]) -> None:
        ...

    """
    Get the entities which are being unloaded.

    @return unmodifiable list of unloaded entities.
    """
        def get_entities(self) -> List[Entity]:
        ...

        def get_handlers(self) -> HandlerList:
        ...

        @staticmethod
    def get_handler_list() -> HandlerList:
        ...
from typing import List
from org.bukkit.Chunk import Chunk
from org.bukkit.entity.Entity import Entity
from org.bukkit.event.HandlerList import HandlerList
from org.bukkit.event.world.ChunkEvent import ChunkEvent
from org.jetbrains.annotations import NotNull

class EntitiesLoadEvent(ChunkEvent):
    """
    Called when entities are loaded.

    The provided chunk may or may not be loaded.
    """

    handlers: HandlerList = HandlerList()
    entities: List[Entity]

    def __init__(self, chunk: NotNull[Chunk], entities: NotNull[List[Entity]]) -> None:
        super().__init__(chunk)
        self.entities = entities

    """
    Get the entities which are being loaded.

    @return unmodifiable list of loaded entities.
    """
        def get_entities(self) -> List[Entity]:
        ...

        def get_handlers(self) -> HandlerList:
        ...

        @staticmethod
    def get_handler_list() -> HandlerList:
        ...
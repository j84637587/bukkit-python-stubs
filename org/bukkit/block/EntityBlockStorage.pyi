from typing import List, TypeVar
from .tile_state import TileState
from org.bukkit.entity import Entity

T = TypeVar("T", bound=Entity)

class EntityBlockStorage(TileState[T]):
    """
    Represents a captured state of a block which stores entities.

    @param <T> Entity this block can store
    """

    def is_full(self) -> bool:
        """
        Check if the block is completely full of entities.

        @return True if block is full
        """
        ...

    def get_entity_count(self) -> int:
        """
        Get the amount of entities currently in this block.

        @return Amount of entities currently in this block
        """
        ...

    def get_max_entities(self) -> int:
        """
        Get the maximum amount of entities this block can hold.

        @return Maximum amount of entities this block can hold
        """
        ...

    def set_max_entities(self, max: int) -> None:
        """
        Set the maximum amount of entities this block can hold.

        @param max Maximum amount of entities this block can hold
        """
        ...

    def release_entities(self) -> List[T]:
        """
        Release all the entities currently stored in the block.

        @return List of all entities which were released
        """
        ...

    def add_entity(self, entity: T) -> None:
        """
        Add an entity to the block.

        @param entity Entity to add to the block
        """
        ...

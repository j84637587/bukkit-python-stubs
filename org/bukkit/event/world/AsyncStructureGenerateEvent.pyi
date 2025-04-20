from collections import OrderedDict
from typing import Dict, Optional

from org.bukkit import NamespacedKey, World
from org.bukkit.event import HandlerList, WorldEvent
from org.bukkit.generator.structure import Structure
from org.bukkit.util import BlockTransformer, BoundingBox, EntityTransformer
from org.jetbrains.annotations import ApiStatus, NotNull, Nullable

class AsyncStructureGenerateEvent(WorldEvent):
    class Cause:
        COMMAND = "COMMAND"
        WORLD_GENERATION = "WORLD_GENERATION"
        CUSTOM = "CUSTOM"

    handlers: HandlerList = HandlerList()

    def __init__(self: "AsyncStructureGenerateEvent", world: World, async_: bool, cause: "AsyncStructureGenerateEvent.Cause", structure: Structure, bounding_box: BoundingBox, chunk_x: int, chunk_z: int) -> None:
        super().__init__(world, async_)
        self.structure: Structure = structure
        self.bounding_box: BoundingBox = bounding_box
        self.chunk_x: int = chunk_x
        self.chunk_z: int = chunk_z
        self.cause: "AsyncStructureGenerateEvent.Cause" = cause
        self.block_transformers: Dict[NamespacedKey, BlockTransformer] = OrderedDict()
        self.entity_transformers: Dict[NamespacedKey, EntityTransformer] = OrderedDict()

        def get_cause(self: "AsyncStructureGenerateEvent") -> "AsyncStructureGenerateEvent.Cause":
        """Gets the event cause."""
        return self.cause

        def get_block_transformer(self: "AsyncStructureGenerateEvent", key: NamespacedKey) -> Optional[BlockTransformer]:
        """Gets a block transformer by key."""
        return self.block_transformers.get(key)

    def set_block_transformer(self: "AsyncStructureGenerateEvent", key: NamespacedKey, transformer: BlockTransformer) -> None:
        """Sets a block transformer to a key."""
        self.block_transformers[key] = transformer

    def remove_block_transformer(self: "AsyncStructureGenerateEvent", key: NamespacedKey) -> None:
        """Removes a block transformer."""
        self.block_transformers.pop(key, None)

    def clear_block_transformers(self: "AsyncStructureGenerateEvent") -> None:
        """Removes all block transformers."""
        self.block_transformers.clear()

        def get_block_transformers(self: "AsyncStructureGenerateEvent") -> Dict[NamespacedKey, BlockTransformer]:
        """Gets all block transformers in an unmodifiable map."""
        return dict(self.block_transformers)

        def get_entity_transformer(self: "AsyncStructureGenerateEvent", key: NamespacedKey) -> Optional[EntityTransformer]:
        """Gets an entity transformer by key."""
        return self.entity_transformers.get(key)

    def set_entity_transformer(self: "AsyncStructureGenerateEvent", key: NamespacedKey, transformer: EntityTransformer) -> None:
        """Sets an entity transformer to a key."""
        self.entity_transformers[key] = transformer

    def remove_entity_transformer(self: "AsyncStructureGenerateEvent", key: NamespacedKey) -> None:
        """Removes an entity transformer."""
        self.entity_transformers.pop(key, None)

    def clear_entity_transformers(self: "AsyncStructureGenerateEvent") -> None:
        """Removes all entity transformers."""
        self.entity_transformers.clear()

        def get_entity_transformers(self: "AsyncStructureGenerateEvent") -> Dict[NamespacedKey, EntityTransformer]:
        """Gets all entity transformers in an unmodifiable map."""
        return dict(self.entity_transformers)

        def get_structure(self: "AsyncStructureGenerateEvent") -> Structure:
        """Get the structure reference that is generated."""
        return self.structure

        def get_bounding_box(self: "AsyncStructureGenerateEvent") -> BoundingBox:
        """Get the bounding box of the structure."""
        return self.bounding_box.clone()

    def get_chunk_x(self: "AsyncStructureGenerateEvent") -> int:
        """Get the x coordinate of the origin chunk of the structure."""
        return self.chunk_x

    def get_chunk_z(self: "AsyncStructureGenerateEvent") -> int:
        """Get the z coordinate of the origin chunk of the structure."""
        return self.chunk_z

        def get_handlers(self: "AsyncStructureGenerateEvent") -> HandlerList:
        """Override method to get handlers."""
        return self.handlers

        @staticmethod
    def get_handler_list() -> HandlerList:
        """Static method to get handler list."""
        return AsyncStructureGenerateEvent.handlers
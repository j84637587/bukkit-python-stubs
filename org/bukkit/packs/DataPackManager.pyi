from typing import Collection, Optional
from org.bukkit.Material import Material
from org.bukkit.NamespacedKey import NamespacedKey
from org.bukkit.World import World
from org.bukkit.block.BlockType import BlockType
from org.bukkit.entity.EntityType import EntityType
from org.bukkit.inventory.ItemType import ItemType
from org.jetbrains.annotations import ApiStatus, NotNull, Nullable

"""
Manager of data packs.
"""
class DataPackManager:

    """
    Return all the available {@link DataPack}s on the server.

    @return a Collection of {@link DataPack}
    """
        def getDataPacks(self) -> Collection['DataPack']:
        ...

    """
    Gets a {@link DataPack} by its key.

    @param dataPackKey the key of the {@link DataPack}
    @return the {@link DataPack} or null if it does not exist
    """
        def getDataPack(self, dataPackKey: @NotNull NamespacedKey) -> Optional['DataPack']:
        ...

    """
    Return all the enabled {@link DataPack} in the World.

    @param world the world to search
    @return a Collection of {@link DataPack}
    """
        def getEnabledDataPacks(self, world: @NotNull World) -> Collection['DataPack']:
        ...

    """
    Return all the disabled {@link DataPack} in the World.

    @param world the world to search
    @return a Collection of {@link DataPack}
    """
        def getDisabledDataPacks(self, world: @NotNull World) -> Collection['DataPack']:
        ...

    """
    Gets if the Material is enabled for use by the features in World.

    @param material Material to check (needs to be an {@link Material#isItem()} or {@link Material#isBlock()})
    @param world World to check
    @return {@code True} if the Item/Block related to the material is enabled
    """
    def isEnabledByFeature(self, material: @NotNull Material, world: @NotNull World) -> bool:
        ...

    """
    Gets if the ItemType is enabled for use by the features in World.

    @param itemType ItemType to check
    @param world World to check
    @return {@code True} if the ItemType is enabled
    @apiNote this method is not ready for public usage yet
    """
        def isEnabledByFeature(self, itemType: @NotNull ItemType, world: @NotNull World) -> bool:
        ...

    """
    Gets if the BlockType is enabled for use by the features in World.

    @param blockType BlockType to check
    @param world World to check
    @return {@code True} if the BlockType is enabled
    @apiNote this method is not ready for public usage yet
    """
        def isEnabledByFeature(self, blockType: @NotNull BlockType, world: @NotNull World) -> bool:
        ...

    """
    Gets if the EntityType is enabled for use by the Features in World.

    @param entityType EntityType to check
    @param world World to check
    @return {@code True} if the type of entity is enabled
    """
    def isEnabledByFeature(self, entityType: @NotNull EntityType, world: @NotNull World) -> bool:
        ...
from typing import Collection, List
from org.bukkit.Location import Location
from org.bukkit.RegionAccessor import RegionAccessor
from org.bukkit.block.structure.Mirror import Mirror
from org.bukkit.block.structure.StructureRotation import StructureRotation
from org.bukkit.entity.Entity import Entity
from org.bukkit.persistence.PersistentDataHolder import PersistentDataHolder
from org.bukkit.util.BlockTransformer import BlockTransformer
from org.bukkit.util.BlockVector import BlockVector
from org.bukkit.util.EntityTransformer import EntityTransformer
from org.jetbrains.annotations import ApiStatus, NotNull
import random

"""
Represents a structure.
<p>
A structure is a mutable template of captured blocks and entities that can be
copied back into the world. The {@link StructureManager}, retrieved via
{@link org.bukkit.Server#getStructureManager()}, allows you to create new
structures, load existing structures, and save structures.
<p>
In order for a structure to be usable by structure blocks, it needs to be
null {@link StructureManager#registerStructure(org.bukkit.NamespacedKey, Structure)
registered} with the {@link StructureManager}, or located in the primary
world folder, a DataPack, or the server's own default resources, so that the
StructureManager can find it.
"""
class Structure(PersistentDataHolder):
    """
    Gets the current size of the structure.
    <p>
    The size of the structure may not be fixed.

    @return A new vector that represents the size of the structure along each
    axis.
    """
        def get_size(self) -> BlockVector: ...

    """
    Gets a list of available block palettes.

    @return a list of available variants of this structure.
    """
        def get_palettes(self) -> List['Palette']: ...

    """
    Gets the number of palettes in this structure.

    @return The number of palettes in this structure
    """
    def get_palette_count(self) -> int: ...

    """
    Gets a list of entities that have been included in the Structure.

    The entity positions are offsets relative to the structure's position
    that is provided once the structure is placed into the world.

    @return a list of Entities included in the Structure.
    """
        def get_entities(self) -> List[Entity]: ...

    """
    Gets the number of entities in this structure.

    @return The number of entities in this structure
    """
    def get_entity_count(self) -> int: ...

    """
    Place a structure in the world.

    @param location The location to place the structure at.
    @param include_entities If the entities present in the structure should be
    spawned.
    @param structure_rotation The rotation of the structure.
    @param mirror The mirror settings of the structure.
    @param palette The palette index of the structure to use, starting at
    {@code 0}, or {@code -1} to pick a random palette.
    @param integrity Determines how damaged the building should look by
    randomly skipping blocks to place. This value can range from 0 to 1. With
    0 removing all blocks and 1 spawning the structure in pristine condition.
    @param random The randomizer used for setting the structure's
    {@link org.bukkit.loot.LootTable}s and integrity.
    """
    def place(self,
              location: Location,
              include_entities: bool,
              structure_rotation: StructureRotation,
              mirror: Mirror,
              palette: int,
              integrity: float,
              random: random.Random) -> None: ...

    """
    Place a structure in the world.

    @param location The location to place the structure at.
    @param include_entities If the entities present in the structure should be
    spawned.
    @param structure_rotation The rotation of the structure.
    @param mirror The mirror settings of the structure.
    @param palette The palette index of the structure to use, starting at
    {@code 0}, or {@code -1} to pick a random palette.
    @param integrity Determines how damaged the building should look by
    randomly skipping blocks to place. This value can range from 0 to 1. With
    0 removing all blocks and 1 spawning the structure in pristine condition.
    @param random The randomizer used for setting the structure's
    {@link org.bukkit.loot.LootTable}s and integrity.
    @param block_transformers A collection of {@link BlockTransformer}s to apply to the structure.
    @param entity_transformers A collection of {@link EntityTransformer}s to apply to the structure.
    """
        def place(self,
              location: Location,
              include_entities: bool,
              structure_rotation: StructureRotation,
              mirror: Mirror,
              palette: int,
              integrity: float,
              random: random.Random,
              block_transformers: Collection[BlockTransformer],
              entity_transformers: Collection[EntityTransformer]) -> None: ...

    """
    Place a structure in the world.

    @param region_accessor The world to place the structure in.
    @param location The location to place the structure at.
    @param include_entities If the entities present in the structure should be
    spawned.
    @param structure_rotation The rotation of the structure.
    @param mirror The mirror settings of the structure.
    @param palette The palette index of the structure to use, starting at
    {@code 0}, or {@code -1} to pick a random palette.
    @param integrity Determines how damaged the building should look by
    randomly skipping blocks to place. This value can range from 0 to 1. With
    0 removing all blocks and 1 spawning the structure in pristine condition.
    @param random The randomizer used for setting the structure's
    {@link org.bukkit.loot.LootTable}s and integrity.
    """
    def place(self,
              region_accessor: RegionAccessor,
              location: BlockVector,
              include_entities: bool,
              structure_rotation: StructureRotation,
              mirror: Mirror,
              palette: int,
              integrity: float,
              random: random.Random) -> None: ...

    """
    Place a structure in the world.

    @param region_accessor The world to place the structure in.
    @param location The location to place the structure at.
    @param include_entities If the entities present in the structure should be
    spawned.
    @param structure_rotation The rotation of the structure.
    @param mirror The mirror settings of the structure.
    @param palette The palette index of the structure to use, starting at
    {@code 0}, or {@code -1} to pick a random palette.
    @param integrity Determines how damaged the building should look by
    randomly skipping blocks to place. This value can range from 0 to 1. With
    0 removing all blocks and 1 spawning the structure in pristine condition.
    @param random The randomizer used for setting the structure's
    {@link org.bukkit.loot.LootTable}s and integrity.
    @param block_transformers A collection of {@link BlockTransformer}s to apply to the structure.
    @param entity_transformers A collection of {@link EntityTransformer}s to apply to the structure.
    """
        def place(self,
              region_accessor: RegionAccessor,
              location: BlockVector,
              include_entities: bool,
              structure_rotation: StructureRotation,
              mirror: Mirror,
              palette: int,
              integrity: float,
              random: random.Random,
              block_transformers: Collection[BlockTransformer],
              entity_transformers: Collection[EntityTransformer]) -> None: ...

    """
    Fills the structure from an area in a world. The origin and size will be
    calculated automatically from the two corners provided.
    <p>
    Be careful as this will override the current data of the structure.
    <p>
    Be aware that this method allows for creating structures larger than the
    48x48x48 size that Minecraft's Structure blocks support. Any structures
    saved this way can not be loaded by using a structure block. Using the
    API however will still work.

    @param corner1 A corner of the structure.
    @param corner2 The corner opposite from corner1.
    @param include_entities true if entities should be included in the saved
    structure.
    """
    def fill(self,
             corner1: Location,
             corner2: Location,
             include_entities: bool) -> None: ...

    """
    Fills the Structure from an area in a world, starting at the specified
    origin and extending in each axis according to the specified size vector.
    <p>
    Be careful as this will override the current data of the structure.
    <p>
    Be aware that this method allows for saving structures larger than the
    48x48x48 size that Minecraft's Structure blocks support. Any structures
    saved this way can not be loaded by using a structure block. Using the
    API however will still work.

    @param origin The origin of the structure.
    @param size The size of the structure, must be at least 1x1x1.
    @param include_entities true if entities should be included in the saved
    structure.
    @throws IllegalArgumentException Thrown if size is smaller than 1x1x1
    """
    def fill(self,
             origin: Location,
             size: BlockVector,
             include_entities: bool) -> None: ...
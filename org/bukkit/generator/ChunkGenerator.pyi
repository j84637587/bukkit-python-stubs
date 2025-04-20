from typing import List, Optional
import random

from org.bukkit import Bukkit, HeightMap, Location, Material, World, Block
from org.bukkit.block import Biome
from org.bukkit.block.data import BlockData
from org.bukkit.material import MaterialData
from org.jetbrains.annotations import NotNull, Nullable


class ChunkGenerator:
    """
    A chunk generator is responsible for the initial shaping of an entire
    chunk. For example, the nether chunk generator should shape netherrack and
    soulsand.

    A chunk is generated in multiple steps, those steps are always in the same
    order. Between those steps however an unlimited time may pass. This means, a
    chunk may generated until the surface step and continue with the bedrock step
    after one or multiple server restarts or even after multiple Minecraft
    versions.

    The order of generation is as follows
    <ol>
    <li>{@link #generateNoise(WorldInfo, Random, int, int, ChunkData)}</li>
    <li>{@link #generateSurface(WorldInfo, Random, int, int, ChunkData)}</li>
    <li>{@link #generateBedrock(WorldInfo, Random, int, int, ChunkData)}</li>
    <li>{@link #generateCaves(WorldInfo, Random, int, int, ChunkData)}</li>
    </ol>

    Every method listed above as well as
    {@link #getBaseHeight(WorldInfo, Random, int, int, HeightMap)}
    <b>must</b> be completely thread safe and able to handle multiple concurrent
    callers.

    Some aspects of world generation can be delegated to the Vanilla generator.
    The following methods can be overridden to enable this:
    <ul>
    <li>{@link ChunkGenerator#shouldGenerateNoise()} or {@link ChunkGenerator#shouldGenerateNoise(WorldInfo, Random, int, int)}</li>
    <li>{@link ChunkGenerator#shouldGenerateSurface()} or {@link ChunkGenerator#shouldGenerateSurface(WorldInfo, Random, int, int)}</li>
    <li>{@link ChunkGenerator#shouldGenerateCaves()} or {@link ChunkGenerator#shouldGenerateCaves(WorldInfo, Random, int, int)}</li>
    <li>{@link ChunkGenerator#shouldGenerateDecorations()} or {@link ChunkGenerator#shouldGenerateDecorations(WorldInfo, Random, int, int)}</li>
    <li>{@link ChunkGenerator#shouldGenerateMobs()} or {@link ChunkGenerator#shouldGenerateMobs(WorldInfo, Random, int, int)}</li>
    <li>{@link ChunkGenerator#shouldGenerateStructures()} or {@link ChunkGenerator#shouldGenerateStructures(WorldInfo, Random, int, int)}</li>
    </ul>
    """

    def generateNoise(self, worldInfo: 'WorldInfo', random: random.Random, chunkX: int, chunkZ: int, chunkData: 'ChunkData') -> None:
        """
        Shapes the Chunk noise for the given coordinates.
        <p>
        Notes:
        <p>
        This method should <b>never</b> attempt to get the Chunk at the passed
        coordinates, as doing so may cause an infinite loop.
        <p>
        This method should <b>never</b> modify the {@link ChunkData} at a later
        point of time.
        <p>
        The Y-coordinate range should <b>never</b> be hardcoded, to get the
        Y-coordinate range use the methods {@link ChunkData#getMinHeight()} and
        {@link ChunkData#getMaxHeight()}.
        <p>
        If {@link #shouldGenerateNoise()} is set to true, the given
        {@link ChunkData} contains already the Vanilla noise generation.
        """
        pass

    def generateSurface(self, worldInfo: 'WorldInfo', random: random.Random, chunkX: int, chunkZ: int, chunkData: 'ChunkData') -> None:
        """
        Shapes the Chunk surface for the given coordinates.
        <p>
        Notes:
        <p>
        This method should <b>never</b> attempt to get the Chunk at the passed
        coordinates, as doing so may cause an infinite loop.
        <p>
        This method should <b>never</b> modify the {@link ChunkData} at a later
        point of time.
        <p>
        The Y-coordinate range should <b>never</b> be hardcoded, to get the
        Y-coordinate range use the methods {@link ChunkData#getMinHeight()} and
        {@link ChunkData#getMaxHeight()}.
        <p>
        If {@link #shouldGenerateSurface()} is set to true, the given
        {@link ChunkData} contains already the Vanilla surface generation.
        """
        pass

    def generateBedrock(self, worldInfo: 'WorldInfo', random: random.Random, chunkX: int, chunkZ: int, chunkData: 'ChunkData') -> None:
        """
        Shapes the Chunk bedrock layer for the given coordinates.
        <p>
        Notes:
        <p>
        This method should <b>never</b> attempt to get the Chunk at the passed
        coordinates, as doing so may cause an infinite loop.
        <p>
        This method should <b>never</b> modify the {@link ChunkData} at a later
        point of time.
        <p>
        The Y-coordinate range should <b>never</b> be hardcoded, to get the
        Y-coordinate range use the methods {@link ChunkData#getMinHeight()} and
        {@link ChunkData#getMaxHeight()}.
        <p>
        """
        pass

    def generateCaves(self, worldInfo: 'WorldInfo', random: random.Random, chunkX: int, chunkZ: int, chunkData: 'ChunkData') -> None:
        """
        Shapes the Chunk caves for the given coordinates.
        <p>
        Notes:
        <p>
        This method should <b>never</b> attempt to get the Chunk at the passed
        coordinates, as doing so may cause an infinite loop.
        <p>
        This method should <b>never</b> modify the {@link ChunkData} at a later
        point of time.
        <p>
        The Y-coordinate range should <b>never</b> be hardcoded, to get the
        Y-coordinate range use the methods {@link ChunkData#getMinHeight()} and
        {@link ChunkData#getMaxHeight()}.
        <p>
        If {@link #shouldGenerateCaves()} is set to true, the given
        {@link ChunkData} contains already the Vanilla cave generation.
        """
        pass

        def getDefaultBiomeProvider(self, worldInfo: 'WorldInfo') -> Optional['BiomeProvider']:
        """
        Gets called when no {@link BiomeProvider} is set in
        {@link org.bukkit.WorldCreator} or via the server configuration files. It
        is therefore possible that one plugin can provide the Biomes and another
        one the generation.
        <p>
        Notes:
        <p>
        If <code>null</code> is returned, than Vanilla biomes are used.
        <p>
        This method only gets called once when the world is loaded. Returning
        another {@link BiomeProvider} later one is not respected.
        """
        return None

    def getBaseHeight(self, worldInfo: 'WorldInfo', random: random.Random, x: int, z: int, heightMap: HeightMap) -> int:
        """
        This method is similar to
        {@link World#getHighestBlockAt(int, int, HeightMap)}. With the difference
        being, that the highest y coordinate should be the block before any
        surface, bedrock, caves or decoration is applied. Or in other words the
        highest block when only the noise is present at the chunk.
        <p>
        Notes:
        <p>
        When this method is not overridden, the Vanilla base height is used.
        <p>
        This method should <b>never</b> attempt to get the Chunk at the passed
        coordinates, or use the method
        {@link World#getHighestBlockAt(int, int, HeightMap)}, as doing so may
        cause an infinite loop.
        """
        raise NotImplementedError("Not implemented")

    class BiomeGrid:
        """
        Interface to biome section for chunk to be generated: initialized with
        default values for world type and seed.
        <p>
        Custom generator is free to access and tailor values during
        generateBlockSections() or generateExtBlockSections().
        @deprecated Biomes are now set with {@link BiomeProvider}
        """

                def getBiome(self, x: int, z: int) -> Biome:
            """
            Get biome at x, z within chunk being generated
            @param x - 0-15
            @param z - 0-15
            @return Biome value
            @deprecated biomes are now 3-dimensional
            """
            pass

                def getBiome(self, x: int, y: int, z: int) -> Biome:
            """
            Get biome at x, z within chunk being generated
            @param x - 0-15
            @param y - world minHeight (inclusive) - world maxHeight (exclusive)
            @param z - 0-15
            @return Biome value
            """
            pass

        def setBiome(self, x: int, z: int, bio: Biome) -> None:
            """
            Set biome at x, z within chunk being generated
            @param x - 0-15
            @param z - 0-15
            @param bio - Biome value
            @deprecated biomes are now 3-dimensional
            """
            pass

        def setBiome(self, x: int, y: int, z: int, bio: Biome) -> None:
            """
            Set biome at x, z within chunk being generated
            @param x - 0-15
            @param y - world minHeight (inclusive) - world maxHeight (exclusive)
            @param z - 0-15
            @param bio - Biome value
            """
            pass

        @Deprecated(since="1.17.1")
    def generateChunkData(self, world: World, random: random.Random, x: int, z: int, biome: BiomeGrid) -> 'ChunkData':
        """
        Shapes the chunk for the given coordinates.
        This method must return a ChunkData.
        <p>
        Notes:
        <p>
        This method should <b>never</b> attempt to get the Chunk at
        the passed coordinates, as doing so may cause an infinite loop
        <p>
        This method should <b>never</b> modify a ChunkData after it has
        been returned.
        <p>
        This method <b>must</b> return a ChunkData returned by {@link ChunkGenerator#createChunkData(org.bukkit.World)}
        """
        raise NotImplementedError("Not implemented, no longer needed")

        @Deprecated(since="1.17.1")
    def createChunkData(self, world: World) -> 'ChunkData':
        """
        Create a ChunkData for a world.
        @param world the world the ChunkData is for
        @return a new ChunkData for world
        @deprecated {@link ChunkData} are now directly provided
        """
        return Bukkit.getServer().createChunkData(world)

    def canSpawn(self, world: World, x: int, z: int) -> bool:
        """
        Tests if the specified location is valid for a natural spawn position
        @param world The world we're testing on
        @param x X-coordinate of the block to test
        @param z Z-coordinate of the block to test
        @return true if the location is valid, otherwise false
        """
        highest: Block = world.getBlockAt(x, world.getHighestBlockYAt(x, z), z)

        if world.getEnvironment() == 'NETHER':
            return True
        elif world.getEnvironment() == 'THE_END':
            return highest.getType() != Material.AIR and highest.getType() != Material.WATER and highest.getType() != Material.LAVA
        else:
            return highest.getType() == Material.SAND or highest.getType() == Material.GRAVEL

        def getDefaultPopulators(self, world: World) -> List['BlockPopulator']:
        """
        Gets a list of default {@link BlockPopulator}s to apply to a given
        world
        @param world World to apply to
        @return List containing any amount of BlockPopulators
        """
        return []

        def getFixedSpawnLocation(self, world: World, random: random.Random) -> Optional[Location]:
        """
        Gets a fixed spawn location to use for a given world.
        <p>
        A null value is returned if a world should not use a fixed spawn point,
        and will instead attempt to find one randomly.
        @param world The world to locate a spawn point for
        @param random Random generator to use in the calculation
        @return Location containing a new spawn point, otherwise null
        """
        return None

    @Deprecated(since="1.17.1")
    def isParallelCapable(self) -> bool:
        """
        Gets if this ChunkGenerator is parallel capable.
        See {@link ChunkGenerator} for more information.
        @return parallel capable status
        """
        return False

    def shouldGenerateNoise(self) -> bool:
        """
        Gets if the server should generate Vanilla noise.
        <p>
        The Vanilla noise is generated <b>before</b>
        {@link #generateNoise(WorldInfo, Random, int, int, ChunkData)} is called.
        <p>
        This is method is not called (and has therefore no effect), if
        {@link #shouldGenerateNoise(WorldInfo, Random, int, int)} is overridden.
        @return true if the server should generate Vanilla noise
        @see #shouldGenerateNoise(WorldInfo, Random, int, int)
        """
        return False

    def shouldGenerateNoise(self, worldInfo: 'WorldInfo', random: random.Random, chunkX: int, chunkZ: int) -> bool:
        """
        Gets if the server should generate Vanilla noise.
        <p>
        The Vanilla noise is generated <b>before</b>
        {@link #generateNoise(WorldInfo, Random, int, int, ChunkData)} is called.
        <p>
        Only this method is called if both this and
        {@link #shouldGenerateNoise()} are overridden.
        @param worldInfo The world info of the world this chunk will be used for
        @param random The random generator to use
        @param chunkX The X-coordinate of the chunk
        @param chunkZ The Z-coordinate of the chunk
        @return true if the server should generate Vanilla noise
        @see #shouldGenerateNoise()
        """
        return self.shouldGenerateNoise()

    def shouldGenerateSurface(self) -> bool:
        """
        Gets if the server should generate Vanilla surface.
        <p>
        The Vanilla surface is generated <b>before</b>
        {@link #generateSurface(WorldInfo, Random, int, int, ChunkData)} is
        called.
        <p>
        This is method is not called (and has therefore no effect), if
        {@link #shouldGenerateSurface(WorldInfo, Random, int, int)} is overridden.
        @return true if the server should generate Vanilla surface
        @see #shouldGenerateSurface(WorldInfo, Random, int, int)
        """
        return False

    def shouldGenerateSurface(self, worldInfo: 'WorldInfo', random: random.Random, chunkX: int, chunkZ: int) -> bool:
        """
        Gets if the server should generate Vanilla surface.
        <p>
        The Vanilla surface is generated <b>before</b>
        {@link #generateSurface(WorldInfo, Random, int, int, ChunkData)} is
        called.
        <p>
        Only this method is called if both this and
        {@link #shouldGenerateSurface()} are overridden.
        @param worldInfo The world info of the world this chunk will be used for
        @param random The random generator to use
        @param chunkX The X-coordinate of the chunk
        @param chunkZ The Z-coordinate of the chunk
        @return true if the server should generate Vanilla surface
        @see #shouldGenerateSurface()
        """
        return self.shouldGenerateSurface()

    def shouldGenerateBedrock(self) -> bool:
        """
        Gets if the server should generate Vanilla bedrock.
        <p>
        The Vanilla bedrock is generated <b>before</b>
        {@link #generateBedrock(WorldInfo, Random, int, int, ChunkData)} is
        called.
        @return true if the server should generate Vanilla bedrock
        @deprecated has no effect, bedrock generation is part of the surface step, see {@link #shouldGenerateSurface()}
        """
        return False

    def shouldGenerateCaves(self) -> bool:
        """
        Gets if the server should generate Vanilla caves.
        <p>
        The Vanilla caves are generated <b>before</b>
        {@link #generateCaves(WorldInfo, Random, int, int, ChunkData)} is called.
        <p>
        This is method is not called (and has therefore no effect), if
        {@link #shouldGenerateCaves(WorldInfo, Random, int, int)} is overridden.
        @return true if the server should generate Vanilla caves
        @see #shouldGenerateCaves(WorldInfo, Random, int, int)
        """
        return False

    def shouldGenerateCaves(self, worldInfo: 'WorldInfo', random: random.Random, chunkX: int, chunkZ: int) -> bool:
        """
        Gets if the server should generate Vanilla caves.
        <p>
        The Vanilla caves are generated <b>before</b>
        {@link #generateCaves(WorldInfo, Random, int, int, ChunkData)} is called.
        <p>
        Only this method is called if both this and
        {@link #shouldGenerateCaves()} are overridden.
        @param worldInfo The world info of the world this chunk will be used for
        @param random The random generator to use
        @param chunkX The X-coordinate of the chunk
        @param chunkZ The Z-coordinate of the chunk
        @return true if the server should generate Vanilla caves
        @see #shouldGenerateCaves()
        """
        return self.shouldGenerateCaves()

    def shouldGenerateDecorations(self) -> bool:
        """
        Gets if the server should generate Vanilla decorations after this
        ChunkGenerator.
        <p>
        The Vanilla decoration are generated <b>before</b> any
        {@link BlockPopulator} are called.
        <p>
        This is method is not called (and has therefore no effect), if
        {@link #shouldGenerateDecorations(WorldInfo, Random, int, int)} is overridden.
        @return true if the server should generate Vanilla decorations
        @see #shouldGenerateDecorations(WorldInfo, Random, int, int)
        """
        return False

    def shouldGenerateDecorations(self, worldInfo: 'WorldInfo', random: random.Random, chunkX: int, chunkZ: int) -> bool:
        """
        Gets if the server should generate Vanilla decorations after this
        ChunkGenerator.
        <p>
        The Vanilla decoration are generated <b>before</b> any
        {@link BlockPopulator} are called.
        <p>
        Only this method is called if both this and
        {@link #shouldGenerateDecorations()} are overridden.
        @param worldInfo The world info of the world this chunk will be used for
        @param random The random generator to use
        @param chunkX The X-coordinate of the chunk
        @param chunkZ The Z-coordinate of the chunk
        @return true if the server should generate Vanilla decorations
        @see #shouldGenerateDecorations()
        """
        return self.shouldGenerateDecorations()

    def shouldGenerateMobs(self) -> bool:
        """
        Gets if the server should generate Vanilla mobs after this
        ChunkGenerator.
        <p>
        This is method is not called (and has therefore no effect), if
        {@link #shouldGenerateMobs(WorldInfo, Random, int, int)} is overridden.
        @return true if the server should generate Vanilla mobs
        @see #shouldGenerateMobs(WorldInfo, Random, int, int)
        """
        return False

    def shouldGenerateMobs(self, worldInfo: 'WorldInfo', random: random.Random, chunkX: int, chunkZ: int) -> bool:
        """
        Gets if the server should generate Vanilla mobs after this
        ChunkGenerator.
        <p>
        Only this method is called if both this and
        {@link #shouldGenerateMobs()} are overridden.
        @param worldInfo The world info of the world this chunk will be used for
        @param random The random generator to use
        @param chunkX The X-coordinate of the chunk
        @param chunkZ The Z-coordinate of the chunk
        @return true if the server should generate Vanilla mobs
        @see #shouldGenerateMobs()
        """
        return self.shouldGenerateMobs()

    def shouldGenerateStructures(self) -> bool:
        """
        Gets if the server should generate Vanilla structures after this
        ChunkGenerator.
        <p>
        This is method is not called (and has therefore no effect), if
        {@link #shouldGenerateStructures(WorldInfo, Random, int, int)} is overridden.
        @return true if the server should generate Vanilla structures
        @see #shouldGenerateStructures(WorldInfo, Random, int, int)
        """
        return False

    def shouldGenerateStructures(self, worldInfo: 'WorldInfo', random: random.Random, chunkX: int, chunkZ: int) -> bool:
        """
        Gets if the server should generate Vanilla structures after this
        ChunkGenerator.
        <p>
        Only this method is called if both this and
        {@link #shouldGenerateStructures()} are overridden.
        @param worldInfo The world info of the world this chunk will be used for
        @param random The random generator to use
        @param chunkX The X-coordinate of the chunk
        @param chunkZ The Z-coordinate of the chunk
        @return true if the server should generate Vanilla structures
        @see #shouldGenerateStructures()
        """
        return self.shouldGenerateStructures()

    class ChunkData:
        """
        Data for a Chunk.
        """

        def getMinHeight(self) -> int:
            """
            Get the minimum height for this ChunkData.
            <p>
            It is not guaranteed that this method will return the same value as
            {@link World#getMinHeight()}.
            <p>
            Setting blocks below this height will do nothing.
            @return the minimum height
            """
            pass

        def getMaxHeight(self) -> int:
            """
            Get the maximum height for this ChunkData.
            <p>
            It is not guaranteed that this method will return the same value as
            {@link World#getMaxHeight()}.
            <p>
            Setting blocks at or above this height will do nothing.
            @return the maximum height
            """
            pass

                def getBiome(self, x: int, y: int, z: int) -> Biome:
            """
            Get the biome at x, y, z within chunk being generated
            @param x the x location in the chunk from 0-15 inclusive
            @param y the y location in the chunk from minimum (inclusive) -
            maxHeight (exclusive)
            @param z the z location in the chunk from 0-15 inclusive
            @return Biome value
            """
            pass

        def setBlock(self, x: int, y: int, z: int, material: Material) -> None:
            """
            Set the block at x,y,z in the chunk data to material.
            Note: setting blocks outside the chunk's bounds does nothing.
            @param x the x location in the chunk from 0-15 inclusive
            @param y the y location in the chunk from minHeight (inclusive) - maxHeight (exclusive)
            @param z the z location in the chunk from 0-15 inclusive
            @param material the type to set the block to
            """
            pass

        def setBlock(self, x: int, y: int, z: int, material: MaterialData) -> None:
            """
            Set the block at x,y,z in the chunk data to material.
            Setting blocks outside the chunk's bounds does nothing.
            @param x the x location in the chunk from 0-15 inclusive
            @param y the y location in the chunk from minHeight (inclusive) - maxHeight (exclusive)
            @param z the z location in the chunk from 0-15 inclusive
            @param material the type to set the block to
            """
            pass

        def setBlock(self, x: int, y: int, z: int, blockData: BlockData) -> None:
            """
            Set the block at x,y,z in the chunk data to material.
            Setting blocks outside the chunk's bounds does nothing.
            @param x the x location in the chunk from 0-15 inclusive
            @param y the y location in the chunk from minHeight (inclusive) - maxHeight (exclusive)
            @param z the z location in the chunk from 0-15 inclusive
            @param blockData the type to set the block to
            """
            pass

        def setRegion(self, xMin: int, yMin: int, zMin: int, xMax: int, yMax: int, zMax: int, material: Material) -> None:
            """
            Set a region of this chunk from xMin, yMin, zMin (inclusive)
            to xMax, yMax, zMax (exclusive) to material.
            Setting blocks outside the chunk's bounds does nothing.
            @param xMin minimum x location (inclusive) in the chunk to set
            @param yMin minimum y location (inclusive) in the chunk to set
            @param zMin minimum z location (inclusive) in the chunk to set
            @param xMax maximum x location (exclusive) in the chunk to set
            @param yMax maximum y location (exclusive) in the chunk to set
            @param zMax maximum z location (exclusive) in the chunk to set
            @param material the type to set the blocks to
            """
            pass

        def setRegion(self, xMin: int, yMin: int, zMin: int, xMax: int, yMax: int, zMax: int, material: MaterialData) -> None:
            """
            Set a region of this chunk from xMin, yMin, zMin (inclusive)
            to xMax, yMax, zMax (exclusive) to material.
            Setting blocks outside the chunk's bounds does nothing.
            @param xMin minimum x location (inclusive) in the chunk to set
            @param yMin minimum y location (inclusive) in the chunk to set
            @param zMin minimum z location (inclusive) in the chunk to set
            @param xMax maximum x location (exclusive) in the chunk to set
            @param yMax maximum y location (exclusive) in the chunk to set
            @param zMax maximum z location (exclusive) in the chunk to set
            @param material the type to set the blocks to
            """
            pass

        def setRegion(self, xMin: int, yMin: int, zMin: int, xMax: int, yMax: int, zMax: int, blockData: BlockData) -> None:
            """
            Set a region of this chunk from xMin, yMin, zMin (inclusive) to xMax,
            yMax, zMax (exclusive) to material.
            Setting blocks outside the chunk's bounds does nothing.
            @param xMin minimum x location (inclusive) in the chunk to set
            @param yMin minimum y location (inclusive) in the chunk to set
            @param zMin minimum z location (inclusive) in the chunk to set
            @param xMax maximum x location (exclusive) in the chunk to set
            @param yMax maximum y location (exclusive) in the chunk to set
            @param zMax maximum z location (exclusive) in the chunk to set
            @param blockData the type to set the blocks to
            """
            pass

                def getType(self, x: int, y: int, z: int) -> Material:
            """
            Get the type of the block at x, y, z.
            Getting blocks outside the chunk's bounds returns air.
            @param x the x location in the chunk from 0-15 inclusive
            @param y the y location in the chunk from minHeight (inclusive) - maxHeight (exclusive)
            @param z the z location in the chunk from 0-15 inclusive
            @return the type of the block or Material.AIR if x, y or z are outside the chunk's bounds
            """
            pass

                def getTypeAndData(self, x: int, y: int, z: int) -> MaterialData:
            """
            Get the type and data of the block at x, y, z.
            Getting blocks outside the chunk's bounds returns air.
            @param x the x location in the chunk from 0-15 inclusive
            @param y the y location in the chunk from minHeight (inclusive) - maxHeight (exclusive)
            @param z the z location in the chunk from 0-15 inclusive
            @return the type and data of the block or the MaterialData for air if x, y or z are outside the chunk's bounds
            """
            pass

                def getBlockData(self, x: int, y: int, z: int) -> BlockData:
            """
            Get the type and data of the block at x, y, z.
            Getting blocks outside the chunk's bounds returns air.
            @param x the x location in the chunk from 0-15 inclusive
            @param y the y location in the chunk from minHeight (inclusive) - maxHeight (exclusive)
            @param z the z location in the chunk from 0-15 inclusive
            @return the data of the block or the BlockData for air if x, y or z are outside the chunk's bounds
            """
            pass

        @Deprecated(since="1.8.8")
        def getData(self, x: int, y: int, z: int) -> int:
            """
            Get the block data at x,y,z in the chunk data.
            Getting blocks outside the chunk's bounds returns 0.
            @param x the x location in the chunk from 0-15 inclusive
            @param y the y location in the chunk from minHeight (inclusive) - maxHeight (exclusive)
            @param z the z location in the chunk from 0-15 inclusive
            @return the block data value or air if x, y or z are outside the chunk's bounds
            @deprecated Uses magic values
            """
            pass
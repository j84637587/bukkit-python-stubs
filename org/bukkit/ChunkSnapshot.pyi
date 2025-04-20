from org.bukkit.block import Biome, BlockData
from org.bukkit import Material
from typing import Any

class ChunkSnapshot:
    """
    Represents a static, thread-safe snapshot of chunk of blocks.
    Purpose is to allow clean, efficient copy of a chunk data to be made, and
    then handed off for processing in another thread (e.g. map rendering)
    """

    def getX(self) -> int:
        """
        Gets the X-coordinate of this chunk
        :return: X-coordinate
        """

    def getZ(self) -> int:
        """
        Gets the Z-coordinate of this chunk
        :return: Z-coordinate
        """

    def getWorldName(self) -> str:
        """
        Gets name of the world containing this chunk
        :return: Parent World Name
        """

    def getBlockType(self, x: int, y: int, z: int) -> Material:
        """
        Get block type for block at corresponding coordinate in the chunk
        :param x: 0-15
        :param y: world minHeight (inclusive) - world maxHeight (exclusive)
        :param z: 0-15
        :return: block material type
        """

    def getBlockData(self, x: int, y: int, z: int) -> BlockData:
        """
        Get block data for block at corresponding coordinate in the chunk
        :param x: 0-15
        :param y: world minHeight (inclusive) - world maxHeight (exclusive)
        :param z: 0-15
        :return: block material type
        """

    def getData(self, x: int, y: int, z: int) -> int:
        """
        Get block data for block at corresponding coordinate in the chunk
        :param x: 0-15
        :param y: world minHeight (inclusive) - world maxHeight (exclusive)
        :param z: 0-15
        :return: 0-15
        """

    def getBlockSkyLight(self, x: int, y: int, z: int) -> int:
        """
        Get sky light level for block at corresponding coordinate in the chunk
        :param x: 0-15
        :param y: world minHeight (inclusive) - world maxHeight (exclusive)
        :param z: 0-15
        :return: 0-15
        """

    def getBlockEmittedLight(self, x: int, y: int, z: int) -> int:
        """
        Get light level emitted by block at corresponding coordinate in the chunk
        :param x: 0-15
        :param y: world minHeight (inclusive) - world maxHeight (exclusive)
        :param z: 0-15
        :return: 0-15
        """

    def getHighestBlockYAt(self, x: int, z: int) -> int:
        """
        Gets the highest non-air coordinate at the given coordinates
        :param x: X-coordinate of the blocks (0-15)
        :param z: Z-coordinate of the blocks (0-15)
        :return: Y-coordinate of the highest non-air block
        """

    def getBiome(self, x: int, z: int) -> Biome:
        """
        Get biome at given coordinates
        :param x: X-coordinate (0-15)
        :param z: Z-coordinate (0-15)
        :return: Biome at given coordinate
        """

    def getBiome(self, x: int, y: int, z: int) -> Biome:
        """
        Get biome at given coordinates
        :param x: X-coordinate (0-15)
        :param y: Y-coordinate (world minHeight (inclusive) - world maxHeight (exclusive))
        :param z: Z-coordinate (0-15)
        :return: Biome at given coordinate
        """

    def getRawBiomeTemperature(self, x: int, z: int) -> float:
        """
        Get raw biome temperature at given coordinates
        :param x: X-coordinate (0-15)
        :param z: Z-coordinate (0-15)
        :return: temperature at given coordinate
        """

    def getRawBiomeTemperature(self, x: int, y: int, z: int) -> float:
        """
        Get raw biome temperature at given coordinates
        :param x: X-coordinate (0-15)
        :param y: Y-coordinate (0-15)
        :param z: Z-coordinate (0-15)
        :return: temperature at given coordinate
        """

    def getCaptureFullTime(self) -> int:
        """
        Get world full time when chunk snapshot was captured
        :return: time in ticks
        """

    def isSectionEmpty(self, sy: int) -> bool:
        """
        Test if section is empty
        :param sy: - section Y coordinate (block Y / 16, world minHeight (inclusive) - world maxHeight (exclusive))
        :return: true if empty, false if not
        """

    def contains(self, block: BlockData) -> bool:
        """
        Tests if this snapshot contains the specified block.
        :param block: block to test
        :return: if the block is contained within
        """

    def contains(self, biome: Biome) -> bool:
        """
        Tests if this chunk contains the specified biome.
        :param biome: biome to test
        :return: if the biome is contained within
        """
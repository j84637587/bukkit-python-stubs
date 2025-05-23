from org.bukkit.block.data import BlockData
from typing import Protocol

class BlockChangeDelegate(Protocol):
    """
    A delegate for handling block changes. This serves as a direct interface
    between generation algorithms in the server implementation and utilizing
    code.
    """

    def setBlockData(self, x: int, y: int, z: int, blockData: BlockData) -> bool:
        """
        Set a block data at the specified coordinates.

        :param x: X coordinate
        :param y: Y coordinate
        :param z: Z coordinate
        :param blockData: Block data
        :return: true if the block was set successfully
        """

    def getBlockData(self, x: int, y: int, z: int) -> BlockData:
        """
        Get the block data at the location.

        :param x: X coordinate
        :param y: Y coordinate
        :param z: Z coordinate
        :return: The block data
        """

    def getHeight(self) -> int:
        """
        Gets the height of the world.

        :return: Height of the world
        """

    def isEmpty(self, x: int, y: int, z: int) -> bool:
        """
        Checks if the specified block is empty (air) or not.

        :param x: X coordinate
        :param y: Y coordinate
        :param z: Z coordinate
        :return: True if the block is considered empty.
        """
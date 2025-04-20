from org.bukkit.block.data import BlockData

class Waterlogged(BlockData):
    """
    'waterlogged' denotes whether this block has fluid in it.
    """

    def is_waterlogged(self) -> bool:
        """
        Gets the value of the 'waterlogged' property.

        Returns:
            bool: the 'waterlogged' value
        """
        ...

    def set_waterlogged(self, waterlogged: bool) -> None:
        """
        Sets the value of the 'waterlogged' property.

        Args:
            waterlogged (bool): the new 'waterlogged' value
        """
        ...
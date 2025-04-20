from org.bukkit.block.data import BlockData

class CaveVinesPlant(BlockData):
    """
    'berries' indicates whether the block has berries.
    """

    def is_berries(self) -> bool:
        """
        Gets the value of the 'berries' property.

        Returns:
            bool: the 'berries' value
        """
        ...

    def set_berries(self, berries: bool) -> None:
        """
        Sets the value of the 'berries' property.

        Args:
            berries (bool): the new 'berries' value
        """
        ...
from org.bukkit.block.data import BlockData

class Snowable(BlockData):
    """
    'snowy' denotes whether this block has a snow covered side and top texture
    (normally because the block above is snow).
    """

    def is_snowy(self) -> bool:
        """
        Gets the value of the 'snowy' property.

        Returns:
            bool: the 'snowy' value
        """
        ...

    def set_snowy(self, snowy: bool) -> None:
        """
        Sets the value of the 'snowy' property.

        Args:
            snowy (bool): the new 'snowy' value
        """
        ...
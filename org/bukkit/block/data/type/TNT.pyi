from org.bukkit.block.data import BlockData

class TNT(BlockData):
    """
    'unstable' indicates whether this TNT will explode on punching.
    """

    def is_unstable(self) -> bool:
        """
        Gets the value of the 'unstable' property.

        Returns:
            bool: the 'unstable' value
        """
        ...

    def set_unstable(self, unstable: bool) -> None:
        """
        Sets the value of the 'unstable' property.

        Args:
            unstable (bool): the new 'unstable' value
        """
        ...
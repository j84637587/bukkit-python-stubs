from org.bukkit.block.data import BlockData

class RespawnAnchor(BlockData):
    """
    'charges' represents the amount of times the anchor may still be used.
    """

    def get_charges(self) -> int:
        """
        Gets the value of the 'charges' property.

        Returns:
            int: the 'charges' value
        """
        ...

    def set_charges(self, charges: int) -> None:
        """
        Sets the value of the 'charges' property.

        Args:
            charges (int): the new 'charges' value
        """
        ...

    def get_maximum_charges(self) -> int:
        """
        Gets the maximum allowed value of the 'charges' property.

        Returns:
            int: the maximum 'charges' value
        """
        ...
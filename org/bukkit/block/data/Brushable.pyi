from org.bukkit.block.data import BlockData

class Brushable(BlockData):
    """
    'dusted' represents how far uncovered by brush the block is.
    """

    def get_dusted(self) -> int:
        """
        Gets the value of the 'dusted' property.

        @return: the 'dusted' value
        """
        ...

    def set_dusted(self, dusted: int) -> None:
        """
        Sets the value of the 'dusted' property.

        @param dusted: the new 'dusted' value
        """
        ...

    def get_maximum_dusted(self) -> int:
        """
        Gets the maximum allowed value of the 'dusted' property.

        @return: the maximum 'dusted' value
        """
        ...
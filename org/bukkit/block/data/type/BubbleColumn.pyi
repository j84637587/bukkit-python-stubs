from org.bukkit.block.data import BlockData

class BubbleColumn(BlockData):
    """
    'drag' indicates whether a force will be applied on entities moving through
    this block.
    """

    def is_drag(self) -> bool:
        """
        Gets the value of the 'drag' property.

        Returns:
            bool: the 'drag' value
        """
        ...

    def set_drag(self, drag: bool) -> None:
        """
        Sets the value of the 'drag' property.

        Args:
            drag (bool): the new 'drag' value
        """
        ...
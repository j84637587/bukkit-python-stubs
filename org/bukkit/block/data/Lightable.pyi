from org.bukkit.block.data import BlockData

class Lightable(BlockData):
    """
    'lit' denotes whether this block (either a redstone torch or furnace) is
    currently lit - that is not burned out.
    """

    def is_lit(self) -> bool:
        """
        Gets the value of the 'lit' property.

        @return: the 'lit' value
        """
        ...

    def set_lit(self, lit: bool) -> None:
        """
        Sets the value of the 'lit' property.

        @param lit: the new 'lit' value
        """
        ...
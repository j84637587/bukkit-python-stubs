from org.bukkit.block.data import BlockData

class Powerable(BlockData):
    """
    'powered' indicates whether this block is in the powered state or not, i.e.
    receiving a redstone current of power > 0.
    """

    def is_powered(self) -> bool:
        """
        Gets the value of the 'powered' property.

        @return: the 'powered' value
        """
        ...

    def set_powered(self, powered: bool) -> None:
        """
        Sets the value of the 'powered' property.

        @param powered: the new 'powered' value
        """
        ...
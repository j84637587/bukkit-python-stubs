from org.bukkit.block.data import BlockData

class Cake(BlockData):
    """
    'bites' represents the amount of bites which have been taken from this slice
    of cake.
    <br>
    A value of 0 indicates that the cake has not been eaten, whilst a value of
    {@link #getMaximumBites()} indicates that it is all gone :(
    """

    def get_bites(self) -> int:
        """
        Gets the value of the 'bites' property.

        @return: the 'bites' value
        """
        ...

    def set_bites(self, bites: int) -> None:
        """
        Sets the value of the 'bites' property.

        @param bites: the new 'bites' value
        """
        ...

    def get_maximum_bites(self) -> int:
        """
        Gets the maximum allowed value of the 'bites' property.

        @return: the maximum 'bites' value
        """
        ...
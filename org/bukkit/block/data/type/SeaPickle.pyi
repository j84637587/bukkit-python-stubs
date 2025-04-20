from org.bukkit.block.data import Waterlogged

class SeaPickle(Waterlogged):
    """
    'pickles' indicates the number of pickles in this block.
    """

    def get_pickles(self) -> int:
        """
        Gets the value of the 'pickles' property.

        @return: the 'pickles' value
        """
        ...

    def set_pickles(self, pickles: int) -> None:
        """
        Sets the value of the 'pickles' property.

        @param pickles: the new 'pickles' value
        """
        ...

    def get_minimum_pickles(self) -> int:
        """
        Gets the minimum allowed value of the 'pickles' property.

        @return: the minimum 'pickles' value
        """
        ...

    def get_maximum_pickles(self) -> int:
        """
        Gets the maximum allowed value of the 'pickles' property.

        @return: the maximum 'pickles' value
        """
        ...
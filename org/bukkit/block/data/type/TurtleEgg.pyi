from org.bukkit.block.data import Hatchable

class TurtleEgg(Hatchable):
    """
    'eggs' is the number of eggs which appear in this block.
    """

    def get_eggs(self) -> int:
        """
        Gets the value of the 'eggs' property.

        Returns:
            int: the 'eggs' value
        """
        ...

    def set_eggs(self, eggs: int) -> None:
        """
        Sets the value of the 'eggs' property.

        Args:
            eggs (int): the new 'eggs' value
        """
        ...

    def get_minimum_eggs(self) -> int:
        """
        Gets the minimum allowed value of the 'eggs' property.

        Returns:
            int: the minimum 'eggs' value
        """
        ...

    def get_maximum_eggs(self) -> int:
        """
        Gets the maximum allowed value of the 'eggs' property.

        Returns:
            int: the maximum 'eggs' value
        """
        ...
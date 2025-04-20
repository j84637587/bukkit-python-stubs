from org.bukkit.block.data import Directional

class Beehive(Directional):
    """'honey_level' represents the amount of honey stored in the hive."""

    def get_honey_level(self) -> int:
        """Gets the value of the 'honey_level' property.

        Returns:
            int: the 'honey_level' value
        """
        ...

    def set_honey_level(self, honey_level: int) -> None:
        """Sets the value of the 'honey_level' property.

        Args:
            honey_level (int): the new 'honey_level' value
        """
        ...

    def get_maximum_honey_level(self) -> int:
        """Gets the maximum allowed value of the 'honey_level' property.

        Returns:
            int: the maximum 'honey_level' value
        """
        ...
from org.bukkit.block.data import Directional

class Piston(Directional):
    """
    'extended' denotes whether the piston head is currently extended or not.
    """

    def is_extended(self) -> bool:
        """
        Gets the value of the 'extended' property.

        Returns:
            bool: the 'extended' value
        """
        ...

    def set_extended(self, extended: bool) -> None:
        """
        Sets the value of the 'extended' property.

        Args:
            extended (bool): the new 'extended' value
        """
        ...
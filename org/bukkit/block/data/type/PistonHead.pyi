from org.bukkit.block.data.type import TechnicalPiston

class PistonHead(TechnicalPiston):
    """
    'short' denotes this piston head is shorter than the usual amount because it
    is currently retracting.
    """

    def is_short(self) -> bool:
        """
        Gets the value of the 'short' property.

        Returns:
            bool: the 'short' value
        """
        ...

    def set_short(self, _short: bool) -> None:
        """
        Sets the value of the 'short' property.

        Args:
            _short (bool): the new 'short' value
        """
        ...
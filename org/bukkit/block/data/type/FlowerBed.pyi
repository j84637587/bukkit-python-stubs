from org.bukkit.block.data import Directional

class FlowerBed(Directional):
    """
    'flower_amount' represents the number of petals.
    """

    def get_flower_amount(self) -> int:
        """
        Gets the value of the 'flower_amount' property.

        @return: the 'flower_amount' value
        """
        ...

    def set_flower_amount(self, flower_amount: int) -> None:
        """
        Sets the value of the 'flower_amount' property.

        @param flower_amount: the new 'flower_amount' value
        """
        ...

    def get_maximum_flower_amount(self) -> int:
        """
        Gets the maximum allowed value of the 'flower_amount' property.

        @return: the maximum 'flower_amount' value
        """
        ...
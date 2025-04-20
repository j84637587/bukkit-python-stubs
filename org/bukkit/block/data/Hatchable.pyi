from org.bukkit.block.data import BlockData

class Hatchable(BlockData):
    """
    'hatch' is the number of entities which may hatch from these eggs.
    """

    def get_hatch(self) -> int:
        """
        Gets the value of the 'hatch' property.

        :return: the 'hatch' value
        """
        ...

    def set_hatch(self, hatch: int) -> None:
        """
        Sets the value of the 'hatch' property.

        :param hatch: the new 'hatch' value
        """
        ...

    def get_maximum_hatch(self) -> int:
        """
        Gets the maximum allowed value of the 'hatch' property.

        :return: the maximum 'hatch' value
        """
        ...
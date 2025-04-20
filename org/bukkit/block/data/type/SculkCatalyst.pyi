from org.bukkit.block.data import BlockData

class SculkCatalyst(BlockData):
    """
    'bloom' indicates whether the sculk catalyst is actively spreading the sculk
    or not.
    """

    def is_bloom(self) -> bool:
        """
        Gets the value of the 'bloom' property.

        @return: the 'bloom' value
        """
        ...

    def set_bloom(self, bloom: bool) -> None:
        """
        Sets the value of the 'bloom' property.

        @param bloom: the new 'bloom' value
        """
        ...
from org.bukkit.block.data import BlockData

class Snow(BlockData):
    """
    'layers' represents the amount of layers of snow which are present in this
    block.
    <br>
    May not be lower than {@link #getMinimumLayers()} or higher than
    {@link #getMaximumLayers()}.
    """

    def get_layers(self) -> int:
        """
        Gets the value of the 'layers' property.

        @return: the 'layers' value
        """
        ...

    def set_layers(self, layers: int) -> None:
        """
        Sets the value of the 'layers' property.

        @param layers: the new 'layers' value
        """
        ...

    def get_minimum_layers(self) -> int:
        """
        Gets the minimum allowed value of the 'layers' property.

        @return: the minimum 'layers' value
        """
        ...

    def get_maximum_layers(self) -> int:
        """
        Gets the maximum allowed value of the 'layers' property.

        @return: the maximum 'layers' value
        """
        ...
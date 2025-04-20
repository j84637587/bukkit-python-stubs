from org.bukkit.block.data import BlockData

class Farmland(BlockData):
    """
    The 'moisture' level of farmland indicates how close it is to a water source
    (if any).
    <br>
    A higher moisture level leads, to faster growth of crops on this block, but
    cannot be higher than {@link #getMaximumMoisture()}.
    """

    def get_moisture(self) -> int:
        """
        Gets the value of the 'moisture' property.

        @return: the 'moisture' value
        """
        ...

    def set_moisture(self, moisture: int) -> None:
        """
        Sets the value of the 'moisture' property.

        @param moisture: the new 'moisture' value
        """
        ...

    def get_maximum_moisture(self) -> int:
        """
        Gets the maximum allowed value of the 'moisture' property.

        @return: the maximum 'moisture' value
        """
        ...
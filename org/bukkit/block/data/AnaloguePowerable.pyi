from typing import Protocol

class BlockData(Protocol):
    pass

class AnaloguePowerable(BlockData, Protocol):
    """
    'power' represents the redstone power level currently being emitted or
    transmitted via this block.
    <br>
    May not be over 9000 or {@link #getMaximumPower()} (usually 15).
    """

    def get_power(self) -> int:
        """
        Gets the value of the 'power' property.

        Returns:
            int: the 'power' value
        """
        ...

    def set_power(self, power: int) -> None:
        """
        Sets the value of the 'power' property.

        Args:
            power (int): the new 'power' value
        """
        ...

    def get_maximum_power(self) -> int:
        """
        Gets the maximum allowed value of the 'power' property.

        Returns:
            int: the maximum 'power' value
        """
        ...
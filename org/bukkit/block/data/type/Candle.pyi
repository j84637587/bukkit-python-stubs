from org.bukkit.block.data import Lightable
from org.bukkit.block.data import Waterlogged

class Candle(Lightable, Waterlogged):
    """'candles' represents the number of candles which are present."""

    def get_candles(self) -> int:
        """Gets the value of the 'candles' property.

        Returns:
            int: the 'candles' value
        """
        ...

    def set_candles(self, candles: int) -> None:
        """Sets the value of the 'candles' property.

        Args:
            candles (int): the new 'candles' value
        """
        ...

    def get_maximum_candles(self) -> int:
        """Gets the maximum allowed value of the 'candles' property.

        Returns:
            int: the maximum 'candles' value
        """
        ...
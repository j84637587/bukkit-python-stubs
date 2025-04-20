from typing import Literal, Protocol

class BlockData(Protocol):
    pass

class Bisected(BlockData, Protocol):
    """
    'half' denotes which half of a two block tall material this block is.
    <br>
    In game it may be referred to as either (top, bottom) or (upper, lower).
    """

    def get_half(self) -> Literal['TOP', 'BOTTOM']:
        """
        Gets the value of the 'half' property.

        Returns:
            The 'half' value.
        """
        ...

    def set_half(self, half: Literal['TOP', 'BOTTOM']) -> None:
        """
        Sets the value of the 'half' property.

        Args:
            half: The new 'half' value.
        """
        ...

class Half:
    """
    The half of a vertically bisected block.
    """
    TOP: Literal['TOP'] = 'TOP'
    BOTTOM: Literal['BOTTOM'] = 'BOTTOM'
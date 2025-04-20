from typing import Protocol

class BlockData(Protocol):
    """Placeholder for BlockData interface."""

class Openable(BlockData, Protocol):
    """
    'open' denotes whether this block is currently opened.
    """

    def is_open(self) -> bool:
        """
        Gets the value of the 'open' property.

        Returns:
            bool: the 'open' value
        """
        ...

    def set_open(self, open: bool) -> None:
        """
        Sets the value of the 'open' property.

        Args:
            open (bool): the new 'open' value
        """
        ...
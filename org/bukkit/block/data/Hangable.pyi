from typing import Protocol

class BlockData(Protocol):
    """Protocol for BlockData."""

class Hangable(BlockData, Protocol):
    """
    'hanging' denotes whether the lantern is hanging from a block.
    """

    def is_hanging(self) -> bool:
        """
        Gets the value of the 'hanging' property.

        Returns:
            bool: the 'hanging' value
        """
        ...

    def set_hanging(self, hanging: bool) -> None:
        """
        Sets the value of the 'hanging' property.

        Args:
            hanging (bool): the new 'hanging' value
        """
        ...
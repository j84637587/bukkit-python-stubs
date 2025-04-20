from typing import Literal
from org.bukkit.block.data import BlockData
from typing import Protocol

class Mode:
    """
    The mode in which a comparator will operate in.
    """
    START: Literal['START']
    LOG: Literal['LOG']
    FAIL: Literal['FAIL']
    ACCEPT: Literal['ACCEPT']


class TestBlock(Protocol):
    """
    'mode' indicates what mode this test block is in.
    """

    def get_mode(self) -> Mode:
        """
        Gets the value of the 'mode' property.

        Returns:
            Mode: the 'mode' value
        """
        ...

    def set_mode(self, mode: Mode) -> None:
        """
        Sets the value of the 'mode' property.

        Args:
            mode (Mode): the new 'mode' value
        """
        ...
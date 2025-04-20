from org.bukkit.block.data import BlockData
from typing import Literal

class StructureBlock(BlockData):
    """
    'mode' represents the different modes in which this structure block may
    operate.
    """

    def get_mode(self) -> 'Mode':
        """
        Gets the value of the 'mode' property.

        Returns:
            Mode: the 'mode' value
        """
        ...

    def set_mode(self, mode: 'Mode') -> None:
        """
        Sets the value of the 'mode' property.

        Args:
            mode (Mode): the new 'mode' value
        """
        ...

class Mode:
    """
    Operating mode of a structure block.
    """
    SAVE: Literal['SAVE'] = 'SAVE'
    LOAD: Literal['LOAD'] = 'LOAD'
    CORNER: Literal['CORNER'] = 'CORNER'
    DATA: Literal['DATA'] = 'DATA'
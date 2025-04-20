from org.bukkit.block.data import BlockData
from org.jetbrains.annotations import ApiStatus

"""
'tip' indicates whether this block is a tip.
"""

class HangingMoss(BlockData):
    """
    Gets the value of the 'tip' property.

    Returns:
        bool: the 'tip' value
    """

    def is_tip(self) -> bool: ...

    """
    Sets the value of the 'tip' property.

    Args:
        tip (bool): the new 'tip' value
    """
    def set_tip(self, tip: bool) -> None: ...

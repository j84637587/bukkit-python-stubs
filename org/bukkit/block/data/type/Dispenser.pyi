from org.bukkit.block.data import Directional
from org.bukkit.block.data import Powerable

"""
Similar to `Powerable`, 'triggered' indicates whether or not the
dispenser is currently activated.
"""
class Dispenser(Directional):
    """
    Gets the value of the 'triggered' property.

    Returns:
        bool: the 'triggered' value
    """
    def is_triggered(self) -> bool: ...

    """
    Sets the value of the 'triggered' property.

    Args:
        triggered (bool): the new 'triggered' value
    """
    def set_triggered(self, triggered: bool) -> None: ...
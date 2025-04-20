from org.bukkit.block.data import Attachable
from org.bukkit.block.data import MultipleFacing
from org.bukkit.block.data import Powerable
from typing import Protocol

class Tripwire(Attachable, MultipleFacing, Powerable, Protocol):
    """
    'disarmed' denotes that the tripwire was broken with shears and will not
    subsequently produce a current when destroyed.
    """

    def is_disarmed(self) -> bool:
        """
        Gets the value of the 'disarmed' property.

        Returns:
            bool: the 'disarmed' value
        """
        ...

    def set_disarmed(self, disarmed: bool) -> None:
        """
        Sets the value of the 'disarmed' property.

        Args:
            disarmed (bool): the new 'disarmed' value
        """
        ...
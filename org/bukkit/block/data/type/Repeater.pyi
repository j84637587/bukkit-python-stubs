from org.bukkit.block.data import Directional
from org.bukkit.block.data import Powerable

class Repeater(Directional, Powerable):
    """
    'delay' is the propagation delay of a repeater, i.e. how many ticks before it
    will be activated from a current change and propagate it to the next block.
    <br>
    Delay may not be lower than {@link #getMinimumDelay()} or higher than
    {@link #getMaximumDelay()}.
    <br>
    'locked' denotes whether the repeater is in the locked state or not.
    <br>
    A locked repeater will not change its output until it is unlocked. In game, a
    locked repeater is created by having a constant current perpendicularly
    entering the block.
    """

    def get_delay(self) -> int:
        """
        Gets the value of the 'delay' property.

        @return: the 'delay' value
        """
        ...

    def set_delay(self, delay: int) -> None:
        """
        Sets the value of the 'delay' property.

        @param delay: the new 'delay' value
        """
        ...

    def get_minimum_delay(self) -> int:
        """
        Gets the minimum allowed value of the 'delay' property.

        @return: the minimum 'delay' value
        """
        ...

    def get_maximum_delay(self) -> int:
        """
        Gets the maximum allowed value of the 'delay' property.

        @return: the maximum 'delay' value
        """
        ...

    def is_locked(self) -> bool:
        """
        Gets the value of the 'locked' property.

        @return: the 'locked' value
        """
        ...

    def set_locked(self, locked: bool) -> None:
        """
        Sets the value of the 'locked' property.

        @param locked: the new 'locked' value
        """
        ...
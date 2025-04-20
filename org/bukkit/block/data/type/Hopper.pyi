from org.bukkit.block.data import Directional
from org.bukkit.block.data import Powerable

class Hopper(Directional):
    """
    Similar to {@link Powerable}, 'enabled' indicates whether or not the hopper
    is currently activated.
    <br>
    Unlike most other blocks, a hopper is only enabled when it is <b>not</b>
    receiving any power.
    """

    def is_enabled(self) -> bool:
        """
        Gets the value of the 'enabled' property.

        @return: the 'enabled' value
        """
        ...

    def set_enabled(self, enabled: bool) -> None:
        """
        Sets the value of the 'enabled' property.

        @param enabled: the new 'enabled' value
        """
        ...
from org.bukkit.entity import Squid

class GlowSquid(Squid):
    """
    A Glow Squid.
    """

    def get_dark_ticks_remaining(self) -> int:
        """
        Get the number of dark ticks remaining for this squid.

        Bravo Six will go dark for 100 ticks (5 seconds) if damaged.

        @return: dark ticks remaining
        """
        ...

    def set_dark_ticks_remaining(self, dark_ticks_remaining: int) -> None:
        """
        Sets the number of dark ticks remaining for this squid.

        Bravo Six will go dark for 100 ticks (5 seconds) if damaged.

        @param dark_ticks_remaining: dark ticks remaining
        """
        ...
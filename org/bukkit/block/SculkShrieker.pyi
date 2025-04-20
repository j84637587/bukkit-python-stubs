from typing import Optional
from org.bukkit.entity import Player

class SculkShrieker(TileState):
    """
    Represents a captured state of a sculk shrieker.
    """

    def get_warning_level(self) -> int:
        """
        Gets the most recent warning level of this block.

        When the warning level reaches 4, the shrieker will attempt to spawn a
        Warden.

        @return: current warning level
        """
        ...

    def set_warning_level(self, level: int) -> None:
        """
        Sets the most recent warning level of this block.

        When the warning level reaches 4, the shrieker will attempt to spawn a
        Warden.

        @param level: new warning level
        """
        ...

    def try_shriek(self, player: Optional[Player]) -> None:
        """
        Simulates a player causing a vibration.

        @param player: the player that "caused" the shriek
        """
        ...
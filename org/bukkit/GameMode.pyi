from typing import Dict, Optional

class GameMode:
    """
    Represents the various type of game modes that HumanEntitys may have
    """
    CREATIVE: int = 1
    """
    Creative mode may fly, build instantly, become invulnerable and create free items.
    """
    SURVIVAL: int = 0
    """
    Survival mode is the "normal" gameplay type, with no special features.
    """
    ADVENTURE: int = 2
    """
    Adventure mode cannot break blocks without the correct tools.
    """
    SPECTATOR: int = 3
    """
    Spectator mode cannot interact with the world in anyway and is invisible to normal players. 
    This grants the player the ability to no-clip through the world.
    """
    value: int
    BY_ID: Dict[int, 'GameMode']

    def __init__(self, value: int) -> None:
        ...

    def getValue(self) -> int:
        """
        Gets the mode value associated with this GameMode

        :return: An integer value of this gamemode
        :deprecated: Magic value
        """
        ...

    @staticmethod
    def getByValue(value: int) -> Optional['GameMode']:
        """
        Gets the GameMode represented by the specified value

        :param value: Value to check
        :return: Associative GameMode with the given value, or null if it doesn't exist
        :deprecated: Magic value
        """
        ...
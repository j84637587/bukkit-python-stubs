from org.bukkit.entity import Player
from org.jetbrains.annotations import ApiStatus
from enum import Enum

class DamageScaling(Enum):
    """
    A means of damage scaling with respect to the server's difficulty.
    """
    NEVER = 0
    """
    Damage is not scaled.
    """
    WHEN_CAUSED_BY_LIVING_NON_PLAYER = 1
    """
    Damage is scaled only when the
    causing entity is not a Player.
    """
    ALWAYS = 2
    """
    Damage is always scaled.
    """
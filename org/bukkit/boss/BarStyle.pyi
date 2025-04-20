# org/bukkit/boss/BarStyle.pyi

from enum import Enum

class BarStyle(Enum):
    """
    Makes the boss bar solid (no segments)
    """
    SOLID: BarStyle

    """
    Splits the boss bar into 6 segments
    """
    SEGMENTED_6: BarStyle

    """
    Splits the boss bar into 10 segments
    """
    SEGMENTED_10: BarStyle

    """
    Splits the boss bar into 12 segments
    """
    SEGMENTED_12: BarStyle

    """
    Splits the boss bar into 20 segments
    """
    SEGMENTED_20: BarStyle
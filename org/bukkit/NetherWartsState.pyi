from enum import Enum

class NetherWartsState(Enum):
    """
    Enum representing the growth stages of Nether Warts.
    """
    SEEDED = 0
    """
    State when first seeded
    """
    STAGE_ONE = 1
    """
    First growth stage
    """
    STAGE_TWO = 2
    """
    Second growth stage
    """
    RIPE = 3
    """
    Ready to harvest
    """
# org/bukkit/scoreboard/RenderType.pyi

from enum import Enum

class RenderType(Enum):
    """
    Controls the way in which an {@link Objective} is rendered client side.
    """
    
    INTEGER: RenderType
    """
    Display integer value.
    """
    
    HEARTS: RenderType
    """
    Display number of hearts corresponding to value.
    """
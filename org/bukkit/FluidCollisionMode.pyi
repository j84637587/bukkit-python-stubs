from enum import Enum

class FluidCollisionMode(Enum):
    """
    Determines the collision behavior when fluids get hit during ray tracing.
    """
    NEVER = 1
    """
    Ignore fluids.
    """
    SOURCE_ONLY = 2
    """
    Only collide with source fluid blocks.
    """
    ALWAYS = 3
    """
    Collide with all fluids.
    """
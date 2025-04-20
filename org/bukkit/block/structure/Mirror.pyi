from enum import Enum

class Mirror(Enum):
    """
    Represents how a :class:`org.bukkit.block.Structure` can be mirrored upon
    being loaded.
    """
    NONE = 0
    """
    No mirroring.
    <br>
    Positive X to Positive Z
    """
    LEFT_RIGHT = 1
    """
    Structure is mirrored left to right.
    <br>
    Similar to looking in a mirror. Positive X to Negative Z
    """
    FRONT_BACK = 2
    """
    Structure is mirrored front to back.
    <br>
    Positive Z to Negative X
    """
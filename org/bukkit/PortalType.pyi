from enum import Enum

class PortalType(Enum):
    """
    Represents various types of portals that can be made in a world.
    """
    NETHER = 1
    """
    This is a Nether portal, made of obsidian.
    """
    ENDER = 2
    """
    This is an Ender portal.
    """
    CUSTOM = 3
    """
    This is a custom Plugin portal.
    """
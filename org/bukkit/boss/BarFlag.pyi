from enum import Enum

class BarFlag(Enum):
    """
    Enum representing various bar flags.
    """

    DARKEN_SKY = ...
    """
    Darkens the sky like during fighting a wither.
    """

    PLAY_BOSS_MUSIC = ...
    """
    Tells the client to play the Ender Dragon boss music.
    """

    CREATE_FOG = ...
    """
    Creates fog around the world.
    """
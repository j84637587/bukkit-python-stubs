from enum import Enum

class SoundCategory(Enum):
    """
    An Enum of categories for sounds.
    """
    MASTER = 1
    MUSIC = 2
    RECORDS = 3
    WEATHER = 4
    BLOCKS = 5
    HOSTILE = 6
    NEUTRAL = 7
    PLAYERS = 8
    AMBIENT = 9
    VOICE = 10
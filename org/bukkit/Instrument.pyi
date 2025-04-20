from typing import Optional, Dict, Type
from org.bukkit import Sound

class Instrument:
    """
    Enum class representing different types of instruments.
    """

    PIANO: 'Instrument'
    BASS_DRUM: 'Instrument'
    SNARE_DRUM: 'Instrument'
    STICKS: 'Instrument'
    BASS_GUITAR: 'Instrument'
    FLUTE: 'Instrument'
    BELL: 'Instrument'
    GUITAR: 'Instrument'
    CHIME: 'Instrument'
    XYLOPHONE: 'Instrument'
    IRON_XYLOPHONE: 'Instrument'
    COW_BELL: 'Instrument'
    DIDGERIDOO: 'Instrument'
    BIT: 'Instrument'
    BANJO: 'Instrument'
    PLING: 'Instrument'
    ZOMBIE: 'Instrument'
    SKELETON: 'Instrument'
    CREEPER: 'Instrument'
    DRAGON: 'Instrument'
    WITHER_SKELETON: 'Instrument'
    PIGLIN: 'Instrument'
    CUSTOM_HEAD: 'Instrument'

    type: bytes
    sound: Sound
    BY_DATA: Dict[bytes, 'Instrument']

    def __init__(self, type: bytes, sound: Sound) -> None:
        ...

    def getSound(self) -> Optional[Sound]:
        """
        Gets the sound associated with this instrument.
        Will be null for Instrument.CUSTOM_HEAD
        """
        ...

    def getType(self) -> bytes:
        """
        The type ID of this instrument.
        Deprecated since version 1.6.2
        """
        ...

    @staticmethod
    def getByType(type: bytes) -> Optional['Instrument']:
        """
        Get an instrument by its type ID.
        Deprecated since version 1.6.2
        """
        ...
from typing import Collection
from org.bukkit import Keyed, RegistryAware, Sound, NamespacedKey
from com.google.common.collect import Lists
from java.util import Collections

class MusicInstrument(Keyed, RegistryAware):
    """
    Python stub for MusicInstrument class
    """

    PONDER_GOAT_HORN: 'MusicInstrument'
    SING_GOAT_HORN: 'MusicInstrument'
    SEEK_GOAT_HORN: 'MusicInstrument'
    FEEL_GOAT_HORN: 'MusicInstrument'
    ADMIRE_GOAT_HORN: 'MusicInstrument'
    CALL_GOAT_HORN: 'MusicInstrument'
    YEARN_GOAT_HORN: 'MusicInstrument'
    DREAM_GOAT_HORN: 'MusicInstrument'

    def getDuration(self) -> float:
        """
        Gets how long the use duration is for the instrument.
        """
        ...

    def getRange(self) -> float:
        """
        Gets the range of the sound.
        """
        ...

    def getDescription(self) -> str:
        """
        Gets the description of this instrument.
        """
        ...

    def getSoundEvent(self) -> Sound:
        """
        Gets the sound/sound-event for this instrument.
        """
        ...

    def getKey(self) -> NamespacedKey:
        """
        {@inheritDoc}
        @see #getKeyOrThrow()
        @see #isRegistered()
        @deprecated A key might not always be present, use {@link #getKeyOrThrow()} instead.
        """
        ...

    @staticmethod
    def getByKey(namespacedKey: NamespacedKey) -> 'MusicInstrument':
        """
        Returns a {@link MusicInstrument} by a {@link NamespacedKey}.
        @deprecated Use {@link Registry#get(NamespacedKey)} instead.
        """
        ...

    @staticmethod
    def values() -> Collection['MusicInstrument']:
        """
        Returns all known MusicInstruments.
        @deprecated use {@link Registry#iterator()}.
        """
        ...

    @staticmethod
    def getInstrument(key: str) -> 'MusicInstrument':
        """
        Returns a MusicInstrument by a key.
        """
        ...
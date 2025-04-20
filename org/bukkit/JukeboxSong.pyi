from typing import Any
from org.bukkit import Keyed, Translatable, RegistryAware
from org.jetbrains.annotations import ApiStatus, NotNull

class JukeboxSong(Keyed, Translatable, RegistryAware):
    """
    Represents a song which may play in a Jukebox.
    """
    THIRTEEN: 'JukeboxSong'
    CAT: 'JukeboxSong'
    BLOCKS: 'JukeboxSong'
    CHIRP: 'JukeboxSong'
    FAR: 'JukeboxSong'
    MALL: 'JukeboxSong'
    MELLOHI: 'JukeboxSong'
    STAL: 'JukeboxSong'
    STRAD: 'JukeboxSong'
    WARD: 'JukeboxSong'
    ELEVEN: 'JukeboxSong'
    WAIT: 'JukeboxSong'
    PIGSTEP: 'JukeboxSong'
    OTHERSIDE: 'JukeboxSong'
    FIVE: 'JukeboxSong'
    RELIC: 'JukeboxSong'
    PRECIPICE: 'JukeboxSong'
    CREATOR: 'JukeboxSong'
    CREATOR_MUSIC_BOX: 'JukeboxSong'

    @staticmethod
    def get(key: str) -> 'JukeboxSong': ...

    def getKey(self) -> Any: ...
from org.bukkit import JukeboxSong
from org.bukkit import NamespacedKey
from org.bukkit.configuration.serialization import ConfigurationSerializable
from typing import Optional
from org.jetbrains.annotations import ApiStatus, NotNull, Nullable

"""
Represents a component which can be inserted into a jukebox.
"""

class JukeboxPlayableComponent(ConfigurationSerializable):
    """
    Gets the song assigned to this component.

    @return song, or None if the song does not exist on the server
    """

    def get_song(self) -> Optional[JukeboxSong]: ...

    """
    Gets the key of the song assigned to this component.

    @return the song key
    """
    def get_song_key(self) -> Optional[NamespacedKey]: ...

    """
    Sets the song assigned to this component.

    @param song the song
    """
    def set_song(self, song: NotNull[JukeboxSong]) -> None: ...

    """
    Sets the key of the song assigned to this component.

    @param song the song key
    """
    def set_song_key(self, song: NotNull[NamespacedKey]) -> None: ...

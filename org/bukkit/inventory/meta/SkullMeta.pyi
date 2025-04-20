from org.bukkit import NamespacedKey
from org.bukkit import OfflinePlayer
from org.bukkit.profile import PlayerProfile
from typing import Optional

class SkullMeta(ItemMeta):
    """
    Represents a skull that can have an owner.
    """

    def get_owner(self) -> Optional[str]:
        """
        Gets the owner of the skull.

        Returns:
            the owner if the skull
        """
        ...

    def has_owner(self) -> bool:
        """
        Checks to see if the skull has an owner.

        Returns:
            true if the skull has an owner
        """
        ...

    def set_owner(self, owner: Optional[str]) -> bool:
        """
        Sets the owner of the skull.

        Args:
            owner: the new owner of the skull

        Returns:
            true if the owner was successfully set
        """
        ...

    def get_owning_player(self) -> Optional[OfflinePlayer]:
        """
        Gets the owner of the skull.

        Returns:
            the owner if the skull
        """
        ...

    def set_owning_player(self, owner: Optional[OfflinePlayer]) -> bool:
        """
        Sets the owner of the skull.
        Plugins should check that hasOwner() returns true before calling this plugin.

        Args:
            owner: the new owner of the skull

        Returns:
            true if the owner was successfully set
        """
        ...

    def get_owner_profile(self) -> Optional[PlayerProfile]:
        """
        Gets the profile of the player who owns the skull. This player profile
        may appear as the texture depending on skull type.

        Returns:
            the profile of the owning player
        """
        ...

    def set_owner_profile(self, profile: Optional[PlayerProfile]) -> None:
        """
        Sets the profile of the player who owns the skull. This player profile
        may appear as the texture depending on skull type.
        The profile must contain both a unique id and a skin texture. If either
        of these is missing, the profile must contain a name by which the server
        will then attempt to look up the unique id and skin texture.

        Args:
            profile: the profile of the owning player

        Raises:
            IllegalArgumentException: if the profile does not contain the
            necessary information
        """
        ...

    def set_note_block_sound(self, note_block_sound: Optional[NamespacedKey]) -> None:
        """
        Sets the sound to play if the skull is placed on a note block.
        Note: This only works for player heads. For other heads,
        see org.bukkit.Instrument.

        Args:
            note_block_sound: the key of the sound to be played, or null
        """
        ...

    def get_note_block_sound(self) -> Optional[NamespacedKey]:
        """
        Gets the sound to play if the skull is placed on a note block.
        Note: This only works for player heads. For other heads,
        see org.bukkit.Instrument.

        Returns:
            the key of the sound, or null
        """
        ...

    def clone(self) -> 'SkullMeta':
        ...
from typing import Optional
from org.bukkit import Material
from .namespaced_key import NamespacedKey
from .offline_player import OfflinePlayer
from .skull_type import SkullType
import org.bukkit.block_data import BlockData
from .player_profile import PlayerProfile
from .tile_state import TileState
import org.bukkit.block_face import BlockFace

class Skull(TileState):
    """
    Represents a captured state of a skull block.
    """

    def has_owner(self) -> bool:
        """
        Checks to see if the skull has an owner.

        :return: true if the skull has an owner
        """
        ...

    @Deprecated(since="1.9.4")
    def get_owner(self) -> Optional[str]:
        """
        Gets the owner of the skull, if one exists.

        :return: the owner of the skull or null if the skull does not have an owner
        """
        ...

    @Deprecated(since="1.9.4")
    def set_owner(self, name: Optional[str]) -> bool:
        """
        Sets the owner of the skull.

        Involves a potentially blocking web request to acquire the profile data for
        the provided name.

        :param name: the new owner of the skull
        :return: true if the owner was successfully set
        """
        ...

    def get_owning_player(self) -> Optional[OfflinePlayer]:
        """
        Get the player which owns the skull. This player may appear as the
        texture depending on skull type.

        :return: owning player
        """
        ...

    def set_owning_player(self, player: OfflinePlayer) -> None:
        """
        Set the player which owns the skull. This player may appear as the
        texture depending on skull type.

        :param player: the owning player
        """
        ...

    def get_owner_profile(self) -> Optional[PlayerProfile]:
        """
        Gets the profile of the player who owns the skull. This player profile
        may appear as the texture depending on skull type.

        :return: the profile of the owning player
        """
        ...

    def set_owner_profile(self, profile: Optional[PlayerProfile]) -> None:
        """
        Sets the profile of the player who owns the skull. This player profile
        may appear as the texture depending on skull type.

        The profile must contain both a unique id and a skin texture. If either
        of these is missing, the profile must contain a name by which the server
        will then attempt to look up the unique id and skin texture.

        :param profile: the profile of the owning player
        :raises IllegalArgumentException: if the profile does not contain the
        necessary information
        """
        ...

    def get_note_block_sound(self) -> Optional[NamespacedKey]:
        """
        Gets the sound to play if the skull is placed on a note block.

        Note: This only works for player heads. For other heads,
        see {@link org.bukkit.Instrument}.

        :return: the key of the sound, or null
        """
        ...

    def set_note_block_sound(self, note_block_sound: Optional[NamespacedKey]) -> None:
        """
        Sets the sound to play if the skull is placed on a note block.

        Note: This only works for player heads. For other heads,
        see {@link org.bukkit.Instrument}.

        :param note_block_sound: the key of the sound to be played, or null
        """
        ...

    @Deprecated(since="1.13")
    def get_rotation(self) -> BlockFace:
        """
        Gets the rotation of the skull in the world (or facing direction if this
        is a wall mounted skull).

        :return: the rotation of the skull
        """
        ...

    @Deprecated(since="1.13")
    def set_rotation(self, rotation: BlockFace) -> None:
        """
        Sets the rotation of the skull in the world (or facing direction if this
        is a wall mounted skull).

        :param rotation: the rotation of the skull
        """
        ...

    @Deprecated(since="1.13")
    def get_skull_type(self) -> SkullType:
        """
        Gets the type of skull.

        :return: the type of skull
        """
        ...

    @Deprecated(since="1.13")
    def set_skull_type(self, skull_type: SkullType) -> None:
        """
        Sets the type of skull.

        :param skull_type: the type of skull
        """
        ...
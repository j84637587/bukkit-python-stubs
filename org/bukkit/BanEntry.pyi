from typing import Optional, TypeVar
from datetime import datetime

T = TypeVar('T')

class BanEntry:
    """
    A single entry from a ban list. This may represent either a player ban or
    an IP ban.

    Ban entries include the following properties:
    - Target Profile / IP Address: The target profile or IP address
    - Creation Date: The creation date of the ban
    - Source: The source of the ban, such as a player, console, plugin, etc
    - Expiration Date: The expiration date of the ban
    - Reason: The reason for the ban

    Unsaved information is not automatically written to the implementation's
    ban list, instead, the save() method must be called to write the
    changes to the ban list. If this ban entry has expired (such as from an
    unban) and is no longer found in the list, the save() call will
    re-add it to the list, therefore banning the victim specified.

    Likewise, changes to the associated BanList or other entries may or
    may not be reflected in this entry.
    """

    def getTarget(self) -> str:
        """
        Gets the target involved. This may be in the form of an IP or a player
        name.

        @return the target name or IP address
        @deprecated See getBanTarget()
        """
        ...

    def getBanTarget(self) -> T:
        """
        Gets the target involved.

        @return the target profile or IP address
        """
        ...

    def getCreated(self) -> datetime:
        """
        Gets the date this ban entry was created.

        @return the creation date
        """
        ...

    def setCreated(self, created: datetime) -> None:
        """
        Sets the date this ban entry was created.

        @param created the new created date, cannot be null
        @see save() saving changes
        """
        ...

    def getSource(self) -> str:
        """
        Gets the source of this ban.
        Note: A source is considered any String, although this is generally a
        player name.

        @return the source of the ban
        """
        ...

    def setSource(self, source: str) -> None:
        """
        Sets the source of this ban.
        Note: A source is considered any String, although this is generally a
        player name.

        @param source the new source where null values become empty strings
        @see save() saving changes
        """
        ...

    def getExpiration(self) -> Optional[datetime]:
        """
        Gets the date this ban expires on, or null for no defined end date.

        @return the expiration date
        """
        ...

    def setExpiration(self, expiration: Optional[datetime]) -> None:
        """
        Sets the date this ban expires on. Null values are considered
        "infinite" bans.

        @param expiration the new expiration date, or null to indicate an
        eternity
        @see save() saving changes
        """
        ...

    def getReason(self) -> Optional[str]:
        """
        Gets the reason for this ban.

        @return the ban reason, or null if not set
        """
        ...

    def setReason(self, reason: Optional[str]) -> None:
        """
        Sets the reason for this ban. Reasons must not be null.

        @param reason the new reason, null values assume the implementation
        default
        @see save() saving changes
        """
        ...

    def save(self) -> None:
        """
        Saves the ban entry, overwriting any previous data in the ban list.
        Saving the ban entry of an unbanned player will cause the player to be
        banned once again.
        """
        ...

    def remove(self) -> None:
        """
        Removes this ban entry from the appropriate ban list.
        """
        ...
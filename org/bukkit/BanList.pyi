from typing import Optional, Set, TypeVar
from datetime import datetime, timedelta

T = TypeVar('T')

class Type:
    """
    Represents a ban-type that a BanList may track.
    """
    NAME = 0  # deprecated in favor of PROFILE
    IP = 1
    PROFILE = 2

class BanEntry:
    """
    A ban entry in the BanList.
    """
    pass

class BanList:
    """
    A ban list, containing bans of some Type.
    """

    def getBanEntry(self, target: str) -> Optional[BanEntry[T]]:
        """
        Gets a BanEntry by target.
        """
        pass

    def getBanEntry(self, target: T) -> Optional[BanEntry[T]]:
        """
        Gets a BanEntry by target.
        """
        pass

    def addBan(self, target: str, reason: Optional[str], expires: Optional[datetime], source: Optional[str]) -> Optional[BanEntry[T]]:
        """
        Adds a ban to this list. If a previous ban exists, this will update the previous entry.
        """
        pass

    def addBan(self, target: T, reason: Optional[str], expires: Optional[datetime], source: Optional[str]) -> Optional[BanEntry[T]]:
        """
        Adds a ban to this list. If a previous ban exists, this will update the previous entry.
        """
        pass

    def addBan(self, target: T, reason: Optional[str], expires: Optional[timedelta], source: Optional[str]) -> Optional[BanEntry[T]]:
        """
        Adds a ban to this list. If a previous ban exists, this will update the previous entry.
        """
        pass

    def getBanEntries(self) -> Set[BanEntry]:
        """
        Gets a set containing every BanEntry in this list.
        """
        pass

    def getEntries(self) -> Set[BanEntry[T]]:
        """
        Gets a set containing every BanEntry in this list.
        """
        pass

    def isBanned(self, target: T) -> bool:
        """
        Gets if a BanEntry exists for the target, indicating an active ban status.
        """
        pass

    def isBanned(self, target: str) -> bool:
        """
        Gets if a BanEntry exists for the target, indicating an active ban status.
        """
        pass

    def pardon(self, target: T) -> None:
        """
        Removes the specified target from this list, therefore indicating a "not banned" status.
        """
        pass

    def pardon(self, target: str) -> None:
        """
        Removes the specified target from this list, therefore indicating a "not banned" status.
        """
        pass
from typing import Optional
from datetime import date
from .ban_entry import BanEntry
from .ban_list import BanList
from .player_profile import PlayerProfile

class ProfileBanList(BanList[PlayerProfile]):
    """
    A {@link BanList} targeting player profile bans.
    """

    def add_ban(
        self,
        target: PlayerProfile,
        reason: Optional[str],
        expires: Optional[date],
        source: Optional[str]
    ) -> Optional[BanEntry[PlayerProfile]]:
        """
        {@inheritDoc}

        :param target: the target of the ban
        :param reason: reason for the ban, None indicates implementation default
        :param expires: date for the ban's expiration (unban), or None to imply
            forever
        :param source: source of the ban, None indicates implementation default
        :return: the entry for the newly created ban, or the entry for the
            (updated) previous ban
        :raises ValueError: if ProfilePlayer has an invalid UUID
        """
        ...
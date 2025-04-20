from typing import Set, Optional
from org.bukkit.ChatColor import ChatColor
from org.bukkit.OfflinePlayer import OfflinePlayer
from org.bukkit.potion.PotionEffectType import PotionEffectType
from org.jetbrains.annotations import NotNull, Nullable

"""
A team on a scoreboard that has a common display theme and other
properties. This team is only relevant to the display of the associated
scoreboard.
"""
class Team:

    """
    Gets the name of this Team

    @return Objective name
    @throws IllegalStateException if this team has been unregistered
    """
        def get_name(self) -> str: ...

    """
    Gets the name displayed to entries for this team

    @return Team display name
    @throws IllegalStateException if this team has been unregistered
    """
        def get_display_name(self) -> str: ...

    """
    Sets the name displayed to entries for this team

    @param displayName New display name
    @throws IllegalStateException if this team has been unregistered
    """
    def set_display_name(self, display_name: str) -> None: ...

    """
    Gets the prefix prepended to the display of entries on this team.

    @return Team prefix
    @throws IllegalStateException if this team has been unregistered
    """
        def get_prefix(self) -> str: ...

    """
    Sets the prefix prepended to the display of entries on this team.

    @param prefix New prefix
    @throws IllegalStateException if this team has been unregistered
    """
    def set_prefix(self, prefix: str) -> None: ...

    """
    Gets the suffix appended to the display of entries on this team.

    @return the team's current suffix
    @throws IllegalStateException if this team has been unregistered
    """
        def get_suffix(self) -> str: ...

    """
    Sets the suffix appended to the display of entries on this team.

    @param suffix the new suffix for this team.
    @throws IllegalStateException if this team has been unregistered
    """
    def set_suffix(self, suffix: str) -> None: ...

    """
    Gets the color of the team.
    <br>
    This only sets the team outline, other occurrences of colors such as in
    names are handled by prefixes / suffixes.

    @return team color, defaults to ChatColor.RESET
    @throws IllegalStateException if this team has been unregistered
    """
        def get_color(self) -> ChatColor: ...

    """
    Sets the color of the team.
    <br>
    This only sets the team outline, other occurrences of colors such as in
    names are handled by prefixes / suffixes.

    @param color new color, must be non-null. Use ChatColor.RESET for
    no color
    """
    def set_color(self, color: ChatColor) -> None: ...

    """
    Gets the team friendly fire state

    @return true if friendly fire is enabled
    @throws IllegalStateException if this team has been unregistered
    """
    def allow_friendly_fire(self) -> bool: ...

    """
    Sets the team friendly fire state

    @param enabled true if friendly fire is to be allowed
    @throws IllegalStateException if this team has been unregistered
    """
    def set_allow_friendly_fire(self, enabled: bool) -> None: ...

    """
    Gets the team's ability to see invisible teammates.

    @return true if team members can see invisible members
    @throws IllegalStateException if this team has been unregistered
    """
    def can_see_friendly_invisibles(self) -> bool: ...

    """
    Sets the team's ability to see invisible teammates.

    @param enabled true if invisible teammates are to be visible
    @throws IllegalStateException if this team has been unregistered
    """
    def set_can_see_friendly_invisibles(self, enabled: bool) -> None: ...

    """
    Gets the team's ability to see name tags

    @return the current name tag visibility for the team
    @throws IllegalArgumentException if this team has been unregistered
    @deprecated see get_option(Team.Option)
    """
    @Deprecated(since="1.9")
        def get_name_tag_visibility(self) -> 'NameTagVisibility': ...

    """
    Set's the team's ability to see name tags

    @param visibility The nameTagVisibility to set
    @throws IllegalArgumentException if this team has been unregistered
    @deprecated see set_option(Team.Option, Team.OptionStatus)
    """
    @Deprecated(since="1.9")
    def set_name_tag_visibility(self, visibility: 'NameTagVisibility') -> None: ...

    """
    Gets the Set of players on the team

    @return players on the team
    @throws IllegalStateException if this team has been unregistered
    @see get_entries()
    @deprecated Teams can contain entries that aren't players
    """
    @Deprecated(since="1.8.6")
        def get_players(self) -> Set[OfflinePlayer]: ...

    """
    Gets the Set of entries on the team

    @return entries on the team
    @throws IllegalStateException if this entries has been unregistered
    """
        def get_entries(self) -> Set[str]: ...

    """
    Gets the size of the team

    @return number of entries on the team
    @throws IllegalStateException if this team has been unregistered
    """
    def get_size(self) -> int: ...

    """
    Gets the Scoreboard to which this team is attached

    @return Owning scoreboard, or null if this team has been unregistered
    """
        def get_scoreboard(self) -> Optional['Scoreboard']: ...

    """
    This puts the specified player onto this team for the scoreboard.
    <p>
    This will remove the player from any other team on the scoreboard.

    @param player the player to add
    @throws IllegalStateException if this team has been unregistered
    @see add_entry(String)
    @deprecated Teams can contain entries that aren't players
    """
    @Deprecated(since="1.8.6")
    def add_player(self, player: OfflinePlayer) -> None: ...

    """
    This puts the specified entry onto this team for the scoreboard.
    <p>
    This will remove the entry from any other team on the scoreboard.

    @param entry the entry to add
    @throws IllegalStateException if this team has been unregistered
    """
    def add_entry(self, entry: str) -> None: ...

    """
    Removes the player from this team.

    @param player the player to remove
    @return if the player was on this team
    @throws IllegalStateException if this team has been unregistered
    @see remove_entry(String)
    @deprecated Teams can contain entries that aren't players
    """
    @Deprecated(since="1.8.6")
    def remove_player(self, player: OfflinePlayer) -> bool: ...

    """
    Removes the entry from this team.

    @param entry the entry to remove
    @return if the entry was a part of this team
    @throws IllegalStateException if this team has been unregistered
    """
    def remove_entry(self, entry: str) -> bool: ...

    """
    Unregisters this team from the Scoreboard

    @throws IllegalStateException if this team has been unregistered
    """
    def unregister(self) -> None: ...

    """
    Checks to see if the specified player is a member of this team.

    @param player the player to search for
    @return true if the player is a member of this team
    @throws IllegalStateException if this team has been unregistered
    @see has_entry(String)
    @deprecated Teams can contain entries that aren't players
    """
    @Deprecated(since="1.8.6")
    def has_player(self, player: OfflinePlayer) -> bool: ...

    """
    Checks to see if the specified entry is a member of this team.

    @param entry the entry to search for
    @return true if the entry is a member of this team
    @throws IllegalStateException if this team has been unregistered
    """
    def has_entry(self, entry: str) -> bool: ...

    """
    Get an option for this team

    @param option the option to get
    @return the option status
    @throws IllegalStateException if this team has been unregistered
    """
        def get_option(self, option: 'Option') -> 'OptionStatus': ...

    """
    Set an option for this team

    @param option the option to set
    @param status the new option status
    @throws IllegalStateException if this team has been unregistered
    """
    def set_option(self, option: 'Option', status: 'OptionStatus') -> None: ...

    """
    Represents an option which may be applied to this team.
    """
    class Option:
        """
        How to display the name tags of players on this team.
        """
        NAME_TAG_VISIBILITY: 'Option'
        """
        How to display the death messages for players on this team.
        """
        DEATH_MESSAGE_VISIBILITY: 'Option'
        """
        How players of this team collide with others.
        """
        COLLISION_RULE: 'Option'

    """
    How an option may be applied to members of this team.
    """
    class OptionStatus:
        """
        Apply this option to everyone.
        """
        ALWAYS: 'OptionStatus'
        """
        Never apply this option.
        """
        NEVER: 'OptionStatus'
        """
        Apply this option only for opposing teams.
        """
        FOR_OTHER_TEAMS: 'OptionStatus'
        """
        Apply this option for only team members.
        """
        FOR_OWN_TEAM: 'OptionStatus'
from typing import Set, Optional
from org.bukkit import OfflinePlayer
from org.jetbrains.annotations import NotNull, Nullable

"""
A scoreboard
"""
class Scoreboard:

    """
    Registers an Objective on this Scoreboard

    @param name Name of the Objective
    @param criteria Criteria for the Objective
    @return The registered Objective
    @throws IllegalArgumentException if name is longer than 32767
        characters.
    @throws IllegalArgumentException if an objective by that name already
        exists
    @deprecated a displayName should be explicitly specified
    """
    @Deprecated(since="1.13")
        def register_new_objective(self, name: str, criteria: str) -> 'Objective':
        ...

    """
    Registers an Objective on this Scoreboard

    @param name Name of the Objective
    @param criteria Criteria for the Objective
    @param displayName Name displayed to players for the Objective.
    @return The registered Objective
    @throws IllegalArgumentException if name is longer than 32767
        characters.
    @throws IllegalArgumentException if an objective by that name already
        exists
    @deprecated use {@link #registerNewObjective(String, Criteria, String)}
    """
    @Deprecated(since="1.20.5")
        def register_new_objective(self, name: str, criteria: str, display_name: str) -> 'Objective':
        ...

    """
    Registers an Objective on this Scoreboard

    @param name Name of the Objective
    @param criteria Criteria for the Objective
    @param displayName Name displayed to players for the Objective.
    @param renderType Manner of rendering the Objective
    @return The registered Objective
    @throws IllegalArgumentException if name is longer than 32767
        characters.
    @throws IllegalArgumentException if an objective by that name already
        exists
    @deprecated use {@link #registerNewObjective(String, Criteria, String, RenderType)}
    """
    @Deprecated(since="1.20.5")
        def register_new_objective(self, name: str, criteria: str, display_name: str, render_type: 'RenderType') -> 'Objective':
        ...

    """
    Registers an Objective on this Scoreboard

    @param name Name of the Objective
    @param criteria Criteria for the Objective
    @param displayName Name displayed to players for the Objective.
    @return The registered Objective
    @throws IllegalArgumentException if name is longer than 32767
        characters.
    @throws IllegalArgumentException if an objective by that name already
        exists
    """
        def register_new_objective(self, name: str, criteria: 'Criteria', display_name: str) -> 'Objective':
        ...

    """
    Registers an Objective on this Scoreboard

    @param name Name of the Objective
    @param criteria Criteria for the Objective
    @param displayName Name displayed to players for the Objective.
    @param renderType Manner of rendering the Objective
    @return The registered Objective
    @throws IllegalArgumentException if name is longer than 32767
        characters.
    @throws IllegalArgumentException if an objective by that name already
        exists
    """
        def register_new_objective(self, name: str, criteria: 'Criteria', display_name: str, render_type: 'RenderType') -> 'Objective':
        ...

    """
    Gets an Objective on this Scoreboard by name

    @param name Name of the Objective
    @return the Objective or null if it does not exist
    """
        def get_objective(self, name: str) -> Optional['Objective']:
        ...

    """
    Gets all Objectives of a Criteria on the Scoreboard

    @param criteria Criteria to search by
    @return an immutable set of Objectives using the specified Criteria
    @deprecated use {@link #getObjectivesByCriteria(Criteria)}
    """
    @Deprecated(since="1.19.2")
        def get_objectives_by_criteria(self, criteria: str) -> Set['Objective']:
        ...

    """
    Gets all Objectives of a Criteria on the Scoreboard

    @param criteria Criteria to search by
    @return an immutable set of Objectives using the specified Criteria
    """
        def get_objectives_by_criteria(self, criteria: 'Criteria') -> Set['Objective']:
        ...

    """
    Gets all Objectives on this Scoreboard

    @return An immutable set of all Objectives on this Scoreboard
    """
        def get_objectives(self) -> Set['Objective']:
        ...

    """
    Gets the Objective currently displayed in a DisplaySlot on this
    Scoreboard

    @param slot The DisplaySlot
    @return the Objective currently displayed or null if nothing is
        displayed in that DisplaySlot
    """
        def get_objective(self, slot: 'DisplaySlot') -> Optional['Objective']:
        ...

    """
    Gets all scores for a player on this Scoreboard

    @param player the player whose scores are being retrieved
    @return immutable set of all scores tracked for the player
    @see #getScores(String)
    @deprecated Scoreboards can contain entries that aren't players
    """
    @Deprecated(since="1.7.8")
        def get_scores(self, player: OfflinePlayer) -> Set['Score']:
        ...

    """
    Gets all scores for an entry on this Scoreboard

    @param entry the entry whose scores are being retrieved
    @return immutable set of all scores tracked for the entry
    """
        def get_scores(self, entry: str) -> Set['Score']:
        ...

    """
    Removes all scores for a player on this Scoreboard

    @param player the player to drop all current scores for
    @see #resetScores(String)
    @deprecated Scoreboards can contain entries that aren't players
    """
    @Deprecated(since="1.7.8")
    def reset_scores(self, player: OfflinePlayer) -> None:
        ...

    """
    Removes all scores for an entry on this Scoreboard

    @param entry the entry to drop all current scores for
    """
    def reset_scores(self, entry: str) -> None:
        ...

    """
    Gets a player's Team on this Scoreboard

    @param player the player to search for
    @return the player's Team or null if the player is not on a team
    @see #getEntryTeam(String)
    @deprecated Scoreboards can contain entries that aren't players
    """
    @Deprecated(since="1.8.6")
        def get_player_team(self, player: OfflinePlayer) -> Optional['Team']:
        ...

    """
    Gets a entries Team on this Scoreboard

    @param entry the entry to search for
    @return the entries Team or null if the entry is not on a team
    """
        def get_entry_team(self, entry: str) -> Optional['Team']:
        ...

    """
    Gets a Team by name on this Scoreboard

    @param team_name Team name
    @return the matching Team or null if no matches
    """
        def get_team(self, team_name: str) -> Optional['Team']:
        ...

    """
    Gets all teams on this Scoreboard

    @return an immutable set of Teams
    """
        def get_teams(self) -> Set['Team']:
        ...

    """
    Registers a Team on this Scoreboard

    @param name Team name
    @return registered Team
    @throws IllegalArgumentException if team by that name already exists
    """
        def register_new_team(self, name: str) -> 'Team':
        ...

    """
    Gets all players tracked by this Scoreboard

    @return immutable set of all tracked players
    @see #getEntries()
    @deprecated Scoreboards can contain entries that aren't players
    """
    @Deprecated(since="1.7.8")
        def get_players(self) -> Set[OfflinePlayer]:
        ...

    """
    Gets all entries tracked by this Scoreboard

    @return immutable set of all tracked entries
    """
        def get_entries(self) -> Set[str]:
        ...

    """
    Clears any objective in the specified slot.

    @param slot the slot to remove objectives
    """
    def clear_slot(self, slot: 'DisplaySlot') -> None:
        ...
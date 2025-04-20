from org.bukkit.OfflinePlayer import OfflinePlayer
from org.bukkit.scoreboard.Criteria import Criteria
from org.bukkit.scoreboard.DisplaySlot import DisplaySlot
from org.bukkit.scoreboard.RenderType import RenderType
from org.bukkit.scoreboard.Score import Score
from org.bukkit.scoreboard.Scoreboard import Scoreboard
from typing import Optional

"""
An objective on a scoreboard that can show scores specific to entries. This
objective is only relevant to the display of the associated scoreboard.
"""
class Objective:

    """
    Gets the name of this Objective

    @return this objective's name
    @throws IllegalStateException if this objective has been unregistered
    """
    def get_name(self) -> str:
        ...

    """
    Gets the name displayed to players for this objective

    @return this objective's display name
    @throws IllegalStateException if this objective has been unregistered
    """
    def get_display_name(self) -> str:
        ...

    """
    Sets the name displayed to players for this objective.

    @param display_name Display name to set
    @throws IllegalStateException if this objective has been unregistered
    """
    def set_display_name(self, display_name: str) -> None:
        ...

    """
    Gets the criteria this objective tracks.

    @return this objective's criteria
    @throws IllegalStateException if this objective has been unregistered
    @deprecated use get_tracked_criteria()
    """
    def get_criteria(self) -> str:
        ...

    """
    Gets the criteria this objective tracks.

    @return this objective's criteria
    @throws IllegalStateException if this objective has been unregistered
    """
    def get_tracked_criteria(self) -> Criteria:
        ...

    """
    Gets if the objective's scores can be modified directly by a plugin.

    @return true if scores are modifiable
    @throws IllegalStateException if this objective has been unregistered
    @see Criterias#HEALTH
    """
    def is_modifiable(self) -> bool:
        ...

    """
    Gets the scoreboard to which this objective is attached.

    @return Owning scoreboard, or null if it has been unregistered
    """
    def get_scoreboard(self) -> Optional[Scoreboard]:
        ...

    """
    Unregisters this objective from the scoreboard.

    @throws IllegalStateException if this objective has been unregistered
    """
    def unregister(self) -> None:
        ...

    """
    Sets this objective to display on the specified slot for the
    scoreboard, removing it from any other display slot.

    @param slot display slot to change, or null to not display
    @throws IllegalStateException if this objective has been unregistered
    """
    def set_display_slot(self, slot: Optional[DisplaySlot]) -> None:
        ...

    """
    Gets the display slot this objective is displayed at.

    @return the display slot for this objective, or null if not displayed
    @throws IllegalStateException if this objective has been unregistered
    """
    def get_display_slot(self) -> Optional[DisplaySlot]:
        ...

    """
    Sets manner in which this objective will be rendered.

    @param render_type new render type
    @throws IllegalStateException if this objective has been unregistered
    """
    def set_render_type(self, render_type: RenderType) -> None:
        ...

    """
    Sets manner in which this objective will be rendered.

    @return the render type
    @throws IllegalStateException if this objective has been unregistered
    """
    def get_render_type(self) -> RenderType:
        ...

    """
    Gets a player's Score for an Objective on this Scoreboard

    @param player Player for the Score
    @return Score tracking the Objective and player specified
    @throws IllegalStateException if this objective has been unregistered
    @see get_score(String)
    @deprecated Scoreboards can contain entries that aren't players
    """
    def get_score(self, player: OfflinePlayer) -> Score:
        ...

    """
    Gets an entry's Score for an Objective on this Scoreboard.

    @param entry Entry for the Score
    @return Score tracking the Objective and entry specified
    @throws IllegalStateException if this objective has been unregistered
    @throws IllegalArgumentException if entry is longer than 32767 characters.
    """
    def get_score(self, entry: str) -> Score:
        ...
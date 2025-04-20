from org.bukkit import OfflinePlayer
from org.bukkit.scoreboard import Objective, Scoreboard
from typing import Optional

"""
A score entry for an {@link #getEntry() entry} on an {@link
#getObjective() objective}. Changing this will not affect any other
objective or scoreboard.
"""
class Score:
    """
    Gets the OfflinePlayer being tracked by this Score

    @return this Score's tracked player
    @see #getEntry()
    @deprecated Scoreboards can contain entries that aren't players
    """
    def getPlayer(self) -> OfflinePlayer:
        ...

    """
    Gets the entry being tracked by this Score

    @return this Score's tracked entry
    """
    def getEntry(self) -> str:
        ...

    """
    Gets the Objective being tracked by this Score

    @return this Score's tracked objective
    """
    def getObjective(self) -> Objective:
        ...

    """
    Gets the current score

    @return the current score
    @throws IllegalStateException if the associated objective has been
        unregistered
    """
    def getScore(self) -> int:
        ...

    """
    Sets the current score.

    @param score New score
    @throws IllegalStateException if the associated objective has been
        unregistered
    """
    def setScore(self, score: int) -> None:
        ...

    """
    Shows if this score has been set at any point in time.

    @return if this score has been set before
    @throws IllegalStateException if the associated objective has been
        unregistered
    """
    def isScoreSet(self) -> bool:
        ...

    """
    Gets the scoreboard for the associated objective.

    @return the owning objective's scoreboard, or null if it has been
        {@link Objective#unregister() unregistered}
    """
    def getScoreboard(self) -> Optional[Scoreboard]:
        ...
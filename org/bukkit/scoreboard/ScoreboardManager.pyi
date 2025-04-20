from typing import Protocol, runtime_checkable
from org.bukkit.scoreboard import Scoreboard

@runtime_checkable
class ScoreboardManager(Protocol):
    """
    Manager of Scoreboards
    """

    def get_main_scoreboard(self) -> Scoreboard:
        """
        Gets the primary Scoreboard controlled by the server.
        <p>
        This Scoreboard is saved by the server, is affected by the /scoreboard
        command, and is the scoreboard shown by default to players.

        @return: the default server scoreboard
        """
        ...

    def get_new_scoreboard(self) -> Scoreboard:
        """
        Gets a new Scoreboard to be tracked by the server. This scoreboard will
        be tracked as long as a reference is kept, either by a player or by a
        plugin.

        @return: the registered Scoreboard
        @see: WeakReference
        """
        ...
from typing import List, Optional
from org.bukkit.entity import Player
from org.bukkit.boss import BarColor, BarStyle, BarFlag

class BossBar:
    """
    Interface for a boss bar.
    """

    def get_title(self) -> str:
        """
        Returns the title of this boss bar.

        Returns:
            The title of the bar.
        """
        ...

    def set_title(self, title: Optional[str]) -> None:
        """
        Sets the title of this boss bar.

        Args:
            title: The title of the bar.
        """
        ...

    def get_color(self) -> BarColor:
        """
        Returns the color of this boss bar.

        Returns:
            The color of the bar.
        """
        ...

    def set_color(self, color: BarColor) -> None:
        """
        Sets the color of this boss bar.

        Args:
            color: The color of the bar.
        """
        ...

    def get_style(self) -> BarStyle:
        """
        Returns the style of this boss bar.

        Returns:
            The style of the bar.
        """
        ...

    def set_style(self, style: BarStyle) -> None:
        """
        Sets the bar style of this boss bar.

        Args:
            style: The style of the bar.
        """
        ...

    def remove_flag(self, flag: BarFlag) -> None:
        """
        Remove an existing flag on this boss bar.

        Args:
            flag: The existing flag to remove.
        """
        ...

    def add_flag(self, flag: BarFlag) -> None:
        """
        Add an optional flag to this boss bar.

        Args:
            flag: An optional flag to set on the boss bar.
        """
        ...

    def has_flag(self, flag: BarFlag) -> bool:
        """
        Returns whether this boss bar has the passed flag set.

        Args:
            flag: The flag to check.

        Returns:
            Whether it has the flag.
        """
        ...

    def set_progress(self, progress: float) -> None:
        """
        Sets the progress of the bar. Values should be between 0.0 (empty) and 1.0 (full).

        Args:
            progress: The progress of the bar.
        """
        ...

    def get_progress(self) -> float:
        """
        Returns the progress of the bar between 0.0 and 1.0.

        Returns:
            The progress of the bar.
        """
        ...

    def add_player(self, player: Player) -> None:
        """
        Adds the player to this boss bar causing it to display on their screen.

        Args:
            player: The player to add.
        """
        ...

    def remove_player(self, player: Player) -> None:
        """
        Removes the player from this boss bar causing it to be removed from their screen.

        Args:
            player: The player to remove.
        """
        ...

    def remove_all(self) -> None:
        """
        Removes all players from this boss bar.
        """
        ...

    def get_players(self) -> List[Player]:
        """
        Returns all players viewing this boss bar.

        Returns:
            An immutable list of players.
        """
        ...

    def set_visible(self, visible: bool) -> None:
        """
        Set if the boss bar is displayed to attached players.

        Args:
            visible: Visible status.
        """
        ...

    def is_visible(self) -> bool:
        """
        Return if the boss bar is displayed to attached players.

        Returns:
            Visible status.
        """
        ...

    def show(self) -> None:
        """
        Shows the previously hidden boss bar to all attached players.

        Deprecated:
            Since 1.9, use set_visible(boolean) instead.
        """
        ...

    def hide(self) -> None:
        """
        Hides this boss bar from all attached players.

        Deprecated:
            Since 1.9, use set_visible(boolean) instead.
        """
        ...
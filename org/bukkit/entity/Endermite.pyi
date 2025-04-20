from typing import Protocol

class Endermite(Protocol):
    """
    Represents an Endermite entity in the game.
    """

    def is_player_spawned(self) -> bool:
        """
        Gets whether this Endermite was spawned by a player.

        An Endermite spawned by a player will be attacked by nearby Enderman.

        Returns:
            player spawned status
        """
        ...

    def set_player_spawned(self, player_spawned: bool) -> None:
        """
        Sets whether this Endermite was spawned by a player.

        An Endermite spawned by a player will be attacked by nearby Enderman.

        Args:
            player_spawned: player spawned status
        """
        ...
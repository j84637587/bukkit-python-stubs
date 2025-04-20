from org.bukkit.entity import Entity
from org.bukkit import OfflinePlayer
from typing import Optional

class Interaction(Entity):
    """
    Represents an entity designed to only record interactions.
    """

    def get_interaction_width(self) -> float:
        """
        Gets the width of this interaction entity.

        Returns:
            width
        """
        ...

    def set_interaction_width(self, width: float) -> None:
        """
        Sets the width of this interaction entity.

        Args:
            width: new width
        """
        ...

    def get_interaction_height(self) -> float:
        """
        Gets the height of this interaction entity.

        Returns:
            height
        """
        ...

    def set_interaction_height(self, height: float) -> None:
        """
        Sets the height of this interaction entity.

        Args:
            height: new height
        """
        ...

    def is_responsive(self) -> bool:
        """
        Gets if this interaction entity should trigger a response when interacted with.

        Returns:
            response setting
        """
        ...

    def set_responsive(self, response: bool) -> None:
        """
        Sets if this interaction entity should trigger a response when interacted with.

        Args:
            response: new setting
        """
        ...

    def get_last_attack(self) -> Optional['PreviousInteraction']:
        """
        Gets the last attack on this interaction entity.

        Returns:
            last attack data, if present
        """
        ...

    def get_last_interaction(self) -> Optional['PreviousInteraction']:
        """
        Gets the last interaction on this entity.

        Returns:
            last interaction data, if present
        """
        ...


class PreviousInteraction:
    """
    Represents a previous interaction with this entity.
    """

    def get_player(self) -> OfflinePlayer:
        """
        Get the previous interacting player.

        Returns:
            interacting player
        """
        ...

    def get_timestamp(self) -> int:
        """
        Gets the Unix timestamp at when this interaction occurred.

        Returns:
            interaction timestamp
        """
        ...
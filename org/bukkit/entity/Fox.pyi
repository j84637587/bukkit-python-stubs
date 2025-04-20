from typing import Optional
from org.bukkit.entity import Animals, Sittable
from org.bukkit.entity import AnimalTamer

class Fox(Animals, Sittable):
    """What does the fox say?"""

    def get_fox_type(self) -> 'Fox.Type':
        """
        Gets the current type of this fox.

        Returns:
            Type of the fox.
        """
        ...

    def set_fox_type(self, type: 'Fox.Type') -> None:
        """
        Sets the current type of this fox.

        Args:
            type: New type of this fox.
        """
        ...

    def is_crouching(self) -> bool:
        """
        Checks if this animal is crouching.

        Returns:
            true if crouching
        """
        ...

    def set_crouching(self, crouching: bool) -> None:
        """
        Sets if this animal is crouching.

        Args:
            crouching: true if crouching
        """
        ...

    def set_sleeping(self, sleeping: bool) -> None:
        """
        Sets if this animal is sleeping.

        Args:
            sleeping: true if sleeping
        """
        ...

    def get_first_trusted_player(self) -> Optional[AnimalTamer]:
        """
        Gets the first trusted player.

        Returns:
            the owning AnimalTamer, or None if not owned
        """
        ...

    def set_first_trusted_player(self, player: Optional[AnimalTamer]) -> None:
        """
        Set the first trusted player.
        The first trusted player may only be removed after the second.

        Args:
            player: the AnimalTamer to be trusted
        """
        ...

    def get_second_trusted_player(self) -> Optional[AnimalTamer]:
        """
        Gets the second trusted player.

        Returns:
            the owning AnimalTamer, or None if not owned
        """
        ...

    def set_second_trusted_player(self, player: Optional[AnimalTamer]) -> None:
        """
        Set the second trusted player.
        The second trusted player may only be added after the first.

        Args:
            player: the AnimalTamer to be trusted
        """
        ...

    def is_faceplanted(self) -> bool:
        """
        Gets whether the fox is faceplanting the ground.

        Returns:
            Whether the fox is faceplanting the ground
        """
        ...

    class Type:
        """Represents the various different fox types there are."""
        RED = ...
        SNOW = ...
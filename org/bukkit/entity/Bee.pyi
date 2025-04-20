from org.bukkit import Location
from typing import Optional

class Bee(Animals):
    """Represents a Bee."""

    def get_hive(self) -> Optional[Location]:
        """Get the bee's hive location.

        Returns:
            hive location or None
        """
        ...

    def set_hive(self, location: Optional[Location]) -> None:
        """Set the bee's hive location.

        Args:
            location: or None
        """
        ...

    def get_flower(self) -> Optional[Location]:
        """Get the bee's flower location.

        Returns:
            flower location or None
        """
        ...

    def set_flower(self, location: Optional[Location]) -> None:
        """Set the bee's flower location.

        Args:
            location: or None
        """
        ...

    def has_nectar(self) -> bool:
        """Get if the bee has nectar.

        Returns:
            nectar
        """
        ...

    def set_has_nectar(self, nectar: bool) -> None:
        """Set if the bee has nectar.

        Args:
            nectar: whether the entity has nectar
        """
        ...

    def has_stung(self) -> bool:
        """Get if the bee has stung.

        Returns:
            has stung
        """
        ...

    def set_has_stung(self, stung: bool) -> None:
        """Set if the bee has stung.

        Args:
            stung: has stung
        """
        ...

    def get_anger(self) -> int:
        """Get the bee's anger level.

        Returns:
            anger level
        """
        ...

    def set_anger(self, anger: int) -> None:
        """Set the bee's new anger level.

        Args:
            anger: new anger
        """
        ...

    def get_cannot_enter_hive_ticks(self) -> int:
        """Get the amount of ticks the bee cannot enter the hive for.

        Returns:
            Ticks the bee cannot enter a hive for
        """
        ...

    def set_cannot_enter_hive_ticks(self, ticks: int) -> None:
        """Set the amount of ticks the bee cannot enter a hive for.

        Args:
            ticks: Ticks the bee cannot enter a hive for
        """
        ...
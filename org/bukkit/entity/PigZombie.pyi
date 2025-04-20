from org.bukkit.entity import Zombie

class PigZombie(Zombie):
    """Represents a Pig Zombie."""

    def get_anger(self) -> int:
        """Get the pig zombie's current anger level.

        Returns:
            The anger level.
        """
        ...

    def set_anger(self, level: int) -> None:
        """Set the pig zombie's current anger level.

        Args:
            level: The anger level. Higher levels of anger take longer to wear off.
        """
        ...

    def set_angry(self, angry: bool) -> None:
        """Shorthand; sets to either 0 or the default level.

        Args:
            angry: Whether the zombie should be angry.
        """
        ...

    def is_angry(self) -> bool:
        """Shorthand; gets whether the zombie is angry.

        Returns:
            True if the zombie is angry, otherwise false.
        """
        ...

    def is_converting(self) -> bool:
        """<b>Not applicable to this entity</b>

        Returns:
            false
        """
        ...

    def get_conversion_time(self) -> int:
        """<b>Not applicable to this entity</b>

        Returns:
            UnsuppotedOperationException
        """
        ...

    def set_conversion_time(self, time: int) -> None:
        """<b>Not applicable to this entity</b>

        Args:
            time: unused
        """
        ...
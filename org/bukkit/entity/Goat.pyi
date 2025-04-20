from org.bukkit.entity import Animals

class Goat(Animals):
    """A Goat."""

    def has_left_horn(self) -> bool:
        """Gets if this goat has its left horn.

        Returns:
            left horn status
        """
        ...

    def set_left_horn(self, has_horn: bool) -> None:
        """Sets if this goat has its left horn.

        Args:
            has_horn: left horn status
        """
        ...

    def has_right_horn(self) -> bool:
        """Gets if this goat has its right horn.

        Returns:
            right horn status
        """
        ...

    def set_right_horn(self, has_horn: bool) -> None:
        """Sets if this goat has its right horn.

        Args:
            has_horn: right horn status
        """
        ...

    def is_screaming(self) -> bool:
        """Gets if this is a screaming goat.

        A screaming goat makes screaming sounds and rams more often. They do not
        offer home loans.

        Returns:
            screaming status
        """
        ...

    def set_screaming(self, screaming: bool) -> None:
        """Sets if this is a screaming goat.

        A screaming goat makes screaming sounds and rams more often. They do not
        offer home loans.

        Args:
            screaming: screaming status
        """
        ...

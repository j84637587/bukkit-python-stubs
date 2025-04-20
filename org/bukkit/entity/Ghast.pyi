from typing import Protocol

class Flying(Protocol):
    pass

class Enemy(Protocol):
    pass

class Ghast(Flying, Enemy):
    """
    Represents a Ghast.
    """

    def is_charging(self) -> bool:
        """
        Gets whether the Ghast is charging.

        Returns:
            Whether the Ghast is charging.
        """
        ...

    def set_charging(self, flag: bool) -> None:
        """
        Sets whether the Ghast is charging.

        Args:
            flag: Whether the Ghast is charging.
        """
        ...
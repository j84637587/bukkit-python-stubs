from typing import Protocol

class Illager(Protocol):
    pass

class Vindicator(Illager, Protocol):
    """
    Represents a Vindicator.
    """

    def is_johnny(self) -> bool:
        """
        Returns whether a vindicator is in "Johnny" mode.

        When this mode is active, vindicators will be hostile to all mobs.

        @return: true if johnny
        """
        ...

    def set_johnny(self, johnny: bool) -> None:
        """
        Sets the Johnny state of a vindicator.

        @param johnny: new johnny state
        """
        ...
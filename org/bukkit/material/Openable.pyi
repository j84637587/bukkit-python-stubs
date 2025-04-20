from typing import Protocol

class Openable(Protocol):
    """Interface for an openable object."""

    def is_open(self) -> bool:
        """Check to see if the door is open.

        Returns:
            True if the door has swung counterclockwise around its hinge.
        """
        ...

    def set_open(self, is_open: bool) -> None:
        """Configure this door to be either open or closed.

        Args:
            is_open: True to open the door.
        """
        ...
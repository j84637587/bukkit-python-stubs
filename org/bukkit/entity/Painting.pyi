from org.bukkit import Art
from org.bukkit.event.hanging import HangingBreakEvent
from typing import Protocol

class Hanging(Protocol):
    pass

class Painting(Hanging, Protocol):
    """
    Represents a Painting.
    """

    def get_art(self) -> Art:
        """
        Get the art on this painting

        Returns:
            The art
        """
        ...

    def set_art(self, art: Art) -> bool:
        """
        Set the art on this painting

        Args:
            art: The new art

        Returns:
            False if the new art won't fit at the painting's current location
        """
        ...

    def set_art(self, art: Art, force: bool) -> bool:
        """
        Set the art on this painting

        Args:
            art: The new art
            force: If true, force the new art regardless of whether it fits
                   at the current location. Note that forcing it where it can't fit
                   normally causes it to drop as an item unless you override this by
                   catching the HangingBreakEvent.

        Returns:
            False if force was false and the new art won't fit at the
            painting's current location
        """
        ...
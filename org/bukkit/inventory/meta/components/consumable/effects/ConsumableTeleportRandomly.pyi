from typing import Protocol

class ConsumableEffect(Protocol):
    pass

class ConsumableTeleportRandomly(Protocol):
    """Represent a random teleport when an item is consumed."""

    def get_diameter(self) -> float:
        """Gets the diameter that the consumer is teleported within.

        Returns:
            float: the diameter
        """
        ...

    def set_diameter(self, diameter: float) -> None:
        """Sets the diameter that the consumer is teleported within.

        Args:
            diameter (float): new diameter
        """
        ...
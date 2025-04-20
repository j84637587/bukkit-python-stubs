from typing import Protocol

class Animals(Protocol):
    pass

class Turtle(Animals, Protocol):
    """Represents a turtle."""

    def has_egg(self) -> bool:
        """Gets whether the turtle has an egg.

        Returns:
            Whether the turtle has an egg.
        """
        ...

    def is_laying_egg(self) -> bool:
        """Gets whether the turtle is laying an egg.

        Returns:
            Whether the turtle is laying an egg.
        """
        ...

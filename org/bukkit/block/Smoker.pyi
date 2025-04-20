from typing import Protocol

class Furnace(Protocol):
    """Represents a furnace interface."""

class Smoker(Furnace, Protocol):
    """Represents a captured state of a smoker."""
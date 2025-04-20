from typing import Protocol

class Container(Protocol):
    pass

class Lootable(Protocol):
    pass

class Lidded(Protocol):
    pass

class Barrel(Container, Lootable, Lidded):
    """Represents a captured state of a Barrel."""
    pass
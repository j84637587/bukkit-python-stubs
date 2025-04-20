from typing import Protocol
from .container import Container
from .lootable import Lootable

class Hopper(Protocol[Container, Lootable]):
    """Represents a captured state of a hopper."""
    pass
from typing import Protocol

class Raider(Protocol):
    """Represents a type of Raider."""

class Illager(Raider, Protocol):
    """Represents a type of "Illager"."""
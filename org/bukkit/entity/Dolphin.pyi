from typing import Protocol

class Ageable(Protocol):
    """Interface for ageable entities."""

class WaterMob(Protocol):
    """Interface for water-based mobs."""

class Dolphin(Ageable, WaterMob, Protocol):
    """Interface representing a Dolphin entity."""
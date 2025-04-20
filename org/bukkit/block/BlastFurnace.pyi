"""
Represents a captured state of a blast furnace.
"""

from typing import Protocol

class Furnace(Protocol):
    pass

class BlastFurnace(Furnace, Protocol):
    pass
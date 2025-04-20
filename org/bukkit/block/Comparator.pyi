# Comparator.pyi

"""
Represents a captured state of an on / off comparator.
"""

from typing import Protocol

class TileState(Protocol):
    pass

class Comparator(TileState, Protocol):
    pass
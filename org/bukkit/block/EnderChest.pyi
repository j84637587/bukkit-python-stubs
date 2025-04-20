# EnderChest.pyi

"""
Represents a captured state of an ender chest.
"""

from typing import Protocol

class Lidded(Protocol):
    pass

class TileState(Protocol):
    pass

class EnderChest(Lidded, TileState, Protocol):
    pass
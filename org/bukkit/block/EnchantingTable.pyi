from typing import Protocol
from .tile_state import TileState
from .nameable import Nameable

class EnchantingTable(Protocol[TileState, Nameable]):
    """Represents a captured state of an enchanting table."""
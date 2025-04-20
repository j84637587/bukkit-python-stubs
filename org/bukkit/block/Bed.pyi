from typing import Protocol
from .tile_state import TileState
from .colorable import Colorable

class Bed(Protocol[TileState, Colorable]):
    """Represents a captured state of a bed.
    
    @deprecated does not provide useful information beyond the material itself
    """
    ...
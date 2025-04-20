# DaylightDetector.pyi

"""
Represents a captured state of a (possibly inverted) daylight detector.
"""

from typing import Protocol

class TileState(Protocol):
    pass

class DaylightDetector(TileState, Protocol):
    pass
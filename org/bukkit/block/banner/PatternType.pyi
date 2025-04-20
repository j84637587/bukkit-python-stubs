from typing import Optional, List
from .namespaced_key import NamespacedKey
from .registry import Registry
from .old_enum import OldEnum
from org.bukkit import Keyed
from .registry_aware import RegistryAware
from google.common.base import Preconditions
from google.common.collect import Lists
import locale

class PatternType(OldEnum["PatternType"], Keyed, RegistryAware):
    BASE: "PatternType"
    SQUARE_BOTTOM_LEFT: "PatternType"
    SQUARE_BOTTOM_RIGHT: "PatternType"
    SQUARE_TOP_LEFT: "PatternType"
    SQUARE_TOP_RIGHT: "PatternType"
    STRIPE_BOTTOM: "PatternType"
    STRIPE_TOP: "PatternType"
    STRIPE_LEFT: "PatternType"
    STRIPE_RIGHT: "PatternType"
    STRIPE_CENTER: "PatternType"
    STRIPE_MIDDLE: "PatternType"
    STRIPE_DOWNRIGHT: "PatternType"
    STRIPE_DOWNLEFT: "PatternType"
    SMALL_STRIPES: "PatternType"
    CROSS: "PatternType"
    STRAIGHT_CROSS: "PatternType"
    TRIANGLE_BOTTOM: "PatternType"
    TRIANGLE_TOP: "PatternType"
    TRIANGLES_BOTTOM: "PatternType"
    TRIANGLES_TOP: "PatternType"
    DIAGONAL_LEFT: "PatternType"
    DIAGONAL_UP_RIGHT: "PatternType"
    DIAGONAL_UP_LEFT: "PatternType"
    DIAGONAL_RIGHT: "PatternType"
    CIRCLE: "PatternType"
    RHOMBUS: "PatternType"
    HALF_VERTICAL: "PatternType"
    HALF_HORIZONTAL: "PatternType"
    HALF_VERTICAL_RIGHT: "PatternType"
    HALF_HORIZONTAL_BOTTOM: "PatternType"
    BORDER: "PatternType"
    CURLY_BORDER: "PatternType"
    CREEPER: "PatternType"
    GRADIENT: "PatternType"
    GRADIENT_UP: "PatternType"
    BRICKS: "PatternType"
    SKULL: "PatternType"
    FLOWER: "PatternType"
    MOJANG: "PatternType"
    GLOBE: "PatternType"
    PIGLIN: "PatternType"
    FLOW: "PatternType"
    GUSTER: "PatternType"

    def getKey(self) -> NamespacedKey:
        """Returns the key associated with this pattern type."""
        ...

    def getIdentifier(self) -> str:
        """Returns the identifier used to represent this pattern type."""
        ...

    @staticmethod
    def getByIdentifier(identifier: Optional[str]) -> Optional["PatternType"]:
        """Returns the pattern type which matches the passed identifier or None if no matches are found."""
        ...

    @staticmethod
    def getType(key: str) -> "PatternType":
        """Private method to get the pattern type by key."""
        ...

    @staticmethod
    def valueOf(name: str) -> "PatternType":
        """Returns the pattern type with the given name."""
        ...

    @staticmethod
    def values() -> List["PatternType"]:
        """Returns an array of all known pattern types."""
        ...

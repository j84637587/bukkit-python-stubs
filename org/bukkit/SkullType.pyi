from enum import Enum
from typing import Any

class Material: ...

class SkullType(Enum):
    """
    Represents the different types of skulls.
    @deprecated check {@link Material} instead
    """
    SKELETON: Any
    WITHER: Any
    ZOMBIE: Any
    PLAYER: Any
    CREEPER: Any
    DRAGON: Any
    PIGLIN: Any
from typing import Any
from enum import Enum

class ExplosionResult(Enum):
    """
    Represents the outcome of an explosion.
    """
    # Represents an explosion where no change took place.
    #
    # This is the case when org.bukkit.GameRule.MOB_GRIEFING is
    # disabled.
    KEEP: Any

    # Represents an explosion where all destroyed blocks drop their items.
    #
    # This is the case when
    # org.bukkit.GameRule.TNT_EXPLOSION_DROP_DECAY or
    # org.bukkit.GameRule.BLOCK_EXPLOSION_DROP_DECAY is disabled.
    DESTROY: Any

    # Represents an explosion where explosions cause only some blocks to drop.
    DESTROY_WITH_DECAY: Any

    # Represents an explosion where a block change/update has happened.
    #
    # For example, when a wind charge is used it will cause nearby buttons,
    # levers and bells to be activated.
    TRIGGER_BLOCK: Any
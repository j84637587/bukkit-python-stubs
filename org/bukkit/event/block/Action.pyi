# org/bukkit/event/block/Action.pyi

from enum import Enum

class Action(Enum):
    """
    Enum representing different block actions.
    """

    LEFT_CLICK_BLOCK: Action
    """Left-clicking a block"""

    RIGHT_CLICK_BLOCK: Action
    """Right-clicking a block"""

    LEFT_CLICK_AIR: Action
    """Left-clicking the air"""

    RIGHT_CLICK_AIR: Action
    """Right-clicking the air"""

    PHYSICAL: Action
    """Stepping onto or into a block (Ass-pressure)

    Examples:
    <ul>
    <li>Jumping on soil
    <li>Standing on pressure plate
    <li>Triggering redstone ore
    <li>Triggering tripwire
    </ul>
    """
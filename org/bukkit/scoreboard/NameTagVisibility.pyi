# org/bukkit/scoreboard/NameTagVisibility.pyi

from enum import Enum
from typing import Literal

class NameTagVisibility(Enum):
    """
    @deprecated replaced by {@link Team.OptionStatus}
    """
    ALWAYS: Literal['ALWAYS']
    NEVER: Literal['NEVER']
    HIDE_FOR_OTHER_TEAMS: Literal['HIDE_FOR_OTHER_TEAMS']
    HIDE_FOR_OWN_TEAM: Literal['HIDE_FOR_OWN_TEAM']
"""
Criteria names which trigger an objective to be modified by actions in-game

@deprecated use the constants declared in {@link Criteria} instead
"""
from typing import Final

class Criterias:
    HEALTH: Final[str] = "health"
    PLAYER_KILLS: Final[str] = "playerKillCount"
    TOTAL_KILLS: Final[str] = "totalKillCount"
    DEATHS: Final[str] = "deathCount"

    def __init__(self) -> None:
        raise NotImplementedError("This class cannot be instantiated.")
from typing import List, Optional
from org.bukkit import Raid, World
from org.bukkit.entity import Raider
from org.bukkit.event import HandlerList

class RaidEvent:
    def __init__(self, raid: Raid, world: World) -> None:
        ...

class RaidSpawnWaveEvent(RaidEvent):
    """
    Called when a raid wave spawns.
    """

    handlers: HandlerList = HandlerList()
    raiders: List[Raider]
    leader: Optional[Raider]

    def __init__(self, raid: Raid, world: World, leader: Optional[Raider], raiders: List[Raider]) -> None:
        super().__init__(raid, world)
        ...

    """
    Returns the patrol leader.

    @return {@link Raider}
    """
    def get_patrol_leader(self) -> Optional[Raider]:
        ...

    """
    Returns all {@link Raider} that spawned in this wave.

    @return an immutable list of raiders
    """
    def get_raiders(self) -> List[Raider]:
        ...

    def get_handlers(self) -> HandlerList:
        ...

    @staticmethod
    def get_handler_list() -> HandlerList:
        ...
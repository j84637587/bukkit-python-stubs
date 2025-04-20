from org.bukkit import Raid
from org.bukkit import World
from org.bukkit.event.world import WorldEvent
from typing import Any
from typing import Optional

class RaidEvent(WorldEvent):
    """
    Represents events related to raids.
    """

    def __init__(self, raid: Raid, world: World) -> None:
        """
        Initializes a new RaidEvent.

        :param raid: The raid involved with this event.
        :param world: The world where the event takes place.
        """
        ...

    def get_raid(self) -> Raid:
        """
        Returns the raid involved with this event.

        :return: Raid
        """
        ...
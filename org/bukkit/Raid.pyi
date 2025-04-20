from typing import List, Set
from uuid import UUID
from org.bukkit.entity import Raider
from org.bukkit import Location

class Raid:
    """
    Represents a raid event.
    """
    def isStarted() -> bool:
        """
        Get whether this raid started.

        :return: whether raid is started
        """
        ...

    def getActiveTicks() -> int:
        """
        Gets the amount of ticks this raid has existed.

        :return: active ticks
        """
        ...

    def getBadOmenLevel() -> int:
        """
        Gets the Bad Omen level of this raid.

        :return: Bad Omen level (between 0 and 5)
        """
        ...

    def setBadOmenLevel(badOmenLevel: int):
        """
        Sets the Bad Omen level.
        <br>
        If the level is higher than 1, there will be an additional wave that as
        strong as the final wave.

        :param badOmenLevel: new Bad Omen level (from 0-5)
        :throws IllegalArgumentException: if invalid Bad Omen level
        """
        ...

    def getLocation() -> Location:
        """
        Gets the center location where the raid occurs.

        :return: location
        """
        ...

    def getStatus() -> 'RaidStatus':
        """
        Gets the current status of the raid.
        <br>
        Do not use this method to check if the raid has been started, call
        {@link #isStarted()} instead.

        :return: Raids status
        """
        ...

    def getSpawnedGroups() -> int:
        """
        Gets the number of raider groups which have spawned.

        :return: total spawned groups
        """
        ...

    def getTotalGroups() -> int:
        """
        Gets the number of raider groups which would spawn.
        <br>
        This also includes the group which spawns in the additional wave (if
        present).

        :return: total groups
        """
        ...

    def getTotalWaves() -> int:
        """
        Gets the number of waves in this raid (exclude the additional wave).

        :return: number of waves
        """
        ...

    def getTotalHealth() -> float:
        """
        Gets the sum of all raider's health.

        :return: total raiders health
        """
        ...

    def getHeroes() -> Set[UUID]:
        """
        Get the UUID of all heroes in this raid.

        :return: a set of unique ids
        """
        ...

    def getRaiders() -> List[Raider]:
        """
        Gets all remaining {@link Raider} in the present wave.

        :return: a list of current raiders
        """
        ...

class RaidStatus:
    """
    Represents the status of a {@link Raid}.
    """
    ONGOING = ...
    VICTORY = ...
    LOSS = ...
    STOPPED = ...
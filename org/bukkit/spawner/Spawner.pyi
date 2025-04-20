from org.bukkit.block import CreatureSpawner
from org.bukkit.entity import EntityType
from org.bukkit.entity.minecart import SpawnerMinecart
from org.bukkit.spawner import BaseSpawner
from typing import Protocol

class Spawner(Protocol):
    """
    Represents an entity spawner. <br>
    May be a {@link SpawnerMinecart} or a {@link CreatureSpawner}.
    """

    def set_delay(self, delay: int) -> None:
        """
        {@inheritDoc}
        <br>
        If set to -1, the spawn delay will be reset to a random value between
        {@link #get_min_spawn_delay} and {@link #get_max_spawn_delay()}.

        @param delay The delay.
        """

    def get_min_spawn_delay(self) -> int:
        """
        The minimum spawn delay amount (in ticks).
        <br>
        This value is used when the spawner resets its delay (for any reason).
        It will choose a random number between {@link #get_min_spawn_delay()}
        and {@link #get_max_spawn_delay()} for its next {@link #get_delay()}.
        <br>
        Default value is 200 ticks.

        @return the minimum spawn delay amount
        """

    def set_min_spawn_delay(self, delay: int) -> None:
        """
        Set the minimum spawn delay amount (in ticks).

        @param delay the minimum spawn delay amount
        @see #get_min_spawn_delay()
        """

    def get_max_spawn_delay(self) -> int:
        """
        The maximum spawn delay amount (in ticks).
        <br>
        This value is used when the spawner resets its delay (for any reason).
        It will choose a random number between {@link #get_min_spawn_delay()}
        and {@link #get_max_spawn_delay()} for its next {@link #get_delay()}.
        <br>
        This value <b>must</b> be greater than 0 and less than or equal to
        {@link #get_max_spawn_delay()}.
        <br>
        Default value is 800 ticks.

        @return the maximum spawn delay amount
        """

    def set_max_spawn_delay(self, delay: int) -> None:
        """
        Set the maximum spawn delay amount (in ticks).
        <br>
        This value <b>must</b> be greater than 0, as well as greater than or
        equal to {@link #get_min_spawn_delay()}

        @param delay the new maximum spawn delay amount
        @see #get_max_spawn_delay()
        """

    def get_spawn_count(self) -> int:
        """
        Get how many mobs attempt to spawn.
        <br>
        Default value is 4.

        @return the current spawn count
        """

    def set_spawn_count(self, spawn_count: int) -> None:
        """
        Set how many mobs attempt to spawn.

        @param spawn_count the new spawn count
        """

    def get_max_nearby_entities(self) -> int:
        """
        Set the new maximum amount of similar entities that are allowed to be
        within spawning range of this spawner.
        <br>
        If more than the maximum number of entities are within range, the spawner
        will not spawn and try again with a new {@link #get_delay()}.
        <br>
        Default value is 16.

        @return the maximum number of nearby, similar, entities
        """

    def set_max_nearby_entities(self, max_nearby_entities: int) -> None:
        """
        Set the maximum number of similar entities that are allowed to be within
        spawning range of this spawner.
        <br>
        Similar entities are entities that are of the same {@link EntityType}

        @param max_nearby_entities the maximum number of nearby, similar, entities
        """
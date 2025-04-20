from typing import Collection, List, Optional
from org.bukkit.block import CreatureSpawner
from org.bukkit.block.spawner import SpawnRule, SpawnerEntry
from org.bukkit.entity import EntitySnapshot, EntityType
from org.bukkit.entity.minecart import SpawnerMinecart
from org.jetbrains.annotations import NotNull, Nullable

"""
Represents a basic entity spawner. <br>
May be a {@link SpawnerMinecart}, {@link CreatureSpawner} or {@link TrialSpawnerConfiguration}.
"""
class BaseSpawner:

    """
    Get the spawner's creature type.

    @return The creature type or null if it not set.
    """
    def get_spawned_type(self) -> Optional[EntityType]: ...

    """
    Set the spawner's creature type. <br>
    This will override any entities that have been added with {@link #addPotentialSpawn}

    @param creatureType The creature type or null to clear.
    """
    def set_spawned_type(self, creature_type: Optional[EntityType]) -> None: ...

    """
    Get the spawner's delay.
    <br>
    This is the delay, in ticks, until the spawner will spawn its next mob.

    @return The delay.
    """
    def get_delay(self) -> int: ...

    """
    Set the spawner's delay.

    @param delay The delay.
    """
    def set_delay(self, delay: int) -> None: ...

    """
    Get the maximum distance a player can be in order for this
    spawner to be active.
    <br>
    If this value is less than or equal to 0, this spawner is always active
    (given that there are players online).
    <br>
    Default value is 16.

    @return the maximum distance a player can be in order for this
    spawner to be active.
    """
    def get_required_player_range(self) -> int: ...

    """
    Set the maximum distance a player can be in order for this
    spawner to be active.
    <br>
    Setting this value to less than or equal to 0 will make this spawner
    always active (given that there are players online).

    @param requiredPlayerRange the maximum distance a player can be
    in order for this spawner to be active.
    """
    def set_required_player_range(self, required_player_range: int) -> None: ...

    """
    Get the radius around which the spawner will attempt to spawn mobs in.
    <br>
    This area is square, includes the block the spawner is in, and is
    centered on the spawner's x,z coordinates - not the spawner itself.
    <br>
    It is 2 blocks high, centered on the spawner's y-coordinate (its bottom);
    thus allowing mobs to spawn as high as its top surface and as low
    as 1 block below its bottom surface.
    <br>
    Default value is 4.

    @return the spawn range
    """
    def get_spawn_range(self) -> int: ...

    """
    Set the new spawn range.
    <br>

    @param spawnRange the new spawn range
    @see #getSpawnRange()
    """
    def set_spawn_range(self, spawn_range: int) -> None: ...

    """
    Gets the {@link EntitySnapshot} that will be spawned by this spawner or null
    if no entities have been assigned to this spawner. <br>
    <p>
    All applicable data from the spawner will be copied, such as custom name,
    health, and velocity. <br>

    @return the entity snapshot or null if no entities have been assigned to this
            spawner.
    """
    def get_spawned_entity(self) -> Optional[EntitySnapshot]: ...

    """
    Sets the entity that will be spawned by this spawner. <br>
    This will override any previous entries that have been added with
    {@link #addPotentialSpawn}
    <p>
    All applicable data from the snapshot will be copied, such as custom name,
    health, and velocity. <br>

    @param snapshot the entity snapshot or null to clear
    """
    def set_spawned_entity(self, snapshot: Optional[EntitySnapshot]) -> None: ...

    """
    Sets the {@link SpawnerEntry} that will be spawned by this spawner. <br>
    This will override any previous entries that have been added with
    {@link #addPotentialSpawn}

    @param spawnerEntry the spawner entry to use
    """
    def set_spawned_entity(self, spawner_entry: NotNull[SpawnerEntry]) -> None: ...

    """
    Adds a new {@link EntitySnapshot} to the list of entities this spawner can
    spawn.
    <p>
    The weight will determine how often this entry is chosen to spawn, higher
    weighted entries will spawn more often than lower weighted ones. <br>
    The {@link SpawnRule} will determine under what conditions this entry can
    spawn, passing null will use the default conditions for the given entity.

    @param snapshot  the snapshot that will be spawned
    @param weight    the weight
    @param spawnRule the spawn rule for this entity, or null
    """
    def add_potential_spawn(self, snapshot: NotNull[EntitySnapshot], weight: int, spawn_rule: Optional[SpawnRule]) -> None: ...

    """
    Adds a new {@link SpawnerEntry} to the list of entities this spawner can
    spawn.

    @param spawnerEntry the spawner entry to use
    @see #addPotentialSpawn(EntitySnapshot, int, SpawnRule)
    """
    def add_potential_spawn(self, spawner_entry: NotNull[SpawnerEntry]) -> None: ...

    """
    Sets the list of {@link SpawnerEntry} this spawner can spawn. <br>
    This will override any previous entries added with
    {@link #addPotentialSpawn}

    @param entries the list of entries
    """
    def set_potential_spawns(self, entries: NotNull[Collection[SpawnerEntry]]) -> None: ...

    """
    Gets a list of potential spawns from this spawner or an empty list if no
    entities have been assigned to this spawner. <br>
    Changes made to the returned list will not be reflected in the spawner unless
    applied with {@link #setPotentialSpawns}

    @return a list of potential spawns from this spawner, or an empty list if no
            entities have been assigned to this spawner
    @see #getSpawnedType()
    """
    def get_potential_spawns(self) -> NotNull[List[SpawnerEntry]]: ...
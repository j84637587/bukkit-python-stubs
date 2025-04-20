from typing import Collection
from org.bukkit.entity import Entity, Player
from org.bukkit.spawner import TrialSpawnerConfiguration
from org.jetbrains.annotations import ApiStatus, NotNull

"""
Represents a captured state of a trial spawner.
"""
class TrialSpawner(TileState):

    """
    Gets the length in ticks the spawner will stay in cooldown for.

    @return: the number of ticks
    """
    def get_cooldown_length(self) -> int:
        ...

    """
    Sets the length in ticks the spawner will stay in cooldown for.

    @param ticks: the number of ticks
    """
    def set_cooldown_length(self, ticks: int) -> None:
        ...

    """
    Get the maximum distance a player can be in order for this
    spawner to be active.
    <br>
    If this value is less than or equal to 0, this spawner is always active
    (given that there are players online).
    <br>
    Default value is 16.

    @return: the maximum distance a player can be in order for this
    spawner to be active.
    """
    def get_required_player_range(self) -> int:
        ...

    """
    Set the maximum distance a player can be in order for this
    spawner to be active.
    <br>
    Setting this value to less than or equal to 0 will make this spawner
    always active (given that there are players online).

    @param required_player_range: the maximum distance a player can be
    in order for this spawner to be active.
    """
    def set_required_player_range(self, required_player_range: int) -> None:
        ...

    """
    Gets the players this spawner is currently tracking.
    <p>
    <b>Note:</b> the returned collection is immutable, use
    {@link #startTrackingPlayer(Player)} or {@link #stopTrackingPlayer(Player)}
    instead.

    @return: a collection of players this spawner is tracking or an empty
             collection if there aren't any
    """
        def get_tracked_players(self) -> Collection[Player]:
        ...

    """
    Checks if this spawner is currently tracking the provided player.

    @param player: the player
    @return: true if this spawner is tracking the provided player
    """
    def is_tracking_player(self, player: Player) -> bool:
        ...

    """
    Force this spawner to start tracking the provided player.
    <p>
    <b>Note:</b> the spawner may decide to stop tracking this player at any given
    time.

    @param player: the player
    """
    def start_tracking_player(self, player: Player) -> None:
        ...

    """
    Force this spawner to stop tracking the provided player.
    <p>
    <b>Note:</b> the spawner may decide to start tracking this player again at
    any given time.

    @param player: the player
    """
    def stop_tracking_player(self, player: Player) -> None:
        ...

    """
    Gets a list of entities this spawner is currently tracking.
    <p>
    <b>Note:</b> the returned collection is immutable, use
    {@link #startTrackingEntity(Entity)} or {@link #stopTrackingEntity(Entity)}
    instead.

    @return: a collection of entities this spawner is tracking or an empty
             collection if there aren't any
    """
        def get_tracked_entities(self) -> Collection[Entity]:
        ...

    """
    Checks if this spawner is currently tracking the provided entity.

    @param entity: the entity
    @return: true if this spawner is tracking the provided entity
    """
    def is_tracking_entity(self, entity: Entity) -> bool:
        ...

    """
    Force this spawner to start tracking the provided entity.
    <p>
    <b>Note:</b> the spawner may decide to stop tracking this entity at any given
    time.

    @param entity: the entity
    """
    def start_tracking_entity(self, entity: Entity) -> None:
        ...

    """
    Force this spawner to stop tracking the provided entity.
    <p>
    <b>Note:</b> the spawner may decide to start tracking this entity again at
    any given time.

    @param entity: the entity
    """
    def stop_tracking_entity(self, entity: Entity) -> None:
        ...

    """
    Checks if this spawner is using the ominous
    {@link TrialSpawnerConfiguration}.

    @return: true is using the ominous configuration
    """
    def is_ominous(self) -> bool:
        ...

    """
    Changes this spawner between the normal and ominous
    {@link TrialSpawnerConfiguration}.

    @param ominous: true to use the ominous TrialSpawnerConfiguration, false to
                    use the normal one.
    """
    def set_ominous(self, ominous: bool) -> None:
        ...

    """
    Gets the {@link TrialSpawnerConfiguration} used when {@link #isOminous()} is
    false.

    @return: the TrialSpawnerConfiguration
    """
        def get_normal_configuration(self) -> TrialSpawnerConfiguration:
        ...

    """
    Gets the {@link TrialSpawnerConfiguration} used when {@link #isOminous()} is
    true.

    @return: the TrialSpawnerConfiguration
    """
        def get_ominous_configuration(self) -> TrialSpawnerConfiguration:
        ...
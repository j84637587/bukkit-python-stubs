from typing import List, Set, Optional
from uuid import UUID
from org.bukkit import EntityEffect, Location, Nameable, Server, Sound, World, BlockFace, PistonMoveReaction
from org.bukkit.command import CommandSender
from org.bukkit.event.entity import EntityDamageEvent
from org.bukkit.event.player import TeleportCause
from org.bukkit.material import Directional
from org.bukkit.metadata import Metadatable
from org.bukkit.persistence import PersistentDataHolder
from org.bukkit.util import BoundingBox, Vector
from org.jetbrains.annotations import ApiStatus, Contract, NotNull, Nullable

"""
Represents a base entity in the world
<p>
Not all methods are guaranteed to work/may have side effects when
{@link #isInWorld()} is false.
"""
class Entity(Metadatable, CommandSender, Nameable, PersistentDataHolder):

    """
    Gets the entity's current position

    @return a new copy of Location containing the position of this entity
    """
        def get_location(self) -> Location: ...

    """
    Stores the entity's current position in the provided Location object.
    <p>
    If the provided Location is null this method does nothing and returns
    null.

    @param loc the location to copy into
    @return The Location object provided or null
    """
    @Contract("null -> null; !null -> !null")
        def get_location(self, loc: Optional[Location]) -> Optional[Location]: ...

    """
    Sets this entity's velocity in meters per tick

    @param velocity New velocity to travel with
    """
    def set_velocity(self, velocity: Vector) -> None: ...

    """
    Gets this entity's current velocity

    @return Current traveling velocity of this entity
    """
        def get_velocity(self) -> Vector: ...

    """
    Gets the entity's height

    @return height of entity
    """
    def get_height(self) -> float: ...

    """
    Gets the entity's width

    @return width of entity
    """
    def get_width(self) -> float: ...

    """
    Gets the entity's current bounding box.
    <p>
    The returned bounding box reflects the entity's current location and
    size.

    @return the entity's current bounding box
    """
        def get_bounding_box(self) -> BoundingBox: ...

    """
    Returns true if the entity is supported by a block. This value is a
    state updated by the server and is not recalculated unless the entity
    moves.

    @return True if entity is on ground.
    @see Player#isOnGround()
    """
    def is_on_ground(self) -> bool: ...

    """
    Returns true if the entity is in water.

    @return <code>true</code> if the entity is in water.
    """
    def is_in_water(self) -> bool: ...

    """
    Gets the current world this entity resides in

    @return World
    """
        def get_world(self) -> World: ...

    """
    Sets the entity's rotation.
    <p>
    Note that if the entity is affected by AI, it may override this rotation.

    @param yaw the yaw
    @param pitch the pitch
    @throws UnsupportedOperationException if used for players
    """
    def set_rotation(self, yaw: float, pitch: float) -> None: ...

    """
    Teleports this entity to the given location. If this entity is riding a
    vehicle, it will be dismounted prior to teleportation.

    @param location New location to teleport this entity to
    @return <code>true</code> if the teleport was successful
    """
    def teleport(self, location: Location) -> bool: ...

    """
    Teleports this entity to the given location. If this entity is riding a
    vehicle, it will be dismounted prior to teleportation.

    @param location New location to teleport this entity to
    @param cause The cause of this teleportation
    @return <code>true</code> if the teleport was successful
    """
    def teleport(self, location: Location, cause: TeleportCause) -> bool: ...

    """
    Teleports this entity to the target Entity. If this entity is riding a
    vehicle, it will be dismounted prior to teleportation.

    @param destination Entity to teleport this entity to
    @return <code>true</code> if the teleport was successful
    """
    def teleport(self, destination: Entity) -> bool: ...

    """
    Teleports this entity to the target Entity. If this entity is riding a
    vehicle, it will be dismounted prior to teleportation.

    @param destination Entity to teleport this entity to
    @param cause The cause of this teleportation
    @return <code>true</code> if the teleport was successful
    """
    def teleport(self, destination: Entity, cause: TeleportCause) -> bool: ...

    """
    Returns a list of entities within a bounding box centered around this
    entity

    @param x 1/2 the size of the box along x axis
    @param y 1/2 the size of the box along y axis
    @param z 1/2 the size of the box along z axis
    @return {@code List<Entity>} List of entities nearby
    """
        def get_nearby_entities(self, x: float, y: float, z: float) -> List[Entity]: ...

    """
    Returns a unique id for this entity

    @return Entity id
    """
    def get_entity_id(self) -> int: ...

    """
    Returns the entity's current fire ticks (ticks before the entity stops
    being on fire).

    @return int fireTicks
    """
    def get_fire_ticks(self) -> int: ...

    """
    Returns the entity's maximum fire ticks.

    @return int maxFireTicks
    """
    def get_max_fire_ticks(self) -> int: ...

    """
    Sets the entity's current fire ticks (ticks before the entity stops
    being on fire).

    @param ticks Current ticks remaining
    """
    def set_fire_ticks(self, ticks: int) -> None: ...

    """
    Sets if the entity has visual fire (it will always appear to be on fire).

    @param fire whether visual fire is enabled
    """
    def set_visual_fire(self, fire: bool) -> None: ...

    """
    Gets if the entity has visual fire (it will always appear to be on fire).

    @return whether visual fire is enabled
    """
    def is_visual_fire(self) -> bool: ...

    """
    Returns the entity's current freeze ticks (amount of ticks the entity has
    been in powdered snow).

    @return int freeze ticks
    """
    def get_freeze_ticks(self) -> int: ...

    """
    Returns the entity's maximum freeze ticks (amount of ticks before it will
    be fully frozen)

    @return int max freeze ticks
    """
    def get_max_freeze_ticks(self) -> int: ...

    """
    Sets the entity's current freeze ticks (amount of ticks the entity has
    been in powdered snow).

    @param ticks Current ticks
    """
    def set_freeze_ticks(self, ticks: int) -> None: ...

    """
    Gets if the entity is fully frozen (it has been in powdered snow for max
    freeze ticks).

    @return freeze status
    """
    def is_frozen(self) -> bool: ...

    """
    Mark the entity's removal.

    @throws UnsupportedOperationException if you try to remove a {@link Player} use {@link Player#kickPlayer(String)} in this case instead
    """
    def remove(self) -> None: ...

    """
    Returns true if this entity has been marked for removal.

    @return True if it is dead.
    """
    def is_dead(self) -> bool: ...

    """
    Returns false if the entity has died, been despawned for some other
    reason, or has not been added to the world.

    @return True if valid.
    """
    def is_valid(self) -> bool: ...

    """
    Gets the {@link Server} that contains this Entity

    @return Server instance running this Entity
    """
    @Override
        def get_server(self) -> Server: ...

    """
    Returns true if the entity gets persisted.
    <p>
    By default all entities are persistent. An entity will also not get
    persisted, if it is riding an entity that is not persistent.
    <p>
    The persistent flag on players controls whether or not to save their
    playerdata file when they quit. If a player is directly or indirectly
    riding a non-persistent entity, the vehicle at the root and all its
    passengers won't get persisted.
    <p>
    <b>This should not be confused with
    {@link LivingEntity#setRemoveWhenFarAway(boolean)} which controls
    despawning of living entities. </b>

    @return true if this entity is persistent
    """
    def is_persistent(self) -> bool: ...

    """
    Sets whether or not the entity gets persisted.

    @param persistent the persistence status
    @see #isPersistent()
    """
    def set_persistent(self, persistent: bool) -> None: ...

    """
    Gets the primary passenger of a vehicle. For vehicles that could have
    multiple passengers, this will only return the primary passenger.

    @return an entity
    @deprecated entities may have multiple passengers, use
    {@link #getPassengers()}
    """
    @Deprecated(since="1.11.2")
        def get_passenger(self) -> Optional[Entity]: ...

    """
    Set the passenger of a vehicle.

    @param passenger The new passenger.
    @return false if it could not be done for whatever reason
    @deprecated entities may have multiple passengers, use
    {@link #addPassenger(org.bukkit.entity.Entity)}
    """
    @Deprecated(since="1.11.2")
    def set_passenger(self, passenger: Entity) -> bool: ...

    """
    Gets a list of passengers of this vehicle.
    <p>
    The returned list will not be directly linked to the entity's current
    passengers, and no guarantees are made as to its mutability.

    @return list of entities corresponding to current passengers.
    """
        def get_passengers(self) -> List[Entity]: ...

    """
    Add a passenger to the vehicle.

    @param passenger The passenger to add
    @return false if it could not be done for whatever reason
    """
    def add_passenger(self, passenger: Entity) -> bool: ...

    """
    Remove a passenger from the vehicle.

    @param passenger The passenger to remove
    @return false if it could not be done for whatever reason
    """
    def remove_passenger(self, passenger: Entity) -> bool: ...

    """
    Check if a vehicle has passengers.

    @return True if the vehicle has no passengers.
    """
    def is_empty(self) -> bool: ...

    """
    Eject any passenger.

    @return True if there was a passenger.
    """
    def eject(self) -> bool: ...

    """
    Returns the distance this entity has fallen

    @return The distance.
    """
    def get_fall_distance(self) -> float: ...

    """
    Sets the fall distance for this entity

    @param distance The new distance.
    """
    def set_fall_distance(self, distance: float) -> None: ...

    """
    Record the last {@link EntityDamageEvent} inflicted on this entity

    @param event a {@link EntityDamageEvent}
    @deprecated method is for internal use only and will be removed
    """
    @Deprecated(since="1.20.4", forRemoval=True)
    def set_last_damage_cause(self, event: Optional[EntityDamageEvent]) -> None: ...

    """
    Retrieve the last {@link EntityDamageEvent} inflicted on this entity.
    This event may have been cancelled.

    @return the last known {@link EntityDamageEvent} or null if hitherto
        unharmed
    """
        def get_last_damage_cause(self) -> Optional[EntityDamageEvent]: ...

    """
    Returns a unique and persistent id for this entity

    @return unique id
    """
        def get_unique_id(self) -> UUID: ...

    """
    Gets the amount of ticks this entity has lived for.
    <p>
    This is the equivalent to "age" in entities.

    @return Age of entity
    """
    def get_ticks_lived(self) -> int: ...

    """
    Sets the amount of ticks this entity has lived for.
    <p>
    This is the equivalent to "age" in entities. May not be less than one
    tick.

    @param value Age of entity
    """
    def set_ticks_lived(self, value: int) -> None: ...

    """
    Performs the specified {@link EntityEffect} for this entity.
    <p>
    This will be viewable to all players near the entity.
    <p>
    If the effect is not applicable to this class of entity, it will not play.

    @param type Effect to play.
    """
    def play_effect(self, type: EntityEffect) -> None: ...

    """
    Get the type of the entity.

    @return The entity type.
    """
        def get_type(self) -> EntityType: ...

    """
    Get the {@link Sound} this entity makes while swimming.

    @return the swimming sound
    """
        def get_swim_sound(self) -> Sound: ...

    """
    Get the {@link Sound} this entity makes when splashing in water. For most
    entities, this is just {@link Sound#ENTITY_GENERIC_SPLASH}.

    @return the splash sound
    """
        def get_swim_splash_sound(self) -> Sound: ...

    """
    Get the {@link Sound} this entity makes when splashing in water at high
    speeds. For most entities, this is just {@link Sound#ENTITY_GENERIC_SPLASH}.

    @return the splash sound
    """
        def get_swim_high_speed_splash_sound(self) -> Sound: ...

    """
    Returns whether this entity is inside a vehicle.

    @return True if the entity is in a vehicle.
    """
    def is_inside_vehicle(self) -> bool: ...

    """
    Leave the current vehicle. If the entity is currently in a vehicle (and
    is removed from it), true will be returned, otherwise false will be
    returned.

    @return True if the entity was in a vehicle.
    """
    def leave_vehicle(self) -> bool: ...

    """
    Get the vehicle that this entity is inside. If there is no vehicle,
    null will be returned.

    @return The current vehicle.
    """
        def get_vehicle(self) -> Optional[Entity]: ...

    """
    Sets whether or not to display the mob's custom name client side. The
    name will be displayed above the mob similarly to a player.
    <p>
    This value has no effect on players, they will always display their
    name.

    @param flag custom name or not
    """
    def set_custom_name_visible(self, flag: bool) -> None: ...

    """
    Gets whether or not the mob's custom name is displayed client side.
    <p>
    This value has no effect on players, they will always display their
    name.

    @return if the custom name is displayed
    """
    def is_custom_name_visible(self) -> bool: ...

    """
    Sets whether or not this entity is visible by default.

    If this entity is not visible by default, then
    {@link Player#showEntity(org.bukkit.plugin.Plugin, org.bukkit.entity.Entity)}
    will need to be called before the entity is visible to a given player.

    @param visible default visibility status
    """
    def set_visible_by_default(self, visible: bool) -> None: ...

    """
    Gets whether or not this entity is visible by default.

    If this entity is not visible by default, then
    {@link Player#showEntity(org.bukkit.plugin.Plugin, org.bukkit.entity.Entity)}
    will need to be called before the entity is visible to a given player.

    @return default visibility status
    """
    def is_visible_by_default(self) -> bool: ...

    """
    Get all players that are currently tracking this entity.
    <p>
    'Tracking' means that this entity has been sent to the player and that
    they are receiving updates on its state. Note that the client's {@code
    'Entity Distance'} setting does not affect the range at which entities
    are tracked.

    @return the players tracking this entity, or an empty set if none
    """
        def get_tracked_by(self) -> Set[Player]: ...

    """
    Sets whether the entity has a team colored (default: white) glow.
    <b>nb: this refers to the 'Glowing' entity property, not whether a
    glowing potion effect is applied</b>

    @param flag if the entity is glowing
    """
    def set_glowing(self, flag: bool) -> None: ...

    """
    Gets whether the entity is glowing or not.
    <b>nb: this refers to the 'Glowing' entity property, not whether a
    glowing potion effect is applied</b>

    @return whether the entity is glowing
    """
    def is_glowing(self) -> bool: ...

    """
    Sets whether the entity is invulnerable or not.
    <p>
    When an entity is invulnerable it can only be damaged by players in
    creative mode.

    @param flag if the entity is invulnerable
    """
    def set_invulnerable(self, flag: bool) -> None: ...

    """
    Gets whether the entity is invulnerable or not.

    @return whether the entity is
    """
    def is_invulnerable(self) -> bool: ...

    """
    Gets whether the entity is silent or not.

    @return whether the entity is silent.
    """
    def is_silent(self) -> bool: ...

    """
    Sets whether the entity is silent or not.
    <p>
    When an entity is silent it will not produce any sound.

    @param flag if the entity is silent
    """
    def set_silent(self, flag: bool) -> None: ...

    """
    Returns whether gravity applies to this entity.

    @return whether gravity applies
    """
    def has_gravity(self) -> bool: ...

    """
    Sets whether gravity applies to this entity.

    @param gravity whether gravity should apply
    """
    def set_gravity(self, gravity: bool) -> None: ...

    """
    Gets the period of time (in ticks) before this entity can use a portal.

    @return portal cooldown ticks
    """
    def get_portal_cooldown(self) -> int: ...

    """
    Sets the period of time (in ticks) before this entity can use a portal.

    @param cooldown portal cooldown ticks
    """
    def set_portal_cooldown(self, cooldown: int) -> None: ...

    """
    Returns a set of tags for this entity.
    <br>
    Entities can have no more than 1024 tags.

    @return a set of tags for this entity
    """
        def get_scoreboard_tags(self) -> Set[str]: ...

    """
    Add a tag to this entity.
    <br>
    Entities can have no more than 1024 tags.

    @param tag the tag to add
    @return true if the tag was successfully added
    """
    def add_scoreboard_tag(self, tag: str) -> bool: ...

    """
    Removes a given tag from this entity.

    @param tag the tag to remove
    @return true if the tag was successfully removed
    """
    def remove_scoreboard_tag(self, tag: str) -> bool: ...

    """
    Returns the reaction of the entity when moved by a piston.

    @return reaction
    """
        def get_piston_move_reaction(self) -> PistonMoveReaction: ...

    """
    Get the closest cardinal {@link BlockFace} direction an entity is
    currently facing.
    <br>
    This will not return any non-cardinal directions such as
    {@link BlockFace#UP} or {@link BlockFace#DOWN}.
    <br>
    {@link Hanging} entities will override this call and thus their behavior
    may be different.

    @return the entity's current cardinal facing.
    @see Hanging
    @see Directional#getFacing()
    """
        def get_facing(self) -> BlockFace: ...

    """
    Gets the entity's current pose.

    <b>Note that the pose is only updated at the end of a tick, so may be
    inconsistent with other methods. eg {@link Player#isSneaking()} being
    true does not imply the current pose will be {@link Pose#SNEAKING}</b>

    @return current pose
    """
        def get_pose(self) -> Pose: ...

    """
    Get the category of spawn to which this entity belongs.

    @return the entity´s category spawn
    """
        def get_spawn_category(self) -> SpawnCategory: ...

    """
    Checks if this entity has been spawned in a world. <br>
    Entities not spawned in a world will not tick, be sent to players, or be
    saved to the server files.

    @return whether the entity has been spawned in a world
    """
    def is_in_world(self) -> bool: ...

    """
    Get this entity as an NBT string.
    <p>
    This string should not be relied upon as a serializable value.

    @return the NBT string or null if one cannot be made
    """
            def get_as_string(self) -> Optional[str]: ...

    """
    Crates an {@link EntitySnapshot} representing the current state of this entity.

    @return a snapshot representing this entity or null if one cannot be made
    """
            def create_snapshot(self) -> Optional[EntitySnapshot]: ...

    """
    Creates a copy of this entity and all its data. Does not spawn the copy in
    the world. <br>
    <b>Note:</b> Players cannot be copied.

    @return a copy of this entity.
    """
            def copy(self) -> Entity: ...

    """
    Creates a copy of this entity and all its data. Spawns the copy at the given location. <br>
    <b>Note:</b> Players cannot be copied.
    @param to the location to copy to
    @return a copy of this entity.
    """
            def copy(self, to: Location) -> Entity: ...
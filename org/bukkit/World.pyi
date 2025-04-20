from typing import Collection, Dict, List, Map, Optional, Set, TypeVar, Callable, Union

T = TypeVar('T')

class World(RegionAccessor, WorldInfo, PluginMessageRecipient, Metadatable, PersistentDataHolder, Keyed):
    """
    Represents a world, which may contain entities, chunks and blocks
    """

    def get_block_at(self, x: int, y: int, z: int) -> Block:
        """
        Gets the Block at the given coordinates

        :param x: X-coordinate of the block
        :param y: Y-coordinate of the block
        :param z: Z-coordinate of the block
        :return: Block at the given coordinates
        """
        pass

    def get_block_at(self, location: Location) -> Block:
        """
        Gets the Block at the given Location

        :param location: Location of the block
        :return: Block at the given location
        """
        pass

    def get_highest_block_at(self, x: int, z: int) -> Block:
        """
        Gets the highest non-empty (impassable) block at the given coordinates.

        :param x: X-coordinate of the block
        :param z: Z-coordinate of the block
        :return: Highest non-empty block
        """
        pass

    def get_highest_block_at(self, location: Location) -> Block:
        """
        Gets the highest non-empty (impassable) block at the given coordinates.

        :param location: Coordinates to get the highest block
        :return: Highest non-empty block
        """
        pass

    def get_highest_block_at(self, x: int, z: int, height_map: HeightMap) -> Block:
        """
        Gets the highest block corresponding to the HeightMap at the given coordinates.

        :param x: X-coordinate of the block
        :param z: Z-coordinate of the block
        :param height_map: the heightMap that is used to determine the highest point
        :return: Highest block corresponding to the HeightMap
        """
        pass

    def get_highest_block_at(self, location: Location, height_map: HeightMap) -> Block:
        """
        Gets the highest block corresponding to the HeightMap at the given coordinates.

        :param location: Coordinates to get the highest block
        :param height_map: the heightMap that is used to determine the highest point
        :return: Highest block corresponding to the HeightMap
        """
        pass

    def get_chunk_at(self, x: int, z: int) -> Chunk:
        """
        Gets the Chunk at the given coordinates

        :param x: X-coordinate of the chunk
        :param z: Z-coordinate of the chunk
        :return: Chunk at the given coordinates
        """
        pass

    def get_chunk_at(self, x: int, z: int, generate: bool) -> Chunk:
        """
        Gets the Chunk at the given coordinates

        :param x: X-coordinate of the chunk
        :param z: Z-coordinate of the chunk
        :param generate: Whether the chunk should be fully generated or not
        :return: Chunk at the given coordinates
        """
        pass

    def get_chunk_at(self, location: Location) -> Chunk:
        """
        Gets the Chunk at the given Location

        :param location: Location of the chunk
        :return: Chunk at the given location
        """
        pass

    def get_chunk_at(self, block: Block) -> Chunk:
        """
        Gets the Chunk that contains the given Block

        :param block: Block to get the containing chunk from
        :return: The chunk that contains the given block
        """
        pass

    def is_chunk_loaded(self, chunk: Chunk) -> bool:
        """
        Checks if the specified Chunk is loaded

        :param chunk: The chunk to check
        :return: true if the chunk is loaded, otherwise false
        """
        pass

    def get_loaded_chunks(self) -> List[Chunk]:
        """
        Gets an array of all loaded Chunks

        :return: Chunk[] containing all loaded chunks
        """
        pass

    def load_chunk(self, chunk: Chunk) -> None:
        """
        Loads the specified Chunk.

        :param chunk: The chunk to load
        """
        pass

    def is_chunk_loaded(self, x: int, z: int) -> bool:
        """
        Checks if the Chunk at the specified coordinates is loaded

        :param x: X-coordinate of the chunk
        :param z: Z-coordinate of the chunk
        :return: true if the chunk is loaded, otherwise false
        """
        pass

    def is_chunk_generated(self, x: int, z: int) -> bool:
        """
        Checks if the Chunk at the specified coordinates is generated

        :param x: X-coordinate of the chunk
        :param z: Z-coordinate of the chunk
        :return: true if the chunk is generated, otherwise false
        """
        pass

    def is_chunk_in_use(self, x: int, z: int) -> bool:
        """
        Checks if the Chunk at the specified coordinates is loaded and in use by one or more players

        :param x: X-coordinate of the chunk
        :param z: Z-coordinate of the chunk
        :return: true if the chunk is loaded and in use by one or more players, otherwise false
        """
        pass

    def load_chunk(self, x: int, z: int) -> None:
        """
        Loads the Chunk at the specified coordinates.

        :param x: X-coordinate of the chunk
        :param z: Z-coordinate of the chunk
        """
        pass

    def load_chunk(self, x: int, z: int, generate: bool) -> bool:
        """
        Loads the Chunk at the specified coordinates.

        :param x: X-coordinate of the chunk
        :param z: Z-coordinate of the chunk
        :param generate: Whether or not to generate a chunk if it doesn't already exist
        :return: true if the chunk has loaded successfully, otherwise false
        """
        pass

    def unload_chunk(self, chunk: Chunk) -> bool:
        """
        Safely unloads and saves the Chunk at the specified coordinates

        :param chunk: the chunk to unload
        :return: true if the chunk has unloaded successfully, otherwise false
        """
        pass

    def unload_chunk(self, x: int, z: int) -> bool:
        """
        Safely unloads and saves the Chunk at the specified coordinates

        :param x: X-coordinate of the chunk
        :param z: Z-coordinate of the chunk
        :return: true if the chunk has unloaded successfully, otherwise false
        """
        pass

    def unload_chunk(self, x: int, z: int, save: bool) -> bool:
        """
        Safely unloads and optionally saves the Chunk at the specified coordinates.

        :param x: X-coordinate of the chunk
        :param z: Z-coordinate of the chunk
        :param save: Whether or not to save the chunk
        :return: true if the chunk has unloaded successfully, otherwise false
        """
        pass

    def unload_chunk_request(self, x: int, z: int) -> bool:
        """
        Safely queues the Chunk at the specified coordinates for unloading.

        :param x: X-coordinate of the chunk
        :param z: Z-coordinate of the chunk
        :return: true if the queue attempt was successful, otherwise false
        """
        pass

    def regenerate_chunk(self, x: int, z: int) -> bool:
        """
        Regenerates the Chunk at the specified coordinates

        :param x: X-coordinate of the chunk
        :param z: Z-coordinate of the chunk
        :return: Whether the chunk was actually regenerated
        """
        pass

    def refresh_chunk(self, x: int, z: int) -> bool:
        """
        Resends the Chunk to all clients

        :param x: X-coordinate of the chunk
        :param z: Z-coordinate of the chunk
        :return: Whether the chunk was actually refreshed
        """
        pass

    def get_players_seeing_chunk(self, chunk: Chunk) -> Collection[Player]:
        """
        Get a list of all players who can view the specified chunk from their client

        :param chunk: the chunk to check
        :return: collection of players who can see the chunk
        """
        pass

    def get_players_seeing_chunk(self, x: int, z: int) -> Collection[Player]:
        """
        Get a list of all players who can view the specified chunk from their client

        :param x: X-coordinate of the chunk
        :param z: Z-coordinate of the chunk
        :return: collection of players who can see the chunk
        """
        pass

    def is_chunk_force_loaded(self, x: int, z: int) -> bool:
        """
        Gets whether the chunk at the specified chunk coordinates is force loaded.

        :param x: X-coordinate of the chunk
        :param z: Z-coordinate of the chunk
        :return: force load status
        """
        pass

    def set_chunk_force_loaded(self, x: int, z: int, forced: bool) -> None:
        """
        Sets whether the chunk at the specified chunk coordinates is force loaded.

        :param x: X-coordinate of the chunk
        :param z: Z-coordinate of the chunk
        :param forced: force load status
        """
        pass

    def get_force_loaded_chunks(self) -> Collection[Chunk]:
        """
        Returns all force loaded chunks in this world.

        :return: unmodifiable collection of force loaded chunks
        """
        pass

    def add_plugin_chunk_ticket(self, x: int, z: int, plugin: Plugin) -> bool:
        """
        Adds a plugin ticket for the specified chunk, loading the chunk if it is not already loaded.

        :param x: X-coordinate of the chunk
        :param z: Z-coordinate of the chunk
        :param plugin: Plugin which owns the ticket
        :return: true if a plugin ticket was added, false if the ticket already exists for the plugin
        :raises IllegalStateException: If the specified plugin is not enabled
        """
        pass

    def remove_plugin_chunk_ticket(self, x: int, z: int, plugin: Plugin) -> bool:
        """
        Removes the specified plugin's ticket for the specified chunk

        :param x: X-coordinate of the chunk
        :param z: Z-coordinate of the chunk
        :param plugin: Plugin which owns the ticket
        :return: true if the plugin ticket was removed, false if there is no plugin ticket for the chunk
        """
        pass

    def remove_plugin_chunk_tickets(self, plugin: Plugin) -> None:
        """
        Removes all plugin tickets for the specified plugin

        :param plugin: Specified plugin
        """
        pass

    def get_plugin_chunk_tickets(self, x: int, z: int) -> Collection[Plugin]:
        """
        Retrieves a collection specifying which plugins have tickets for the specified chunk.

        :param x: X-coordinate of the chunk
        :param z: Z-coordinate of the chunk
        :return: unmodifiable collection containing which plugins have tickets for the chunk
        """
        pass

    def get_plugin_chunk_tickets(self) -> Map[Plugin, Collection[Chunk]]:
        """
        Returns a map of which plugins have tickets for what chunks.

        :return: unmodifiable map containing which plugins have tickets for what chunks
        """
        pass

    def get_intersecting_chunks(self, box: BoundingBox) -> Collection[Chunk]:
        """
        Gets all Chunks intersecting the given BoundingBox.

        :param box: BoundingBox to check
        :return: A collection of Chunks intersecting the given BoundingBox
        """
        pass

    def drop_item(self, location: Location, item: ItemStack) -> Item:
        """
        Drops an item at the specified Location

        :param location: Location to drop the item
        :param item: ItemStack to drop
        :return: ItemDrop entity created as a result of this method
        """
        pass

    def drop_item(self, location: Location, item: ItemStack, function: Optional[Callable[[Item], None]]) -> Item:
        """
        Drops an item at the specified Location

        :param location: Location to drop the item
        :param item: ItemStack to drop
        :param function: the function to be run before the entity is spawned.
        :return: ItemDrop entity created as a result of this method
        """
        pass

    def drop_item_naturally(self, location: Location, item: ItemStack) -> Item:
        """
        Drops an item at the specified Location with a random offset

        :param location: Location to drop the item
        :param item: ItemStack to drop
        :return: ItemDrop entity created as a result of this method
        """
        pass

    def drop_item_naturally(self, location: Location, item: ItemStack, function: Optional[Callable[[Item], None]]) -> Item:
        """
        Drops an item at the specified Location with a random offset

        :param location: Location to drop the item
        :param item: ItemStack to drop
        :param function: the function to be run before the entity is spawned.
        :return: ItemDrop entity created as a result of this method
        """
        pass

    def spawn_arrow(self, location: Location, direction: Vector, speed: float, spread: float) -> Arrow:
        """
        Creates an Arrow entity at the given Location

        :param location: Location to spawn the arrow
        :param direction: Direction to shoot the arrow in
        :param speed: Speed of the arrow. A recommend speed is 0.6
        :param spread: Spread of the arrow. A recommend spread is 12
        :return: Arrow entity spawned as a result of this method
        """
        pass

    def spawn_arrow(self, location: Location, direction: Vector, speed: float, spread: float, clazz: Type[T]) -> T:
        """
        Creates an arrow entity of the given class at the given Location

        :param location: Location to spawn the arrow
        :param direction: Direction to shoot the arrow in
        :param speed: Speed of the arrow. A recommend speed is 0.6
        :param spread: Spread of the arrow. A recommend spread is 12
        :param clazz: the Entity class for the arrow
        :return: Arrow entity spawned as a result of this method
        """
        pass

    def generate_tree(self, location: Location, type: TreeType) -> bool:
        """
        Creates a tree at the given Location

        :param location: Location to spawn the tree
        :param type: Type of the tree to create
        :return: true if the tree was created successfully, otherwise false
        """
        pass

    def generate_tree(self, loc: Location, type: TreeType, delegate: BlockChangeDelegate) -> bool:
        """
        Creates a tree at the given Location

        :param loc: Location to spawn the tree
        :param type: Type of the tree to create
        :param delegate: A class to call for each block changed as a result of this method
        :return: true if the tree was created successfully, otherwise false
        """
        pass

    def strike_lightning(self, loc: Location) -> LightningStrike:
        """
        Strikes lightning at the given Location

        :param loc: The location to strike lightning
        :return: The lightning entity.
        """
        pass

    def strike_lightning_effect(self, loc: Location) -> LightningStrike:
        """
        Strikes lightning at the given Location without doing damage

        :param loc: The location to strike lightning
        :return: The lightning entity.
        """
        pass

    def get_entities(self) -> List[Entity]:
        """
        Get a list of all entities in this World

        :return: A List of all Entities currently residing in this world
        """
        pass

    def get_living_entities(self) -> List[LivingEntity]:
        """
        Get a list of all living entities in this World

        :return: A List of all LivingEntities currently residing in this world
        """
        pass

    def get_entities_by_class(self, classes: List[Type[T]]) -> Collection[T]:
        """
        Get a collection of all entities in this World matching the given class/interface

        :param classes: The classes representing the types of entity to match
        :return: A List of all Entities currently residing in this world that match the given class/interface
        """
        pass

    def get_entities_by_class(self, cls: Type[T]) -> Collection[T]:
        """
        Get a collection of all entities in this World matching the given class/interface

        :param cls: The class representing the type of entity to match
        :return: A List of all Entities currently residing in this world that match the given class/interface
        """
        pass

    def get_entities_by_classes(self, classes: List[Type]) -> Collection[Entity]:
        """
        Get a collection of all entities in this World matching any of the given classes/interfaces

        :param classes: The classes representing the types of entity to match
        :return: A List of all Entities currently residing in this world that match one or more of the given classes/interfaces
        """
        pass

    def get_players(self) -> List[Player]:
        """
        Get a list of all players in this World

        :return: A list of all Players currently residing in this world
        """
        pass

    def get_nearby_entities(self, location: Location, x: float, y: float, z: float) -> Collection[Entity]:
        """
        Returns a list of entities within a bounding box centered around a Location.

        :param location: The center of the bounding box
        :param x: 1/2 the size of the box along x axis
        :param y: 1/2 the size of the box along y axis
        :param z: 1/2 the size of the box along z axis
        :return: the collection of entities near location. This will always be a non-null collection.
        """
        pass

    def get_nearby_entities(self, location: Location, x: float, y: float, z: float, filter: Optional[Callable[[Entity], bool]]) -> Collection[Entity]:
        """
        Returns a list of entities within a bounding box centered around a Location.

        :param location: The center of the bounding box
        :param x: 1/2 the size of the box along x axis
        :param y: 1/2 the size of the box along y axis
        :param z: 1/2 the size of the box along z axis
        :param filter: only entities that fulfill this predicate are considered, or null to consider all entities
        :return: the collection of entities near location. This will always be a non-null collection.
        """
        pass

    def get_nearby_entities(self, bounding_box: BoundingBox) -> Collection[Entity]:
        """
        Returns a list of entities within the given bounding box.

        :param bounding_box: the bounding box
        :return: the collection of entities within the bounding box, will always be a non-null collection
        """
        pass

    def get_nearby_entities(self, bounding_box: BoundingBox, filter: Optional[Callable[[Entity], bool]]) -> Collection[Entity]:
        """
        Returns a list of entities within the given bounding box.

        :param bounding_box: the bounding box
        :param filter: only entities that fulfill this predicate are considered, or null to consider all entities
        :return: the collection of entities within the bounding box, will always be a non-null collection
        """
        pass

    def ray_trace_entities(self, start: Location, direction: Vector, max_distance: float) -> Optional[RayTraceResult]:
        """
        Performs a ray trace that checks for entity collisions.

        :param start: the start position
        :param direction: the ray direction
        :param max_distance: the maximum distance
        :return: the closest ray trace hit result, or null if there is no hit
        """
        pass

    def ray_trace_entities(self, start: Location, direction: Vector, max_distance: float, ray_size: float) -> Optional[RayTraceResult]:
        """
        Performs a ray trace that checks for entity collisions.

        :param start: the start position
        :param direction: the ray direction
        :param max_distance: the maximum distance
        :param ray_size: entity bounding boxes will be uniformly expanded (or shrunk) by this value before doing collision checks
        :return: the closest ray trace hit result, or null if there is no hit
        """
        pass

    def ray_trace_entities(self, start: Location, direction: Vector, max_distance: float, filter: Optional[Callable[[Entity], bool]]) -> Optional[RayTraceResult]:
        """
        Performs a ray trace that checks for entity collisions.

        :param start: the start position
        :param direction: the ray direction
        :param max_distance: the maximum distance
        :param filter: only entities that fulfill this predicate are considered, or null to consider all entities
        :return: the closest ray trace hit result, or null if there is no hit
        """
        pass

    def ray_trace_blocks(self, start: Location, direction: Vector, max_distance: float) -> Optional[RayTraceResult]:
        """
        Performs a ray trace that checks for block collisions using the blocks' precise collision shapes.

        :param start: the start location
        :param direction: the ray direction
        :param max_distance: the maximum distance
        :return: the ray trace hit result, or null if there is no hit
        """
        pass

    def ray_trace_blocks(self, start: Location, direction: Vector, max_distance: float, fluid_collision_mode: FluidCollisionMode) -> Optional[RayTraceResult]:
        """
        Performs a ray trace that checks for block collisions using the blocks' precise collision shapes.

        :param start: the start location
        :param direction: the ray direction
        :param max_distance: the maximum distance
        :param fluid_collision_mode: the fluid collision mode
        :return: the ray trace hit result, or null if there is no hit
        """
        pass

    def ray_trace_blocks(self, start: Location, direction: Vector, max_distance: float, fluid_collision_mode: FluidCollisionMode, ignore_passable_blocks: bool) -> Optional[RayTraceResult]:
        """
        Performs a ray trace that checks for block collisions using the blocks' precise collision shapes.

        :param start: the start location
        :param direction: the ray direction
        :param max_distance: the maximum distance
        :param fluid_collision_mode: the fluid collision mode
        :param ignore_passable_blocks: whether to ignore passable but collidable blocks
        :return: the ray trace hit result, or null if there is no hit
        """
        pass

    def ray_trace(self, start: Location, direction: Vector, max_distance: float, fluid_collision_mode: FluidCollisionMode, ignore_passable_blocks: bool, ray_size: float, filter: Optional[Callable[[Entity], bool]]) -> Optional[RayTraceResult]:
        """
        Performs a ray trace that checks for both block and entity collisions.

        :param start: the start location
        :param direction: the ray direction
        :param max_distance: the maximum distance
        :param fluid_collision_mode: the fluid collision mode
        :param ignore_passable_blocks: whether to ignore passable but collidable blocks
        :param ray_size: entity bounding boxes will be uniformly expanded (or shrunk) by this value before doing collision checks
        :param filter: only entities that fulfill this predicate are considered, or null to consider all entities
        :return: the closest ray trace hit result with either a block or an entity, or null if there is no hit
        """
        pass

    def get_spawn_location(self) -> Location:
        """
        Gets the default spawn Location of this world

        :return: The spawn location of this world
        """
        pass

    def set_spawn_location(self, location: Location) -> bool:
        """
        Sets the spawn location of the world.

        :param location: The Location to set the spawn for this world at.
        :return: True if it was successfully set.
        """
        pass

    def set_spawn_location(self, x: int, y: int, z: int, angle: float) -> bool:
        """
        Sets the spawn location of the world

        :param x: X coordinate
        :param y: Y coordinate
        :param z: Z coordinate
        :param angle: the angle
        :return: True if it was successfully set.
        """
        pass

    def set_spawn_location(self, x: int, y: int, z: int) -> bool:
        """
        Sets the spawn location of the world

        :param x: X coordinate
        :param y: Y coordinate
        :param z: Z coordinate
        :return: True if it was successfully set.
        """
        pass

    def get_time(self) -> int:
        """
        Gets the relative in-game time of this world.

        :return: The current relative time
        """
        pass

    def set_time(self, time: int) -> None:
        """
        Sets the relative in-game time on the server.

        :param time: The new relative time to set the in-game time to (in hours*1000)
        """
        pass

    def get_full_time(self) -> int:
        """
        Gets the full in-game time on this world

        :return: The current absolute time
        """
        pass

    def set_full_time(self, time: int) -> None:
        """
        Sets the in-game time on the server

        :param time: The new absolute time to set this world to
        """
        pass

    def get_game_time(self) -> int:
        """
        Gets the full in-game time on this world since the world generation

        :return: The current absolute time since the world generation
        """
        pass

    def has_storm(self) -> bool:
        """
        Returns whether the world has an ongoing storm.

        :return: Whether there is an ongoing storm
        """
        pass

    def set_storm(self, has_storm: bool) -> None:
        """
        Set whether there is a storm.

        :param has_storm: Whether there is rain and snow
        """
        pass

    def get_weather_duration(self) -> int:
        """
        Get the remaining time in ticks of the current conditions.

        :return: Time in ticks
        """
        pass

    def set_weather_duration(self, duration: int) -> None:
        """
        Set the remaining time in ticks of the current conditions.

        :param duration: Time in ticks
        """
        pass

    def is_thundering(self) -> bool:
        """
        Returns whether there is thunder.

        :return: Whether there is thunder
        """
        pass

    def set_thundering(self, thundering: bool) -> None:
        """
        Set whether it is thundering.

        :param thundering: Whether it is thundering
        """
        pass

    def get_thunder_duration(self) -> int:
        """
        Get the thundering duration.

        :return: Duration in ticks
        """
        pass

    def set_thunder_duration(self, duration: int) -> None:
        """
        Set the thundering duration.

        :param duration: Duration in ticks
        """
        pass

    def is_clear_weather(self) -> bool:
        """
        Returns whether the world has clear weather.

        :return: true if clear weather
        """
        pass

    def set_clear_weather_duration(self, duration: int) -> None:
        """
        Set the clear weather duration.

        :param duration: duration in ticks
        """
        pass

    def get_clear_weather_duration(self) -> int:
        """
        Get the clear weather duration.

        :return: duration in ticks
        """
        pass

    def create_explosion(self, x: float, y: float, z: float, power: float) -> bool:
        """
        Creates explosion at given coordinates with given power

        :param x: X coordinate
        :param y: Y coordinate
        :param z: Z coordinate
        :param power: The power of explosion, where 4F is TNT
        :return: false if explosion was canceled, otherwise true
        """
        pass

    def create_explosion(self, x: float, y: float, z: float, power: float, set_fire: bool) -> bool:
        """
        Creates explosion at given coordinates with given power and optionally setting blocks on fire.

        :param x: X coordinate
        :param y: Y coordinate
        :param z: Z coordinate
        :param power: The power of explosion, where 4F is TNT
        :param set_fire: Whether or not to set blocks on fire
        :return: false if explosion was canceled, otherwise true
        """
        pass

    def create_explosion(self, x: float, y: float, z: float, power: float, set_fire: bool, break_blocks: bool) -> bool:
        """
        Creates explosion at given coordinates with given power and optionally setting blocks on fire or breaking blocks.

        :param x: X coordinate
        :param y: Y coordinate
        :param z: Z coordinate
        :param power: The power of explosion, where 4F is TNT
        :param set_fire: Whether or not to set blocks on fire
        :param break_blocks: Whether or not to have blocks be destroyed
        :return: false if explosion was canceled, otherwise true
        """
        pass

    def create_explosion(self, x: float, y: float, z: float, power: float, set_fire: bool, break_blocks: bool, source: Optional[Entity]) -> bool:
        """
        Creates explosion at given coordinates with given power and optionally setting blocks on fire or breaking blocks.

        :param x: X coordinate
        :param y: Y coordinate
        :param z: Z coordinate
        :param power: The power of explosion, where 4F is TNT
        :param set_fire: Whether or not to set blocks on fire
        :param break_blocks: Whether or not to have blocks be destroyed
        :param source: the source entity, used for tracking damage
        :return: false if explosion was canceled, otherwise true
        """
        pass

    def create_explosion(self, loc: Location, power: float) -> bool:
        """
        Creates explosion at given coordinates with given power

        :param loc: Location to blow up
        :param power: The power of explosion, where 4F is TNT
        :return: false if explosion was canceled, otherwise true
        """
        pass

    def create_explosion(self, loc: Location, power: float, set_fire: bool) -> bool:
        """
        Creates explosion at given coordinates with given power and optionally setting blocks on fire.

        :param loc: Location to blow up
        :param power: The power of explosion, where 4F is TNT
        :param set_fire: Whether or not to set blocks on fire
        :return: false if explosion was canceled, otherwise true
        """
        pass

    def create_explosion(self, loc: Location, power: float, set_fire: bool, break_blocks: bool) -> bool:
        """
        Creates explosion at given coordinates with given power and optionally setting blocks on fire or breaking blocks.

        :param loc: Location to blow up
        :param power: The power of explosion, where 4F is TNT
        :param set_fire: Whether or not to set blocks on fire
        :param break_blocks: Whether or not to have blocks be destroyed
        :return: false if explosion was canceled, otherwise true
        """
        pass

    def create_explosion(self, loc: Location, power: float, set_fire: bool, break_blocks: bool, source: Optional[Entity]) -> bool:
        """
        Creates explosion at given coordinates with given power and optionally setting blocks on fire or breaking blocks.

        :param loc: Location to blow up
        :param power: The power of explosion, where 4F is TNT
        :param set_fire: Whether or not to set blocks on fire
        :param break_blocks: Whether or not to have blocks be destroyed
        :param source: the source entity, used for tracking damage
        :return: false if explosion was canceled, otherwise true
        """
        pass

    def get_pvp(self) -> bool:
        """
        Gets the current PVP setting for this world.

        :return: True if PVP is enabled
        """
        pass

    def set_pvp(self, pvp: bool) -> None:
        """
        Sets the PVP setting for this world.

        :param pvp: True/False whether PVP should be Enabled.
        """
        pass

    def get_generator(self) -> Optional[ChunkGenerator]:
        """
        Gets the chunk generator for this world

        :return: ChunkGenerator associated with this world
        """
        pass

    def get_biome_provider(self) -> Optional[BiomeProvider]:
        """
        Gets the biome provider for this world

        :return: BiomeProvider associated with this world
        """
        pass

    def save(self) -> None:
        """
        Saves world to disk
        """
        pass

    def get_populators(self) -> List[BlockPopulator]:
        """
        Gets a list of all applied BlockPopulators for this World

        :return: List containing any or none BlockPopulators
        """
        pass

    def spawn(self, location: Location, clazz: Type[T], spawn_reason: CreatureSpawnEvent.SpawnReason, randomize_data: bool, function: Optional[Callable[[T], None]]) -> T:
        """
        Creates a new entity at the given Location with the supplied function run before the entity is added to the world.

        :param location: the location at which the entity will be spawned.
        :param clazz: the class of the LivingEntity that is to be spawned.
        :param spawn_reason: the reason provided during the CreatureSpawnEvent call.
        :param randomize_data: whether or not the entity's data should be randomised before spawning.
        :param function: the function to be run before the entity is spawned.
        :return: the spawned entity instance.
        :raises IllegalArgumentException: if either the world or clazz parameter are null.
        """
        pass

    def spawn_falling_block(self, location: Location, data: MaterialData) -> FallingBlock:
        """
        Spawn a FallingBlock entity at the given Location of the specified MaterialData.

        :param location: The Location to spawn the FallingBlock
        :param data: The block data
        :return: The spawned FallingBlock instance
        :raises IllegalArgumentException: if Location or MaterialData are null or Material of the MaterialData is not a block
        """
        pass

    def spawn_falling_block(self, location: Location, data: BlockData) -> FallingBlock:
        """
        Spawn a FallingBlock entity at the given Location of the specified BlockData.

        :param location: The Location to spawn the FallingBlock
        :param data: The BlockData of the FallingBlock to spawn
        :return: The spawned FallingBlock instance
        :raises IllegalArgumentException: if Location or BlockData are null
        """
        pass

    def spawn_falling_block(self, location: Location, material: Material, data: bytes) -> FallingBlock:
        """
        Spawn a FallingBlock entity at the given Location of the specified Material.

        :param location: The Location to spawn the FallingBlock
        :param material: The block Material type
        :param data: The block data
        :return: The spawned FallingBlock instance
        :raises IllegalArgumentException: if Location or Material are null or Material is not a block
        """
        pass

    def play_effect(self, location: Location, effect: Effect, data: int) -> None:
        """
        Plays an effect to all players within a default radius around a given location.

        :param location: the Location around which players must be to hear the sound
        :param effect: the Effect
        :param data: a data bit needed for some effects
        """
        pass

    def play_effect(self, location: Location, effect: Effect, data: int, radius: int) -> None:
        """
        Plays an effect to all players within a given radius around a location.

        :param location: the Location around which players must be to hear the effect
        :param effect: the Effect
        :param data: a data bit needed for some effects
        :param radius: the radius around the location
        """
        pass

    def play_effect(self, location: Location, effect: Effect, data: T) -> None:
        """
        Plays an effect to all players within a default radius around a given location.

        :param location: the Location around which players must be to hear the sound
        :param effect: the Effect
        :param data: a data bit needed for some effects
        """
        pass

    def play_effect(self, location: Location, effect: Effect, data: T, radius: int) -> None:
        """
        Plays an effect to all players within a given radius around a location.

        :param location: the Location around which players must be to hear the effect
        :param effect: the Effect
        :param data: a data bit needed for some effects
        :param radius: the radius around the location
        """
        pass

    def get_empty_chunk_snapshot(self, x: int, z: int, include_biome: bool, include_biome_temp: bool) -> ChunkSnapshot:
        """
        Get empty chunk snapshot (equivalent to all air blocks), optionally including valid biome data.

        :param x: - chunk x coordinate
        :param z: - chunk z coordinate
        :param include_biome: if true, snapshot includes per-coordinate biome type
        :param include_biome_temp: if true, snapshot includes per-coordinate raw biome temperature
        :return: The empty snapshot.
        """
        pass

    def set_spawn_flags(self, allow_monsters: bool, allow_animals: bool) -> None:
        """
        Sets the spawn flags for this.

        :param allow_monsters: if true, monsters are allowed to spawn in this world.
        :param allow_animals: if true, animals are allowed to spawn in this world.
        """
        pass

    def get_allow_animals(self) -> bool:
        """
        Gets whether animals can spawn in this world.

        :return: whether animals can spawn in this world.
        """
        pass

    def get_allow_monsters(self) -> bool:
        """
        Gets whether monsters can spawn in this world.

        :return: whether monsters can spawn in this world.
        """
        pass

    def get_biome(self, x: int, z: int) -> Biome:
        """
        Gets the biome for the given block coordinates.

        :param x: X coordinate of the block
        :param z: Z coordinate of the block
        :return: Biome of the requested block
        """
        pass

    def set_biome(self, x: int, z: int, bio: Biome) -> None:
        """
        Sets the biome for the given block coordinates

        :param x: X coordinate of the block
        :param z: Z coordinate of the block
        :param bio: new Biome type for this block
        """
        pass

    def get_temperature(self, x: int, z: int) -> float:
        """
        Gets the temperature for the given block coordinates.

        :param x: X coordinate of the block
        :param z: Z coordinate of the block
        :return: Temperature of the requested block
        """
        pass

    def get_temperature(self, x: int, y: int, z: int) -> float:
        """
        Gets the temperature for the given block coordinates.

        :param x: X coordinate of the block
        :param y: Y coordinate of the block
        :param z: Z coordinate of the block
        :return: Temperature of the requested block
        """
        pass

    def get_humidity(self, x: int, z: int) -> float:
        """
        Gets the humidity for the given block coordinates.

        :param x: X coordinate of the block
        :param z: Z coordinate of the block
        :return: Humidity of the requested block
        """
        pass

    def get_humidity(self, x: int, y: int, z: int) -> float:
        """
        Gets the humidity for the given block coordinates.

        :param x: X coordinate of the block
        :param y: Y coordinate of the block
        :param z: Z coordinate of the block
        :return: Humidity of the requested block
        """
        pass

    def get_logical_height(self) -> int:
        """
        Gets the maximum height to which chorus fruits and nether portals can bring players within this dimension.

        :return: maximum logical height for chorus fruits and nether portals
        """
        pass

    def is_natural(self) -> bool:
        """
        Gets if this world is natural.

        :return: true if world is natural
        """
        pass

    def is_bed_works(self) -> bool:
        """
        Gets if beds work in this world.

        :return: true if beds work in this world
        """
        pass

    def has_sky_light(self) -> bool:
        """
        Gets if this world has skylight access.

        :return: true if this world has skylight access
        """
        pass

    def has_ceiling(self) -> bool:
        """
        Gets if this world has a ceiling.

        :return: true if this world has a bedrock ceiling
        """
        pass

    def is_piglin_safe(self) -> bool:
        """
        Gets if this world allow to piglins to survive without shaking and transforming to zombified piglins.

        :return: true if piglins will not transform to zombified piglins
        """
        pass

    def is_respawn_anchor_works(self) -> bool:
        """
        Gets if this world allows players to charge and use respawn anchors.

        :return: true if players can charge and use respawn anchors
        """
        pass

    def has_raids(self) -> bool:
        """
        Gets if players with the bad omen effect in this world will trigger a raid.

        :return: true if raids will be triggered
        """
        pass

    def is_ultra_warm(self) -> bool:
        """
        Gets if various water/lava mechanics will be triggered in this world.

        :return: true if this world has the above mechanics
        """
        pass

    def get_sea_level(self) -> int:
        """
        Gets the sea level for this world.

        :return: Sea level
        """
        pass

    def get_keep_spawn_in_memory(self) -> bool:
        """
        Gets whether the world's spawn area should be kept loaded into memory or not.

        :return: true if the world's spawn area will be kept loaded into memory.
        """
        pass

    def set_keep_spawn_in_memory(self, keep_loaded: bool) -> None:
        """
        Sets whether the world's spawn area should be kept loaded into memory or not.

        :param keep_loaded: if true then the world's spawn area will be kept loaded into memory.
        """
        pass

    def is_auto_save(self) -> bool:
        """
        Gets whether or not the world will automatically save

        :return: true if the world will automatically save, otherwise false
        """
        pass

    def set_auto_save(self, value: bool) -> None:
        """
        Sets whether or not the world will automatically save

        :param value: true if the world should automatically save, otherwise false
        """
        pass

    def set_difficulty(self, difficulty: Difficulty) -> None:
        """
        Sets the Difficulty of the world.

        :param difficulty: the new difficulty you want to set the world to
        """
        pass

    def get_difficulty(self) -> Difficulty:
        """
        Gets the Difficulty of the world.

        :return: The difficulty of the world.
        """
        pass

    def get_view_distance(self) -> int:
        """
        Returns the view distance used for this world.

        :return: the view distance used for this world
        """
        pass

    def get_simulation_distance(self) -> int:
        """
        Returns the simulation distance used for this world.

        :return: the simulation distance used for this world
        """
        pass

    def get_world_folder(self) -> File:
        """
        Gets the folder of this world on disk.

        :return: The folder of this world.
        """
        pass

    def get_world_type(self) -> Optional[WorldType]:
        """
        Gets the type of this world.

        :return: Type of this world.
        """
        pass

    def can_generate_structures(self) -> bool:
        """
        Gets whether or not structures are being generated.

        :return: True if structures are being generated.
        """
        pass

    def is_hardcore(self) -> bool:
        """
        Gets whether the world is hardcore or not.

        :return: hardcore status
        """
        pass

    def set_hardcore(self, hardcore: bool) -> None:
        """
        Sets whether the world is hardcore or not.

        :param hardcore: Whether the world is hardcore
        """
        pass

    def get_ticks_per_animal_spawns(self) -> int:
        """
        Gets the world's ticks per animal spawns value

        :return: The world's ticks per animal spawns value
        """
        pass

    def set_ticks_per_animal_spawns(self, ticks_per_animal_spawns: int) -> None:
        """
        Sets the world's ticks per animal spawns value

        :param ticks_per_animal_spawns: the ticks per animal spawns value you want to set the world to
        """
        pass

    def get_ticks_per_monster_spawns(self) -> int:
        """
        Gets the world's ticks per monster spawns value

        :return: The world's ticks per monster spawns value
        """
        pass

    def set_ticks_per_monster_spawns(self, ticks_per_monster_spawns: int) -> None:
        """
        Sets the world's ticks per monster spawns value

        :param ticks_per_monster_spawns: the ticks per monster spawns value you want to set the world to
        """
        pass

    def get_ticks_per_water_spawns(self) -> int:
        """
        Gets the world's ticks per water mob spawns value

        :return: The world's ticks per water mob spawns value
        """
        pass

    def set_ticks_per_water_spawns(self, ticks_per_water_spawns: int) -> None:
        """
        Sets the world's ticks per water mob spawns value

        :param ticks_per_water_spawns: the ticks per water mob spawns value you want to set the world to
        """
        pass

    def get_ticks_per_water_ambient_spawns(self) -> int:
        """
        Gets the default ticks per water ambient mob spawns value.

        :return: the default ticks per water ambient mobs spawn value
        """
        pass

    def set_ticks_per_water_ambient_spawns(self, ticks_per_ambient_spawns: int) -> None:
        """
        Sets the world's ticks per water ambient mob spawns value

        :param ticks_per_ambient_spawns: the ticks per water ambient mob spawns value you want to set the world to
        """
        pass

    def get_ticks_per_water_underground_creature_spawns(self) -> int:
        """
        Gets the default ticks per water underground creature spawns value.

        :return: the default ticks per water underground creature spawn value
        """
        pass

    def set_ticks_per_water_underground_creature_spawns(self, ticks_per_water_underground_creature_spawns: int) -> None:
        """
        Sets the world's ticks per water underground creature spawns value

        :param ticks_per_water_underground_creature_spawns: the ticks per water underground creature spawns value you want to set the world to
        """
        pass

    def get_ticks_per_ambient_spawns(self) -> int:
        """
        Gets the world's ticks per ambient mob spawns value

        :return: The world's ticks per ambient spawns value
        """
        pass

    def set_ticks_per_ambient_spawns(self, ticks_per_ambient_spawns: int) -> None:
        """
        Sets the world's ticks per ambient mob spawns value

        :param ticks_per_ambient_spawns: the ticks per ambient mob spawns value you want to set the world to
        """
        pass

    def get_spawn_limit(self, spawn_category: SpawnCategory) -> int:
        """
        Gets the limit for number of {@link SpawnCategory} entities that can spawn in a chunk in this world

        :param spawn_category: the entity category
        :return: The ambient spawn limit
        """
        pass

    def set_spawn_limit(self, spawn_category: SpawnCategory, limit: int) -> None:
        """
        Sets the limit for number of {@link SpawnCategory} entities that can spawn in a chunk in this world

        :param spawn_category: the entity category
        :param limit: the new mob limit
        """
        pass

    def play_note(self, loc: Location, instrument: Instrument, note: Note) -> None:
        """
        Play a note at the provided Location in the World.

        :param loc: The location to play the note
        :param instrument: The instrument
        :param note: The note
        """
        pass

    def play_sound(self, location: Location, sound: Sound, volume: float, pitch: float) -> None:
        """
        Play a Sound at the provided Location in the World.

        :param location: The location to play the sound
        :param sound: The sound to play
        :param volume: The volume of the sound
        :param pitch: The pitch of the sound
        """
        pass

    def play_sound(self, location: Location, sound: str, volume: float, pitch: float) -> None:
        """
        Play a Sound at the provided Location in the World.

        :param location: The location to play the sound
        :param sound: The internal sound name to play
        :param volume: The volume of the sound
        :param pitch: The pitch of the sound
        """
        pass

    def play_sound(self, location: Location, sound: Sound, category: SoundCategory, volume: float, pitch: float) -> None:
        """
        Play a Sound at the provided Location in the World.

        :param location: The location to play the sound
        :param sound: The sound to play
        :param category: the category of the sound
        :param volume: The volume of the sound
        :param pitch: The pitch of the sound
        """
        pass

    def play_sound(self, location: Location, sound: str, category: SoundCategory, volume: float, pitch: float) -> None:
        """
        Play a Sound at the provided Location in the World.

        :param location: The location to play the sound
        :param sound: The internal sound name to play
        :param category: The category of the sound
        :param volume: The volume of the sound
        :param pitch: The pitch of the sound
        """
        pass

    def play_sound(self, location: Location, sound: Sound, category: SoundCategory, volume: float, pitch: float, seed: int) -> None:
        """
        Play a Sound at the provided Location in the World.

        :param location: The location to play the sound
        :param sound: The sound to play
        :param category: the category of the sound
        :param volume: The volume of the sound
        :param pitch: The pitch of the sound
        :param seed: The seed for the sound
        """
        pass

    def play_sound(self, location: Location, sound: str, category: SoundCategory, volume: float, pitch: float, seed: int) -> None:
        """
        Play a Sound at the provided Location in the World.

        :param location: The location to play the sound
        :param sound: The internal sound name to play
        :param category: The category of the sound
        :param volume: The volume of the sound
        :param pitch: The pitch of the sound
        :param seed: The seed for the sound
        """
        pass

    def play_sound(self, entity: Entity, sound: Sound, volume: float, pitch: float) -> None:
        """
        Play a Sound at the location of the provided entity in the World.

        :param entity: The entity to play the sound
        :param sound: The sound to play
        :param volume: The volume of the sound
        :param pitch: The pitch of the sound
        """
        pass

    def play_sound(self, entity: Entity, sound: str, volume: float, pitch: float) -> None:
        """
        Play a Sound at the location of the provided entity in the World.

        :param entity: The entity to play the sound
        :param sound: The sound to play
        :param volume: The volume of the sound
        :param pitch: The pitch of the sound
        """
        pass

    def play_sound(self, entity: Entity, sound: Sound, category: SoundCategory, volume: float, pitch: float) -> None:
        """
        Play a Sound at the location of the provided entity in the World.

        :param entity: The entity to play the sound
        :param sound: The sound to play
        :param category: The category of the sound
        :param volume: The volume of the sound
        :param pitch: The pitch of the sound
        """
        pass

    def play_sound(self, entity: Entity, sound: str, category: SoundCategory, volume: float, pitch: float) -> None:
        """
        Play a Sound at the location of the provided entity in the World.

        :param entity: The entity to play the sound
        :param sound: The sound to play
        :param category: The category of the sound
        :param volume: The volume of the sound
        :param pitch: The pitch of the sound
        """
        pass

    def play_sound(self, entity: Entity, sound: Sound, category: SoundCategory, volume: float, pitch: float, seed: int) -> None:
        """
        Play a Sound at the location of the provided entity in the World.

        :param entity: The entity to play the sound
        :param sound: The sound to play
        :param category: The category of the sound
        :param volume: The volume of the sound
        :param pitch: The pitch of the sound
        :param seed: The seed for the sound
        """
        pass

    def play_sound(self, entity: Entity, sound: str, category: SoundCategory, volume: float, pitch: float, seed: int) -> None:
        """
        Play a Sound at the location of the provided entity in the World.

        :param entity: The entity to play the sound
        :param sound: The internal sound name to play
        :param category: The category of the sound
        :param volume: The volume of the sound
        :param pitch: The pitch of the sound
        :param seed: The seed for the sound
        """
        pass

    def get_game_rules(self) -> List[str]:
        """
        Get an array containing the names of all the GameRules.

        :return: An array of GameRule names.
        """
        pass

    def get_game_rule_value(self, rule: Optional[str]) -> Optional[str]:
        """
        Gets the current state of the specified rule

        :param rule: Rule to look up value of
        :return: String value of rule
        """
        pass

    def set_game_rule_value(self, rule: str, value: str) -> bool:
        """
        Set the specified gamerule to specified value.

        :param rule: Rule to set
        :param value: Value to set rule to
        :return: True if rule was set
        """
        pass

    def is_game_rule(self, rule: str) -> bool:
        """
        Checks if string is a valid game rule

        :param rule: Rule to check
        :return: True if rule exists
        """
        pass

    def get_game_rule_value(self, rule: GameRule[T]) -> Optional[T]:
        """
        Get the current value for a given GameRule.

        :param rule: the GameRule to check
        :return: the current value
        """
        pass

    def get_game_rule_default(self, rule: GameRule[T]) -> Optional[T]:
        """
        Get the default value for a given GameRule.

        :param rule: the rule to return a default value for
        :return: the default value
        """
        pass

    def set_game_rule(self, rule: GameRule[T], new_value: T) -> bool:
        """
        Set the given GameRule's new value.

        :param rule: the GameRule to update
        :param new_value: the new value
        :return: true if the value was successfully set
        """
        pass

    def get_world_border(self) -> WorldBorder:
        """
        Gets the world border for this world.

        :return: The world border for this world.
        """
        pass

    def spawn_particle(self, particle: Particle, location: Location, count: int) -> None:
        """
        Spawns the particle at the target location.

        :param particle: the particle to spawn
        :param location: the location to spawn at
        :param count: the number of particles
        """
        pass

    def spawn_particle(self, particle: Particle, x: float, y: float, z: float, count: int) -> None:
        """
        Spawns the particle at the target location.

        :param particle: the particle to spawn
        :param x: the position on the x axis to spawn at
        :param y: the position on the y axis to spawn at
        :param z: the position on the z axis to spawn at
        :param count: the number of particles
        """
        pass

    def spawn_particle(self, particle: Particle, location: Location, count: int, data: Optional[T]) -> None:
        """
        Spawns the particle at the target location.

        :param particle: the particle to spawn
        :param location: the location to spawn at
        :param count: the number of particles
        :param data: the data to use for the particle or null
        """
        pass

    def spawn_particle(self, particle: Particle, x: float, y: float, z: float, count: int, data: Optional[T]) -> None:
        """
        Spawns the particle at the target location.

        :param particle: the particle to spawn
        :param x: the position on the x axis to spawn at
        :param y: the position on the y axis to spawn at
        :param z: the position on the z axis to spawn at
        :param count: the number of particles
        :param data: the data to use for the particle or null
        """
        pass

    def spawn_particle(self, particle: Particle, location: Location, count: int, offset_x: float, offset_y: float, offset_z: float) -> None:
        """
        Spawns the particle at the target location.

        :param particle: the particle to spawn
        :param location: the location to spawn at
        :param count: the number of particles
        :param offset_x: the maximum random offset on the X axis
        :param offset_y: the maximum random offset on the Y axis
        :param offset_z: the maximum random offset on the Z axis
        """
        pass

    def spawn_particle(self, particle: Particle, x: float, y: float, z: float, count: int, offset_x: float, offset_y: float, offset_z: float) -> None:
        """
        Spawns the particle at the target location.

        :param particle: the particle to spawn
        :param x: the position on the x axis to spawn at
        :param y: the position on the y axis to spawn at
        :param z: the position on the z axis to spawn at
        :param count: the number of particles
        :param offset_x: the maximum random offset on the X axis
        :param offset_y: the maximum random offset on the Y axis
        :param offset_z: the maximum random offset on the Z axis
        """
        pass

    def spawn_particle(self, particle: Particle, location: Location, count: int, offset_x: float, offset_y: float, offset_z: float, extra: float) -> None:
        """
        Spawns the particle at the target location.

        :param particle: the particle to spawn
        :param location: the location to spawn at
        :param count: the number of particles
        :param offset_x: the maximum random offset on the X axis
        :param offset_y: the maximum random offset on the Y axis
        :param offset_z: the maximum random offset on the Z axis
        :param extra: the extra data for this particle, depends on the particle used
        """
        pass

    def spawn_particle(self, particle: Particle, x: float, y: float, z: float, count: int, offset_x: float, offset_y: float, offset_z: float, extra: float) -> None:
        """
        Spawns the particle at the target location.

        :param particle: the particle to spawn
        :param x: the position on the x axis to spawn at
        :param y: the position on the y axis to spawn at
        :param z: the position on the z axis to spawn at
        :param count: the number of particles
        :param offset_x: the maximum random offset on the X axis
        :param offset_y: the maximum random offset on the Y axis
        :param offset_z: the maximum random offset on the Z axis
        :param extra: the extra data for this particle, depends on the particle used
        """
        pass

    def spawn_particle(self, particle: Particle, location: Location, count: int, offset_x: float, offset_y: float, offset_z: float, extra: float, data: Optional[T]) -> None:
        """
        Spawns the particle at the target location.

        :param particle: the particle to spawn
        :param location: the location to spawn at
        :param count: the number of particles
        :param offset_x: the maximum random offset on the X axis
        :param offset_y: the maximum random offset on the Y axis
        :param offset_z: the maximum random offset on the Z axis
        :param extra: the extra data for this particle, depends on the particle used
        :param data: the data to use for the particle or null
        """
        pass

    def spawn_particle(self, particle: Particle, x: float, y: float, z: float, count: int, offset_x: float, offset_y: float, offset_z: float, extra: float, data: Optional[T]) -> None:
        """
        Spawns the particle at the target location.

        :param particle: the particle to spawn
        :param x: the position on the x axis to spawn at
        :param y: the position on the y axis to spawn at
        :param z: the position on the z axis to spawn at
        :param count: the number of particles
        :param offset_x: the maximum random offset on the X axis
        :param offset_y: the maximum random offset on the Y axis
        :param offset_z: the maximum random offset on the Z axis
        :param extra: the extra data for this particle, depends on the particle used
        :param data: the data to use for the particle or null
        """
        pass

    def locate_nearest_structure(self, origin: Location, structure_type: StructureType, radius: int, find_unexplored: bool) -> Optional[Location]:
        """
        Find the closest nearby structure of a given StructureType.

        :param origin: where to start looking for a structure
        :param structure_type: the type of structure to find
        :param radius: the radius, in chunks, around which to search
        :param find_unexplored: true to only find unexplored structures
        :return: the closest Location, or null if no structure of the specified type exists.
        """
        pass

    def locate_nearest_structure(self, origin: Location, structure_type: StructureType, radius: int, find_unexplored: bool) -> Optional[StructureSearchResult]:
        """
        Find the closest nearby structure of a given StructureType.

        :param origin: where to start looking for a structure
        :param structure_type: the type of structure to find
        :param radius: the radius, in chunks, around which to search
        :param find_unexplored: true to only find unexplored structures
        :return: the closest Location and Structure, or null if no structure of the specified type exists.
        """
        pass

    def locate_nearest_structure(self, origin: Location, structure: Structure, radius: int, find_unexplored: bool) -> Optional[StructureSearchResult]:
        """
        Find the closest nearby structure of a given Structure.

        :param origin: where to start looking for a structure
        :param structure: the structure to find
        :param radius: the radius, in chunks, around which to search
        :param find_unexplored: true to only find unexplored structures
        :return: the closest Location and Structure, or null if no structure was found.
        """
        pass

    def locate_nearest_biome(self, origin: Location, radius: int, biomes: List[Biome]) -> Optional[BiomeSearchResult]:
        """
        Find the closest nearby location with a biome matching the provided Biome(s).

        :param origin: where to start looking for a biome
        :param radius: the radius, in blocks, around which to search
        :param biomes: the biomes to search for
        :return: a BiomeSearchResult containing the closest Location and Biome, or null if no biome was found.
        """
        pass

    def locate_nearest_biome(self, origin: Location, radius: int, horizontal_interval: int, vertical_interval: int, biomes: List[Biome]) -> Optional[BiomeSearchResult]:
        """
        Find the closest nearby location with a biome matching the provided Biome(s).

        :param origin: where to start looking for a biome
        :param radius: the radius, in blocks, around which to search
        :param horizontal_interval: the horizontal distance between each check
        :param vertical_interval: the vertical distance between each check
        :param biomes: the biomes to search for
        :return: a BiomeSearchResult containing the closest Location and Biome, or null if no biome was found.
        """
        pass

    def locate_nearest_raid(self, location: Location, radius: int) -> Optional[Raid]:
        """
        Finds the nearest raid close to the given location.

        :param location: the origin location
        :param radius: the radius
        :return: the closest Raid, or null if no raids were found
        """
        pass

    def get_raids(self) -> List[Raid]:
        """
        Gets all raids that are going on over this world.

        :return: the list of all active raids
        """
        pass

    def get_ender_dragon_battle(self) -> Optional[DragonBattle]:
        """
        Get the DragonBattle associated with this world.

        :return: the dragon battle instance
        """
        pass

    def get_feature_flags(self) -> Set[FeatureFlag]:
        """
        Get all FeatureFlags enabled in this world.

        :return: all enabled FeatureFlags
        """
        pass

    def get_structures(self, x: int, z: int) -> Collection[GeneratedStructure]:
        """
        Gets all generated structures that intersect the chunk at the given coordinates.

        :param x: X-coordinate of the chunk
        :param z: Z-coordinate of the chunk
        :return: a collection of placed structures in the chunk at the given coordinates
        """
        pass

    def get_structures(self, x: int, z: int, structure: Structure) -> Collection[GeneratedStructure]:
        """
        Gets all generated structures of a given Structure that intersect the chunk at the given coordinates.

        :param x: X-coordinate of the chunk
        :param z: Z-coordinate of the chunk
        :param structure: the structure to find
        :return: a collection of placed structures in the chunk at the given coordinates
        """
        pass
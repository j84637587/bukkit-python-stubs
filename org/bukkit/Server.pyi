from typing import Collection, List, Set, Dict, Optional, Iterator, Any
from . import (
    Advancement,
    BlockData,
    BarColor,
    BarFlag,
    BarStyle,
    BossBar,
    KeyedBossBar,
    CommandException,
    CommandSender,
    ConsoleCommandSender,
    PluginCommand,
    Entity,
    EntityFactory,
    EntitySnapshot,
    Player,
    SpawnCategory,
    InventoryType,
    ServerListPingEvent,
    ChunkGenerator,
    HelpMap,
    Inventory,
    InventoryHolder,
    ItemCraftResult,
    ItemFactory,
    ItemStack,
    MenuType,
    Merchant,
    Recipe,
    ItemMeta,
    LootTable,
    MapView,
    DataPackManager,
    ResourcePack,
    Permissible,
    PluginManager,
    ServicesManager,
    Messenger,
    PlayerProfile,
    BukkitScheduler,
    Criteria,
    ScoreboardManager,
    StructureManager,
    CachedServerIcon,
    WarningState,
    NamespacedKey,
    OfflinePlayer,
    World,
    WorldCreator,
    WorldBorder,
    Location,
    Tag,
    GameMode,
    UnsafeValues,
)

class Server:
    """
    Represents a server implementation.
    """

    BROADCAST_CHANNEL_ADMINISTRATIVE: str = "bukkit.broadcast.admin"
    BROADCAST_CHANNEL_USERS: str = "bukkit.broadcast.user"

    def get_name(self) -> str:
        """Gets the name of this server implementation."""
        ...

    def get_version(self) -> str:
        """Gets the version string of this server implementation."""
        ...

    def get_bukkit_version(self) -> str:
        """Gets the Bukkit version that this server is running."""
        ...

    def get_online_players(self) -> Collection[Player]:
        """Gets a view of all currently logged in players."""
        ...

    def get_max_players(self) -> int:
        """Get the maximum amount of players which can login to this server."""
        ...

    def set_max_players(self, max_players: int) -> None:
        """Set the maximum amount of players allowed to be logged in at once."""
        ...

    def get_port(self) -> int:
        """Get the game port that the server runs on."""
        ...

    def get_view_distance(self) -> int:
        """Get the view distance from this server."""
        ...

    def get_simulation_distance(self) -> int:
        """Get the simulation distance from this server."""
        ...

    def get_ip(self) -> str:
        """Get the IP that this server is bound to, or empty string if not specified."""
        ...

    def get_world_type(self) -> str:
        """Get world type (level-type setting) for default world."""
        ...

    def get_generate_structures(self) -> bool:
        """Get generate-structures setting."""
        ...

    def get_max_world_size(self) -> int:
        """Get max world size."""
        ...

    def get_allow_end(self) -> bool:
        """Gets whether this server allows the End or not."""
        ...

    def get_allow_nether(self) -> bool:
        """Gets whether this server allows the Nether or not."""
        ...

    def is_logging_ips(self) -> bool:
        """Gets whether the server is logging the IP addresses of players."""
        ...

    def get_initial_enabled_packs(self) -> List[str]:
        """Gets a list of packs to be enabled."""
        ...

    def get_initial_disabled_packs(self) -> List[str]:
        """Gets a list of packs that will not be enabled automatically."""
        ...

    def get_data_pack_manager(self) -> DataPackManager:
        """Get the DataPack Manager."""
        ...

    def get_server_tick_manager(self) -> Any:
        """Get the ServerTick Manager."""
        ...

    def get_server_resource_pack(self) -> Optional[ResourcePack]:
        """Gets the resource pack configured to be sent to clients by the server."""
        ...

    def get_resource_pack(self) -> str:
        """Gets the server resource pack uri, or empty string if not specified."""
        ...

    def get_resource_pack_hash(self) -> str:
        """Gets the SHA-1 digest of the server resource pack, or empty string if not specified."""
        ...

    def get_resource_pack_prompt(self) -> str:
        """Gets the custom prompt message to be shown when the server resource pack is required, or empty string if not specified."""
        ...

    def is_resource_pack_required(self) -> bool:
        """Gets whether the server resource pack is enforced."""
        ...

    def has_whitelist(self) -> bool:
        """Gets whether this server has a whitelist or not."""
        ...

    def set_whitelist(self, value: bool) -> None:
        """Sets if the server is whitelisted."""
        ...

    def is_whitelist_enforced(self) -> bool:
        """Gets whether the server whitelist is enforced."""
        ...

    def set_whitelist_enforced(self, value: bool) -> None:
        """Sets if the server whitelist is enforced."""
        ...

    def get_whitelisted_players(self) -> Set[OfflinePlayer]:
        """Gets a list of whitelisted players."""
        ...

    def reload_whitelist(self) -> None:
        """Reloads the whitelist from disk."""
        ...

    def broadcast_message(self, message: str) -> int:
        """Broadcast a message to all players."""
        ...

    def get_update_folder(self) -> str:
        """Gets the name of the update folder."""
        ...

    def get_update_folder_file(self) -> File:
        """Gets the update folder."""
        ...

    def get_connection_throttle(self) -> int:
        """Gets the value of the connection throttle setting."""
        ...

    def get_ticks_per_animal_spawns(self) -> int:
        """Gets default ticks per animal spawns value."""
        ...

    def get_ticks_per_monster_spawns(self) -> int:
        """Gets the default ticks per monster spawns value."""
        ...

    def get_ticks_per_water_spawns(self) -> int:
        """Gets the default ticks per water mob spawns value."""
        ...

    def get_ticks_per_water_ambient_spawns(self) -> int:
        """Gets the default ticks per water ambient mob spawns value."""
        ...

    def get_ticks_per_water_underground_creature_spawns(self) -> int:
        """Gets the default ticks per water underground creature spawns value."""
        ...

    def get_ticks_per_ambient_spawns(self) -> int:
        """Gets the default ticks per ambient mob spawns value."""
        ...

    def get_ticks_per_spawns(self, spawn_category: SpawnCategory) -> int:
        """Gets the default ticks per SpawnCategory spawns value."""
        ...

    def get_player(self, name: str) -> Optional[Player]:
        """Gets a player whose name matches the given name closest."""
        ...

    def get_player_exact(self, name: str) -> Optional[Player]:
        """Gets the player with the exact given name, case insensitive."""
        ...

    def match_player(self, name: str) -> List[Player]:
        """Attempts to match any players with the given name, and returns a list of all possibly matches."""
        ...

    def get_player_by_uuid(self, id: UUID) -> Optional[Player]:
        """Gets the player with the given UUID."""
        ...

    def get_plugin_manager(self) -> PluginManager:
        """Gets the plugin manager for interfacing with plugins."""
        ...

    def get_scheduler(self) -> BukkitScheduler:
        """Gets the scheduler for managing scheduled events."""
        ...

    def get_services_manager(self) -> ServicesManager:
        """Gets a services manager."""
        ...

    def get_worlds(self) -> List[World]:
        """Gets a list of all worlds on this server."""
        ...

    def create_world(self, creator: WorldCreator) -> Optional[World]:
        """Creates or loads a world with the given name using the specified options."""
        ...

    def unload_world_by_name(self, name: str, save: bool) -> bool:
        """Unloads a world with the given name."""
        ...

    def unload_world(self, world: World, save: bool) -> bool:
        """Unloads the given world."""
        ...

    def get_world_by_name(self, name: str) -> Optional[World]:
        """Gets the world with the given name."""
        ...

    def get_world_by_uuid(self, uid: UUID) -> Optional[World]:
        """Gets the world from the given Unique ID."""
        ...

    def create_world_border(self) -> WorldBorder:
        """Create a new virtual WorldBorder."""
        ...

    def get_map(self, id: int) -> Optional[MapView]:
        """Gets the map from the given item ID."""
        ...

    def create_map(self, world: World) -> MapView:
        """Create a new map with an automatically assigned ID."""
        ...

    def create_explorer_map(self, world: World, location: Location, structure_type: Any) -> ItemStack:
        """Create a new explorer map targeting the closest nearby structure of a given StructureType."""
        ...

    def create_explorer_map_with_radius(self, world: World, location: Location, structure_type: Any, radius: int, find_unexplored: bool) -> ItemStack:
        """Create a new explorer map targeting the closest nearby structure of a given StructureType with specified radius."""
        ...

    def reload(self) -> None:
        """Reloads the server, refreshing settings and plugin information."""
        ...

    def reload_data(self) -> None:
        """Reload only the Minecraft data for the server."""
        ...

    def get_logger(self) -> Logger:
        """Returns the primary logger associated with this server instance."""
        ...

    def get_plugin_command(self, name: str) -> Optional[PluginCommand]:
        """Gets a PluginCommand with the given name or alias."""
        ...

    def save_players(self) -> None:
        """Writes loaded players to disk."""
        ...

    def dispatch_command(self, sender: CommandSender, command_line: str) -> bool:
        """Dispatches a command on this server, and executes it if found."""
        ...

    def add_recipe(self, recipe: Optional[Recipe]) -> bool:
        """Adds a recipe to the crafting manager."""
        ...

    def get_recipes_for(self, result: ItemStack) -> List[Recipe]:
        """Get a list of all recipes for a given item."""
        ...

    def get_recipe(self, recipe_key: NamespacedKey) -> Optional[Recipe]:
        """Get the Recipe for the given key."""
        ...

    def get_crafting_recipe(self, crafting_matrix: List[ItemStack], world: World) -> Optional[Recipe]:
        """Get the Recipe for the list of ItemStacks provided."""
        ...

    def craft_item(self, crafting_matrix: List[ItemStack], world: World, player: Player) -> ItemStack:
        """Get the crafted item using the list of ItemStack provided."""
        ...

    def craft_item_without_player(self, crafting_matrix: List[ItemStack], world: World) -> ItemStack:
        """Get the crafted item using the list of ItemStack provided."""
        ...

    def craft_item_result(self, crafting_matrix: List[ItemStack], world: World, player: Player) -> ItemCraftResult:
        """Get the crafted item using the list of ItemStack provided."""
        ...

    def craft_item_result_without_player(self, crafting_matrix: List[ItemStack], world: World) -> ItemCraftResult:
        """Get the crafted item using the list of ItemStack provided."""
        ...

    def recipe_iterator(self) -> Iterator[Recipe]:
        """Get an iterator through the list of crafting recipes."""
        ...

    def clear_recipes(self) -> None:
        """Clears the list of crafting recipes."""
        ...

    def reset_recipes(self) -> None:
        """Resets the list of crafting recipes to the default."""
        ...

    def remove_recipe(self, key: NamespacedKey) -> bool:
        """Remove a recipe from the server."""
        ...

    def get_command_aliases(self) -> Dict[str, List[str]]:
        """Gets a list of command aliases defined in the server properties."""
        ...

    def get_spawn_radius(self) -> int:
        """Gets the radius, in blocks, around each worlds spawn point to protect."""
        ...

    def set_spawn_radius(self, value: int) -> None:
        """Sets the radius, in blocks, around each worlds spawn point to protect."""
        ...

    def should_send_chat_previews(self) -> bool:
        """Gets whether the server should send a preview of the player's chat message to the client."""
        ...

    def is_enforcing_secure_profiles(self) -> bool:
        """Gets whether the server only allow players with Mojang-signed public key to join."""
        ...

    def is_accepting_transfers(self) -> bool:
        """Gets whether this server is allowing connections transferred from other servers."""
        ...

    def get_hide_online_players(self) -> bool:
        """Gets whether the Server hide online players in server status."""
        ...

    def get_online_mode(self) -> bool:
        """Gets whether the Server is in online mode or not."""
        ...

    def get_allow_flight(self) -> bool:
        """Gets whether this server allows flying or not."""
        ...

    def is_hardcore(self) -> bool:
        """Gets whether the server is in hardcore mode or not."""
        ...

    def shutdown(self) -> None:
        """Shutdowns the server, stopping everything."""
        ...

    def broadcast(self, message: str, permission: str) -> int:
        """Broadcasts the specified message to every user with the given permission name."""
        ...

    def get_offline_player(self, name: str) -> OfflinePlayer:
        """Gets the player by the given name, regardless if they are offline or online."""
        ...

    def get_offline_player_by_uuid(self, id: UUID) -> OfflinePlayer:
        """Gets the player by the given UUID, regardless if they are offline or online."""
        ...

    def create_player_profile(self, unique_id: Optional[UUID], name: Optional[str]) -> PlayerProfile:
        """Creates a new PlayerProfile."""
        ...

    def get_ip_bans(self) -> Set[str]:
        """Gets a set containing all current IPs that are banned."""
        ...

    def ban_ip(self, address: str) -> None:
        """Bans the specified address from the server."""
        ...

    def unban_ip(self, address: str) -> None:
        """Unbans the specified address from the server."""
        ...

    def ban_ip_by_inet(self, address: InetAddress) -> None:
        """Bans the specified address from the server."""
        ...

    def unban_ip_by_inet(self, address: InetAddress) -> None:
        """Unbans the specified address from the server."""
        ...

    def get_banned_players(self) -> Set[OfflinePlayer]:
        """Gets a set containing all banned players."""
        ...

    def get_ban_list(self, type: Any) -> Any:
        """Gets a ban list for the supplied type."""
        ...

    def get_operators(self) -> Set[OfflinePlayer]:
        """Gets a set containing all player operators."""
        ...

    def get_default_game_mode(self) -> GameMode:
        """Gets the default GameMode for new players."""
        ...

    def set_default_game_mode(self, mode: GameMode) -> None:
        """Sets the default GameMode for new players."""
        ...

    def get_console_sender(self) -> ConsoleCommandSender:
        """Gets a ConsoleCommandSender that may be used as an input source for this server."""
        ...

    def get_world_container(self) -> File:
        """Gets the folder that contains all of the various Worlds."""
        ...

    def get_offline_players(self) -> List[OfflinePlayer]:
        """Gets every player that has ever played on this server."""
        ...

    def get_messenger(self) -> Messenger:
        """Gets the Messenger responsible for this server."""
        ...

    def get_help_map(self) -> HelpMap:
        """Gets the HelpMap providing help topics for this server."""
        ...

    def create_inventory(self, owner: Optional[InventoryHolder], type: InventoryType) -> Inventory:
        """Creates an empty inventory with the specified type."""
        ...

    def create_inventory_with_title(self, owner: Optional[InventoryHolder], type: InventoryType, title: str) -> Inventory:
        """Creates an empty inventory with the specified type and title."""
        ...

    def create_inventory_with_size(self, owner: Optional[InventoryHolder], size: int) -> Inventory:
        """Creates an empty inventory of type CHEST with the specified size."""
        ...

    def create_inventory_with_size_and_title(self, owner: Optional[InventoryHolder], size: int, title: str) -> Inventory:
        """Creates an empty inventory of type CHEST with the specified size and title."""
        ...

    def create_merchant(self, title: Optional[str]) -> Merchant:
        """Creates an empty merchant."""
        ...

    def create_merchant_without_title(self) -> Merchant:
        """Creates an empty merchant."""
        ...

    def get_max_chained_neighbor_updates(self) -> int:
        """Gets the amount of consecutive neighbor updates before skipping additional ones."""
        ...

    def get_monster_spawn_limit(self) -> int:
        """Gets user-specified limit for number of monsters that can spawn in a chunk."""
        ...

    def get_animal_spawn_limit(self) -> int:
        """Gets user-specified limit for number of animals that can spawn in a chunk."""
        ...

    def get_water_animal_spawn_limit(self) -> int:
        """Gets user-specified limit for number of water animals that can spawn in a chunk."""
        ...

    def get_water_ambient_spawn_limit(self) -> int:
        """Gets user-specified limit for number of water ambient mobs that can spawn in a chunk."""
        ...

    def get_water_underground_creature_spawn_limit(self) -> int:
        """Get user-specified limit for number of water underground creature that can spawn in a chunk."""
        ...

    def get_ambient_spawn_limit(self) -> int:
        """Gets user-specified limit for number of ambient mobs that can spawn in a chunk."""
        ...

    def get_spawn_limit(self, spawn_category: SpawnCategory) -> int:
        """Gets user-specified limit for number of SpawnCategory mobs that can spawn in a chunk."""
        ...

    def is_primary_thread(self) -> bool:
        """Checks the current thread against the expected primary thread for the server."""
        ...

    def get_motd(self) -> str:
        """Gets the message that is displayed on the server list."""
        ...

    def set_motd(self, motd: str) -> None:
        """Set the message that is displayed on the server list."""
        ...

    def get_server_links(self) -> Any:
        """Gets the server links which will be sent to clients."""
        ...

    def get_shutdown_message(self) -> Optional[str]:
        """Gets the default message that is displayed when the server is stopped."""
        ...

    def get_warning_state(self) -> WarningState:
        """Gets the current warning state for the server."""
        ...

    def get_item_factory(self) -> ItemFactory:
        """Gets the instance of the item factory (for ItemMeta)."""
        ...

    def get_entity_factory(self) -> EntityFactory:
        """Gets the instance of the entity factory (for EntitySnapshot)."""
        ...

    def get_scoreboard_manager(self) -> Optional[ScoreboardManager]:
        """Gets the instance of the scoreboard manager."""
        ...

    def get_scoreboard_criteria(self, name: str) -> Criteria:
        """Get (or create) a new Criteria by its name."""
        ...

    def get_server_icon(self) -> Optional[CachedServerIcon]:
        """Gets an instance of the server's default server-icon."""
        ...

    def load_server_icon_from_file(self, file: File) -> CachedServerIcon:
        """Loads an image from a file, and returns a cached image for the specific server-icon."""
        ...

    def load_server_icon_from_image(self, image: BufferedImage) -> CachedServerIcon:
        """Creates a cached server-icon for the specific image."""
        ...

    def set_idle_timeout(self, threshold: int) -> None:
        """Set the idle kick timeout."""
        ...

    def get_idle_timeout(self) -> int:
        """Gets the idle kick timeout."""
        ...

    def get_pause_when_empty_time(self) -> int:
        """Gets the pause when empty threshold seconds."""
        ...

    def set_pause_when_empty_time(self, seconds: int) -> None:
        """Sets the pause when empty threshold seconds."""
        ...

    def create_chunk_data(self, world: World) -> ChunkGenerator.ChunkData:
        """Create a ChunkData for use in a generator."""
        ...

    def create_boss_bar(self, title: Optional[str], color: BarColor, style: BarStyle, *flags: BarFlag) -> BossBar:
        """Creates a boss bar instance to display to players."""
        ...

    def create_keyed_boss_bar(self, key: NamespacedKey, title: Optional[str], color: BarColor, style: BarStyle, *flags: BarFlag) -> KeyedBossBar:
        """Creates a boss bar instance to display to players."""
        ...

    def get_boss_bars(self) -> Iterator[KeyedBossBar]:
        """Gets an unmodifiable iterator through all persistent bossbars."""
        ...

    def get_boss_bar(self, key: NamespacedKey) -> Optional[KeyedBossBar]:
        """Gets the KeyedBossBar specified by this key."""
        ...

    def remove_boss_bar(self, key: NamespacedKey) -> bool:
        """Removes a KeyedBossBar specified by this key."""
        ...

    def get_entity(self, uuid: UUID) -> Optional[Entity]:
        """Gets an entity on the server by its UUID."""
        ...

    def get_advancement(self, key: NamespacedKey) -> Optional[Advancement]:
        """Get the advancement specified by this key."""
        ...

    def advancement_iterator(self) -> Iterator[Advancement]:
        """Get an iterator through all advancements."""
        ...

    def create_block_data(self, material: Any) -> BlockData:
        """Creates a new BlockData instance for the specified Material."""
        ...

    def create_block_data_with_consumer(self, material: Any, consumer: Optional[Consumer[BlockData]]) -> BlockData:
        """Creates a new BlockData instance for the specified Material."""
        ...

    def create_block_data_from_string(self, data: str) -> BlockData:
        """Creates a new BlockData instance with material and properties parsed from provided data."""
        ...

    def create_block_data_with_material_and_string(self, material: Optional[Any], data: Optional[str]) -> BlockData:
        """Creates a new BlockData instance for the specified Material."""
        ...

    def get_tag(self, registry: str, tag: NamespacedKey, clazz: Any) -> Optional[Tag[Any]]:
        """Gets a tag which has already been defined within the server."""
        ...

    def get_tags(self, registry: str, clazz: Any) -> Iterable[Tag[Any]]:
        """Gets a all tags which have been defined within the server."""
        ...

    def get_loot_table(self, key: NamespacedKey) -> Optional[LootTable]:
        """Gets the specified LootTable."""
        ...

    def select_entities(self, sender: CommandSender, selector: str) -> List[Entity]:
        """Selects entities using the given Vanilla selector."""
        ...

    def get_structure_manager(self) -> StructureManager:
        """Gets the structure manager for loading and saving structures."""
        ...

    def get_registry(self, t_class: Any) -> Optional[Any]:
        """Returns the registry for the given class."""
        ...

    def get_unsafe(self) -> UnsafeValues:
        """@return the unsafe values instance."""
        ...
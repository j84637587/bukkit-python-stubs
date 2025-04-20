from typing import Collection, List, Set, Dict, Optional, Iterator
from java.awt.image import BufferedImage
from java.io import File
from java.net import InetAddress
from java.util import UUID
from org.bukkit import Server
from org.bukkit.advancement import Advancement
from org.bukkit.block.data import BlockData
from org.bukkit.boss import BarColor, BarFlag, BarStyle, BossBar, KeyedBossBar
from org.bukkit.command import CommandException, CommandSender, ConsoleCommandSender, PluginCommand
from org.bukkit.entity import Entity, EntityFactory, Player, SpawnCategory
from org.bukkit.inventory import Inventory, InventoryHolder, ItemCraftResult, ItemStack, Recipe, Merchant
from org.bukkit.plugin import PluginManager, ServicesManager
from org.bukkit.packs import DataPackManager, ResourcePack
from org.bukkit.permissions import Permissible
from org.bukkit.scheduler import BukkitScheduler
from org.bukkit.scoreboard import ScoreboardManager
from org.bukkit.structure import StructureManager
from org.bukkit.util import CachedServerIcon
from org.bukkit import Warning
from org.jetbrains.annotations import NotNull, Nullable, Contract

class Bukkit:
    """
    Represents the Bukkit core, for version and Server singleton handling
    """

    server: Server

    def __init__(self) -> None:
        raise NotImplementedError("Static class cannot be initialized.")

    @staticmethod
        def getServer() -> Server:
        """
        Gets the current {@link Server} singleton

        @return Server instance being ran
        """
        ...

    @staticmethod
    def setServer(@NotNull server: Server) -> None:
        """
        Attempts to set the {@link Server} singleton.
        This cannot be done if the Server is already set.

        @param server Server instance
        """
        ...

    @staticmethod
        def getName() -> str:
        """
        Gets the name of this server implementation.

        @return name of this server implementation
        """
        ...

    @staticmethod
        def getVersion() -> str:
        """
        Gets the version string of this server implementation.

        @return version of this server implementation
        """
        ...

    @staticmethod
        def getBukkitVersion() -> str:
        """
        Gets the Bukkit version that this server is running.

        @return version of Bukkit
        """
        ...

    @staticmethod
        def getOnlinePlayers() -> Collection[Player]:
        """
        Gets a view of all currently logged in players.

        @return a view of currently online players.
        """
        ...

    @staticmethod
    def getMaxPlayers() -> int:
        """
        Get the maximum amount of players which can login to this server.

        @return the amount of players this server allows
        """
        ...

    @staticmethod
    def setMaxPlayers(maxPlayers: int) -> None:
        """
        Set the maximum amount of players allowed to be logged in at once.

        @param maxPlayers The maximum amount of concurrent players
        """
        ...

    @staticmethod
    def getPort() -> int:
        """
        Get the game port that the server runs on.

        @return the port number of this server
        """
        ...

    @staticmethod
    def getViewDistance() -> int:
        """
        Get the view distance from this server.

        @return the view distance from this server.
        """
        ...

    @staticmethod
    def getSimulationDistance() -> int:
        """
        Get the simulation distance from this server.

        @return the simulation distance from this server.
        """
        ...

    @staticmethod
        def getIp() -> str:
        """
        Get the IP that this server is bound to, or empty string if not specified.

        @return the IP string that this server is bound to, otherwise empty string
        """
        ...

    @staticmethod
        def getWorldType() -> str:
        """
        Get world type (level-type setting) for default world.

        @return the value of level-type (e.g. DEFAULT, FLAT, DEFAULT_1_1)
        """
        ...

    @staticmethod
    def getGenerateStructures() -> bool:
        """
        Get generate-structures setting.

        @return true if structure generation is enabled, false otherwise
        """
        ...

    @staticmethod
    def getMaxWorldSize() -> int:
        """
        Get max world size.

        @return the maximum world size as specified for the server
        """
        ...

    @staticmethod
    def getAllowEnd() -> bool:
        """
        Gets whether this server allows the End or not.

        @return whether this server allows the End or not
        """
        ...

    @staticmethod
    def getAllowNether() -> bool:
        """
        Gets whether this server allows the Nether or not.

        @return whether this server allows the Nether or not
        """
        ...

    @staticmethod
    def isLoggingIPs() -> bool:
        """
        Gets whether the server is logging the IP addresses of players.

        @return whether the server is logging the IP addresses of players
        """
        ...

    @staticmethod
        def getInitialEnabledPacks() -> List[str]:
        """
        @return a list of initial enabled packs
        """
        ...

    @staticmethod
        def getInitialDisabledPacks() -> List[str]:
        """
        @return a list of initial disabled packs
        """
        ...

    @staticmethod
        def getDataPackManager() -> DataPackManager:
        """
        Get the DataPack Manager.

        @return the manager
        """
        ...

    @staticmethod
        def getServerResourcePack() -> ResourcePack:
        """
        Gets the resource pack configured to be sent to clients by the server.

        @return the resource pack
        """
        ...

    @staticmethod
        def getServerTickManager() -> ServerTickManager:
        """
        Get the ServerTick Manager.

        @return the manager
        """
        ...

    @staticmethod
        def getResourcePack() -> str:
        """
        Gets the server resource pack uri, or empty string if not specified.

        @return the server resource pack uri, otherwise empty string
        """
        ...

    @staticmethod
        def getResourcePackHash() -> str:
        """
        Gets the SHA-1 digest of the server resource pack, or empty string if not specified.

        @return the SHA-1 digest of the server resource pack, otherwise empty string
        """
        ...

    @staticmethod
        def getResourcePackPrompt() -> str:
        """
        Gets the custom prompt message to be shown when the server resource pack is required, or empty string if not specified.

        @return the custom prompt message to be shown when the server resource, otherwise empty string
        """
        ...

    @staticmethod
    def isResourcePackRequired() -> bool:
        """
        Gets whether the server resource pack is enforced.

        @return whether the server resource pack is enforced
        """
        ...

    @staticmethod
    def hasWhitelist() -> bool:
        """
        Gets whether this server has a whitelist or not.

        @return whether this server has a whitelist or not
        """
        ...

    @staticmethod
    def setWhitelist(value: bool) -> None:
        """
        Sets if the server is whitelisted.

        @param value true for whitelist on, false for off
        """
        ...

    @staticmethod
    def isWhitelistEnforced() -> bool:
        """
        Gets whether the server whitelist is enforced.

        @return whether the server whitelist is enforced
        """
        ...

    @staticmethod
    def setWhitelistEnforced(value: bool) -> None:
        """
        Sets if the server whitelist is enforced.

        @param value true for enforced, false for not
        """
        ...

    @staticmethod
        def getWhitelistedPlayers() -> Set[OfflinePlayer]:
        """
        Gets a list of whitelisted players.

        @return a set containing all whitelisted players
        """
        ...

    @staticmethod
    def reloadWhitelist() -> None:
        """
        Reloads the whitelist from disk.
        """
        ...

    @staticmethod
    def broadcastMessage(@NotNull message: str) -> int:
        """
        Broadcast a message to all players.

        @param message the message
        @return the number of players
        """
        ...

    @staticmethod
        def getUpdateFolder() -> str:
        """
        Gets the name of the update folder.

        @return the name of the update folder
        """
        ...

    @staticmethod
        def getUpdateFolderFile() -> File:
        """
        Gets the update folder.

        @return the update folder
        """
        ...

    @staticmethod
    def getConnectionThrottle() -> int:
        """
        Gets the value of the connection throttle setting.

        @return the value of the connection throttle setting
        """
        ...

    @staticmethod
    @Deprecated(since="1.18.1")
    def getTicksPerAnimalSpawns() -> int:
        """
        Gets default ticks per animal spawns value.

        @return the default ticks per animal spawns value
        """
        ...

    @staticmethod
    @Deprecated(since="1.18.1")
    def getTicksPerMonsterSpawns() -> int:
        """
        Gets the default ticks per monster spawns value.

        @return the default ticks per monsters spawn value
        """
        ...

    @staticmethod
    @Deprecated(since="1.18.1")
    def getTicksPerWaterSpawns() -> int:
        """
        Gets the default ticks per water mob spawns value.

        @return the default ticks per water mobs spawn value
        """
        ...

    @staticmethod
    @Deprecated(since="1.18.1")
    def getTicksPerAmbientSpawns() -> int:
        """
        Gets the default ticks per ambient mob spawns value.

        @return the default ticks per ambient mobs spawn value
        """
        ...

    @staticmethod
    @Deprecated(since="1.18.1")
    def getTicksPerWaterAmbientSpawns() -> int:
        """
        Gets the default ticks per water ambient mob spawns value.

        @return the default ticks per water ambient mobs spawn value
        """
        ...

    @staticmethod
    @Deprecated(since="1.18.1")
    def getTicksPerWaterUndergroundCreatureSpawns() -> int:
        """
        Gets the default ticks per water underground creature spawns value.

        @return the default ticks per water underground creature spawn value
        """
        ...

    @staticmethod
    def getTicksPerSpawns(@NotNull spawnCategory: SpawnCategory) -> int:
        """
        Gets the default ticks per {@link SpawnCategory} spawns value.

        @param spawnCategory the category of spawn
        @return the default ticks per {@link SpawnCategory} mobs spawn value
        """
        ...

    @staticmethod
        def getPlayer(@NotNull name: str) -> Optional[Player]:
        """
        Gets a player whose name matches the given name closest.

        @param name the name to look up
        @return a player if one was found, null otherwise
        """
        ...

    @staticmethod
        def getPlayerExact(@NotNull name: str) -> Optional[Player]:
        """
        Gets the player with the exact given name, case insensitive.

        @param name Exact name of the player to retrieve
        @return a player object if one was found, null otherwise
        """
        ...

    @staticmethod
        def matchPlayer(@NotNull name: str) -> List[Player]:
        """
        Attempts to match any players with the given name, and returns a list of all possibly matches.

        @param name the (partial) name to match
        @return list of all possible players
        """
        ...

    @staticmethod
        def getPlayer(@NotNull id: UUID) -> Optional[Player]:
        """
        Gets the player with the given UUID.

        @param id UUID of the player to retrieve
        @return a player object if one was found, null otherwise
        """
        ...

    @staticmethod
        def getPluginManager() -> PluginManager:
        """
        Gets the plugin manager for interfacing with plugins.

        @return a plugin manager for this Server instance
        """
        ...

    @staticmethod
        def getScheduler() -> BukkitScheduler:
        """
        Gets the scheduler for managing scheduled events.

        @return a scheduling service for this server
        """
        ...

    @staticmethod
        def getServicesManager() -> ServicesManager:
        """
        Gets a services manager.

        @return s services manager
        """
        ...

    @staticmethod
        def getWorlds() -> List[World]:
        """
        Gets a list of all worlds on this server.

        @return a list of worlds
        """
        ...

    @staticmethod
        def createWorld(@NotNull creator: WorldCreator) -> Optional[World]:
        """
        Creates or loads a world with the given name using the specified options.

        @param creator the options to use when creating the world
        @return newly created or loaded world
        """
        ...

    @staticmethod
    def unloadWorld(@NotNull name: str, save: bool) -> bool:
        """
        Unloads a world with the given name.

        @param name Name of the world to unload
        @param save whether to save the chunks before unloading
        @return true if successful, false otherwise
        """
        ...

    @staticmethod
    def unloadWorld(@NotNull world: World, save: bool) -> bool:
        """
        Unloads the given world.

        @param world the world to unload
        @param save whether to save the chunks before unloading
        @return true if successful, false otherwise
        """
        ...

    @staticmethod
        def getWorld(@NotNull name: str) -> Optional[World]:
        """
        Gets the world with the given name.

        @param name the name of the world to retrieve
        @return a world with the given name, or null if none exists
        """
        ...

    @staticmethod
        def getWorld(@NotNull uid: UUID) -> Optional[World]:
        """
        Gets the world from the given Unique ID.

        @param uid a unique-id of the world to retrieve
        @return a world with the given Unique ID, or null if none exists
        """
        ...

    @staticmethod
        def createWorldBorder() -> WorldBorder:
        """
        Create a new virtual {@link WorldBorder}.

        @return the created world border instance
        """
        ...

    @staticmethod
        @Deprecated(since="1.6.2")
    def getMap(id: int) -> Optional[MapView]:
        """
        Gets the map from the given item ID.

        @param id the id of the map to get
        @return a map view if it exists, or null otherwise
        """
        ...

    @staticmethod
        def createMap(@NotNull world: World) -> MapView:
        """
        Create a new map with an automatically assigned ID.

        @param world the world the map will belong to
        @return a newly created map view
        """
        ...

    @staticmethod
        def createExplorerMap(@NotNull world: World, @NotNull location: Location, @NotNull structureType: StructureType) -> ItemStack:
        """
        Create a new explorer map targeting the closest nearby structure of a given {@link StructureType}.

        @param world the world the map will belong to
        @param location the origin location to find the nearest structure
        @param structureType the type of structure to find
        @return a newly created item stack
        """
        ...

    @staticmethod
        def createExplorerMap(@NotNull world: World, @NotNull location: Location, @NotNull structureType: StructureType, radius: int, findUnexplored: bool) -> ItemStack:
        """
        Create a new explorer map targeting the closest nearby structure of a given {@link StructureType}.

        @param world the world the map will belong to
        @param location the origin location to find the nearest structure
        @param structureType the type of structure to find
        @param radius radius to search
        @param findUnexplored whether to find unexplored structures
        @return the newly created item stack
        """
        ...

    @staticmethod
    def reload() -> None:
        """
        Reloads the server, refreshing settings and plugin information.
        """
        ...

    @staticmethod
    def reloadData() -> None:
        """
        Reload only the Minecraft data for the server. This includes custom advancements and loot tables.
        """
        ...

    @staticmethod
        def getLogger() -> Logger:
        """
        Returns the primary logger associated with this server instance.

        @return Logger associated with this server
        """
        ...

    @staticmethod
        def getPluginCommand(@NotNull name: str) -> Optional[PluginCommand]:
        """
        Gets a {@link PluginCommand} with the given name or alias.

        @param name the name of the command to retrieve
        @return a plugin command if found, null otherwise
        """
        ...

    @staticmethod
    def savePlayers() -> None:
        """
        Writes loaded players to disk.
        """
        ...

    @staticmethod
    def dispatchCommand(@NotNull sender: CommandSender, @NotNull commandLine: str) -> bool:
        """
        Dispatches a command on this server, and executes it if found.

        @param sender the apparent sender of the command
        @param commandLine the command + arguments
        @return returns false if no target is found
        @throws CommandException thrown when the executor for the given command fails with an unhandled exception
        """
        ...

    @staticmethod
    @Contract("null -> false")
    def addRecipe(@Nullable recipe: Recipe) -> bool:
        """
        Adds a recipe to the crafting manager.

        @param recipe the recipe to add
        @return true if the recipe was added, false if it wasn't for some reason
        """
        ...

    @staticmethod
        def getRecipesFor(@NotNull result: ItemStack) -> List[Recipe]:
        """
        Get a list of all recipes for a given item.

        @param result the item to match against recipe results
        @return a list of recipes with the given result
        """
        ...

    @staticmethod
        def getRecipe(@NotNull recipeKey: NamespacedKey) -> Optional[Recipe]:
        """
        Get the {@link Recipe} for the given key.

        @param recipeKey the key of the recipe to return
        @return the recipe for the given key or null.
        """
        ...

    @staticmethod
        def getCraftingRecipe(@NotNull craftingMatrix: List[ItemStack], @NotNull world: World) -> Optional[Recipe]:
        """
        Get the {@link Recipe} for the list of ItemStacks provided.

        @param craftingMatrix list of items to be crafted from.
        @param world The world the crafting takes place in.
        @return the {@link Recipe} resulting from the given crafting matrix.
        """
        ...

    @staticmethod
        def craftItemResult(@NotNull craftingMatrix: List[ItemStack], @NotNull world: World, @NotNull player: Player) -> ItemCraftResult:
        """
        Get the crafted item using the list of {@link ItemStack} provided.

        @param craftingMatrix list of items to be crafted from.
        @param world The world the crafting takes place in.
        @param player The player to imitate the crafting event on.
        @return resulting {@link ItemCraftResult} containing the resulting item, matrix and any overflow items.
        """
        ...

    @staticmethod
        def craftItemResult(@NotNull craftingMatrix: List[ItemStack], @NotNull world: World) -> ItemCraftResult:
        """
        Get the crafted item using the list of {@link ItemStack} provided.

        @param craftingMatrix list of items to be crafted from.
        @param world The world the crafting takes place in.
        @return resulting {@link ItemCraftResult} containing the resulting item, matrix and any overflow items.
        """
        ...

    @staticmethod
        def craftItem(@NotNull craftingMatrix: List[ItemStack], @NotNull world: World, @NotNull player: Player) -> ItemStack:
        """
        Get the crafted item using the list of {@link ItemStack} provided.

        @param craftingMatrix list of items to be crafted from.
        @param world The world the crafting takes place in.
        @param player The player to imitate the crafting event on.
        @return the {@link ItemStack} resulting from the given crafting matrix
        """
        ...

    @staticmethod
        def craftItem(@NotNull craftingMatrix: List[ItemStack], @NotNull world: World) -> ItemStack:
        """
        Get the crafted item using the list of {@link ItemStack} provided.

        @param craftingMatrix list of items to be crafted from.
        @param world The world the crafting takes place in.
        @return the {@link ItemStack} resulting from the given crafting matrix
        """
        ...

    @staticmethod
        def recipeIterator() -> Iterator[Recipe]:
        """
        Get an iterator through the list of crafting recipes.

        @return an iterator
        """
        ...

    @staticmethod
    def clearRecipes() -> None:
        """
        Clears the list of crafting recipes.
        """
        ...

    @staticmethod
    def resetRecipes() -> None:
        """
        Resets the list of crafting recipes to the default.
        """
        ...

    @staticmethod
    def removeRecipe(@NotNull key: NamespacedKey) -> bool:
        """
        Remove a recipe from the server.

        @param key NamespacedKey of recipe to remove.
        @return True if recipe was removed
        """
        ...

    @staticmethod
        def getCommandAliases() -> Dict[str, List[str]]:
        """
        Gets a list of command aliases defined in the server properties.

        @return a map of aliases to command names
        """
        ...

    @staticmethod
    def getSpawnRadius() -> int:
        """
        Gets the radius, in blocks, around each worlds spawn point to protect.

        @return spawn radius, or 0 if none
        """
        ...

    @staticmethod
    def setSpawnRadius(value: int) -> None:
        """
        Sets the radius, in blocks, around each worlds spawn point to protect.

        @param value new spawn radius, or 0 if none
        """
        ...

    @staticmethod
    @Deprecated(since="1.19.3")
    def shouldSendChatPreviews() -> bool:
        """
        Gets whether the server should send a preview of the player's chat message to the client when the player sends a message

        @return true if the server should send a preview, false otherwise
        """
        ...

    @staticmethod
    def isEnforcingSecureProfiles() -> bool:
        """
        Gets whether the server only allow players with Mojang-signed public key to join

        @return true if only Mojang-signed players can join, false otherwise
        """
        ...

    @staticmethod
    def isAcceptingTransfers() -> bool:
        """
        Gets whether this server is allowing connections transferred from other servers.

        @return true if the server accepts transfers, false otherwise
        """
        ...

    @staticmethod
    def getHideOnlinePlayers() -> bool:
        """
        Gets whether the Server hide online players in server status.

        @return true if the server hide online players, false otherwise
        """
        ...

    @staticmethod
    def getOnlineMode() -> bool:
        """
        Gets whether the Server is in online mode or not.

        @return true if the server authenticates clients, false otherwise
        """
        ...

    @staticmethod
    def getAllowFlight() -> bool:
        """
        Gets whether this server allows flying or not.

        @return true if the server allows flight, false otherwise
        """
        ...

    @staticmethod
    def isHardcore() -> bool:
        """
        Gets whether the server is in hardcore mode or not.

        @return true if the server mode is hardcore, false otherwise
        """
        ...

    @staticmethod
    def shutdown() -> None:
        """
        Shutdowns the server, stopping everything.
        """
        ...

    @staticmethod
    def broadcast(@NotNull message: str, @NotNull permission: str) -> int:
        """
        Broadcasts the specified message to every user with the given permission name.

        @param message message to broadcast
        @param permission the required permission {@link Permissible permissibles} must have to receive the broadcast
        @return number of message recipients
        """
        ...

    @staticmethod
    @Deprecated(since="1.7.5")
        def getOfflinePlayer(@NotNull name: str) -> OfflinePlayer:
        """
        Gets the player by the given name, regardless if they are offline or online.

        @param name the name the player to retrieve
        @return an offline player
        """
        ...

    @staticmethod
        def getOfflinePlayer(@NotNull id: UUID) -> OfflinePlayer:
        """
        Gets the player by the given UUID, regardless if they are offline or online.

        @param id the UUID of the player to retrieve
        @return an offline player
        """
        ...

    @staticmethod
        def createPlayerProfile(@Nullable uniqueId: UUID, @Nullable name: str) -> PlayerProfile:
        """
        Creates a new {@link PlayerProfile}.

        @param uniqueId the unique id
        @param name the name
        @return the new PlayerProfile
        """
        ...

    @staticmethod
        def createPlayerProfile(@NotNull uniqueId: UUID) -> PlayerProfile:
        """
        Creates a new {@link PlayerProfile}.

        @param uniqueId the unique id
        @return the new PlayerProfile
        """
        ...

    @staticmethod
        def createPlayerProfile(@NotNull name: str) -> PlayerProfile:
        """
        Creates a new {@link PlayerProfile}.

        @param name the name
        @return the new PlayerProfile
        """
        ...

    @staticmethod
        def getIPBans() -> Set[str]:
        """
        Gets a set containing all current IPs that are banned.

        @return a set containing banned IP addresses
        """
        ...

    @staticmethod
    @Deprecated(since="1.20.1")
    def banIP(@NotNull address: str) -> None:
        """
        Bans the specified address from the server.

        @param address the IP address to ban
        """
        ...

    @staticmethod
    @Deprecated(since="1.20.1")
    def unbanIP(@NotNull address: str) -> None:
        """
        Unbans the specified address from the server.

        @param address the IP address to unban
        """
        ...

    @staticmethod
    def banIP(@NotNull address: InetAddress) -> None:
        """
        Bans the specified address from the server.

        @param address the IP address to ban
        """
        ...

    @staticmethod
    def unbanIP(@NotNull address: InetAddress) -> None:
        """
        Unbans the specified address from the server.

        @param address the IP address to unban
        """
        ...

    @staticmethod
        def getBannedPlayers() -> Set[OfflinePlayer]:
        """
        Gets a set containing all banned players.

        @return a set containing banned players
        """
        ...

    @staticmethod
        def getBanList(@NotNull type: BanList.Type) -> BanList:
        """
        Gets a ban list for the supplied type.

        @param type the type of list to fetch, cannot be null
        @param <T> The ban target
        @return a ban list of the specified type
        """
        ...

    @staticmethod
        def getOperators() -> Set[OfflinePlayer]:
        """
        Gets a set containing all player operators.

        @return a set containing player operators
        """
        ...

    @staticmethod
        def getDefaultGameMode() -> GameMode:
        """
        Gets the default {@link GameMode} for new players.

        @return the default game mode
        """
        ...

    @staticmethod
    def setDefaultGameMode(@NotNull mode: GameMode) -> None:
        """
        Sets the default {@link GameMode} for new players.

        @param mode the new game mode
        """
        ...

    @staticmethod
        def getConsoleSender() -> ConsoleCommandSender:
        """
        Gets a {@link ConsoleCommandSender} that may be used as an input source for this server.

        @return a console command sender
        """
        ...

    @staticmethod
        def getWorldContainer() -> File:
        """
        Gets the folder that contains all of the various {@link World}s.

        @return folder that contains all worlds
        """
        ...

    @staticmethod
        def getOfflinePlayers() -> List[OfflinePlayer]:
        """
        Gets every player that has ever played on this server.

        @return an array containing all previous players
        """
        ...

    @staticmethod
        def getMessenger() -> Messenger:
        """
        Gets the {@link Messenger} responsible for this server.

        @return messenger responsible for this server
        """
        ...

    @staticmethod
        def getHelpMap() -> HelpMap:
        """
        Gets the {@link HelpMap} providing help topics for this server.

        @return a help map for this server
        """
        ...

    @staticmethod
        def createInventory(@Nullable owner: InventoryHolder, @NotNull type: InventoryType) -> Inventory:
        """
        Creates an empty inventory with the specified type.

        @param owner the holder of the inventory, or null to indicate no holder
        @param type the type of inventory to create
        @return a new inventory
        """
        ...

    @staticmethod
        def createInventory(@Nullable owner: InventoryHolder, @NotNull type: InventoryType, @NotNull title: str) -> Inventory:
        """
        Creates an empty inventory with the specified type and title.

        @param owner The holder of the inventory; can be null if there's no holder.
        @param type The type of inventory to create.
        @param title The title of the inventory, to be displayed when it is viewed.
        @return The new inventory.
        """
        ...

    @staticmethod
        def createInventory(@Nullable owner: InventoryHolder, size: int) -> Inventory:
        """
        Creates an empty inventory of type {@link InventoryType#CHEST} with the specified size.

        @param owner the holder of the inventory, or null to indicate no holder
        @param size a multiple of 9 as the size of inventory to create
        @return a new inventory
        """
        ...

    @staticmethod
        def createInventory(@Nullable owner: InventoryHolder, size: int, @NotNull title: str) -> Inventory:
        """
        Creates an empty inventory of type {@link InventoryType#CHEST} with the specified size and title.

        @param owner the holder of the inventory, or null to indicate no holder
        @param size a multiple of 9 as the size of inventory to create
        @param title the title of the inventory, displayed when inventory is viewed
        @return a new inventory
        """
        ...

    @staticmethod
        def createMerchant(@Nullable title: str) -> Merchant:
        """
        Creates an empty merchant.

        @param title the title of the corresponding merchant inventory, displayed when the merchant inventory is viewed
        @return a new merchant
        """
        ...

    @staticmethod
        def createMerchant() -> Merchant:
        """
        Creates an empty merchant.

        @return a new merchant
        """
        ...

    @staticmethod
    def getMaxChainedNeighborUpdates() -> int:
        """
        Gets the amount of consecutive neighbor updates before skipping additional ones.

        @return the amount of consecutive neighbor updates
        """
        ...

    @staticmethod
    @Deprecated(since="1.18.1")
    def getMonsterSpawnLimit() -> int:
        """
        Gets user-specified limit for number of monsters that can spawn in a chunk.

        @return the monster spawn limit
        """
        ...

    @staticmethod
    @Deprecated(since="1.18.1")
    def getAnimalSpawnLimit() -> int:
        """
        Gets user-specified limit for number of animals that can spawn in a chunk.

        @return the animal spawn limit
        """
        ...

    @staticmethod
    @Deprecated(since="1.18.1")
    def getWaterAnimalSpawnLimit() -> int:
        """
        Gets user-specified limit for number of water animals that can spawn in a chunk.

        @return the water animal spawn limit
        """
        ...

    @staticmethod
    @Deprecated(since="1.18.1")
    def getWaterAmbientSpawnLimit() -> int:
        """
        Gets user-specified limit for number of water ambient mobs that can spawn in a chunk.

        @return the water ambient spawn limit
        """
        ...

    @staticmethod
    @Deprecated(since="1.18.1")
    def getWaterUndergroundCreatureSpawnLimit() -> int:
        """
        Get user-specified limit for number of water creature underground that can spawn in a chunk.

        @return the water underground creature limit
        """
        ...

    @staticmethod
    @Deprecated(since="1.18.1")
    def getAmbientSpawnLimit() -> int:
        """
        Gets user-specified limit for number of ambient mobs that can spawn in a chunk.

        @return the ambient spawn limit
        """
        ...

    @staticmethod
    def getSpawnLimit(@NotNull spawnCategory: SpawnCategory) -> int:
        """
        Gets user-specified limit for number of {@link SpawnCategory} mobs that can spawn in a chunk.

        @param spawnCategory the category spawn
        @return the {@link SpawnCategory} spawn limit
        """
        ...

    @staticmethod
    def isPrimaryThread() -> bool:
        """
        Checks the current thread against the expected primary thread for the server.

        @return true if the current thread matches the expected primary thread, false otherwise
        """
        ...

    @staticmethod
        def getMotd() -> str:
        """
        Gets the message that is displayed on the server list.

        @return the servers MOTD
        """
        ...

    @staticmethod
    def setMotd(@NotNull motd: str) -> None:
        """
        Set the message that is displayed on the server list.

        @param motd The message to be displayed
        """
        ...

    @staticmethod
            def getServerLinks() -> ServerLinks:
        """
        Gets the server links which will be sent to clients

        @return the server's links
        """
        ...

    @staticmethod
        def getShutdownMessage() -> Optional[str]:
        """
        Gets the default message that is displayed when the server is stopped.

        @return the shutdown message
        """
        ...

    @staticmethod
        def getWarningState() -> Warning.WarningState:
        """
        Gets the current warning state for the server.

        @return the configured warning state
        """
        ...

    @staticmethod
        def getItemFactory() -> ItemFactory:
        """
        Gets the instance of the item factory (for {@link ItemMeta}).

        @return the item factory
        """
        ...

    @staticmethod
        def getEntityFactory() -> EntityFactory:
        """
        Gets the instance of the entity factory (for {@link EntitySnapshot}).

        @return the entity factory
        """
        ...

    @staticmethod
        def getScoreboardManager() -> Optional[ScoreboardManager]:
        """
        Gets the instance of the scoreboard manager.

        @return the scoreboard manager or null if no worlds are loaded.
        """
        ...

    @staticmethod
        def getScoreboardCriteria(@NotNull name: str) -> Criteria:
        """
        Get (or create) a new {@link Criteria} by its name.

        @param name the criteria name
        @return the criteria
        """
        ...

    @staticmethod
        def getServerIcon() -> Optional[CachedServerIcon]:
        """
        Gets an instance of the server's default server-icon.

        @return the default server-icon; null values may be used by the implementation to indicate no defined icon
        """
        ...

    @staticmethod
        def loadServerIcon(@NotNull file: File) -> CachedServerIcon:
        """
        Loads an image from a file, and returns a cached image for the specific server-icon.

        @param file the file to load the from
        @return a cached server-icon that can be used for a {@link ServerListPingEvent#setServerIcon(CachedServerIcon)}
        """
        ...

    @staticmethod
        def loadServerIcon(@NotNull image: BufferedImage) -> CachedServerIcon:
        """
        Creates a cached server-icon for the specific image.

        @param image the image to use
        @return a cached server-icon that can be used for a {@link ServerListPingEvent#setServerIcon(CachedServerIcon)}
        """
        ...

    @staticmethod
    def setIdleTimeout(threshold: int) -> None:
        """
        Set the idle kick timeout.

        @param threshold the idle timeout in minutes
        """
        ...

    @staticmethod
    def getIdleTimeout() -> int:
        """
        Gets the idle kick timeout.

        @return the idle timeout in minutes
        """
        ...

    @staticmethod
    def getPauseWhenEmptyTime() -> int:
        """
        Gets the pause when empty threshold seconds.

        @return the pause threshold in seconds
        """
        ...

    @staticmethod
    def setPauseWhenEmptyTime(seconds: int) -> None:
        """
        Sets the pause when empty threshold seconds.

        @param seconds the pause threshold in seconds
        """
        ...

    @staticmethod
        def createChunkData(@NotNull world: World) -> ChunkGenerator.ChunkData:
        """
        Create a ChunkData for use in a generator.

        @param world the world to create the ChunkData for
        @return a new ChunkData for the world
        """
        ...

    @staticmethod
        def createBossBar(@Nullable title: str, @NotNull color: BarColor, @NotNull style: BarStyle, @NotNull flags: BarFlag...) -> BossBar:
        """
        Creates a boss bar instance to display to players.

        @param title the title of the boss bar
        @param color the color of the boss bar
        @param style the style of the boss bar
        @param flags an optional list of flags to set on the boss bar
        @return the created boss bar
        """
        ...

    @staticmethod
        def createBossBar(@NotNull key: NamespacedKey, @Nullable title: str, @NotNull color: BarColor, @NotNull style: BarStyle, @NotNull flags: BarFlag...) -> KeyedBossBar:
        """
        Creates a boss bar instance to display to players.

        @param key the key of the boss bar that is used to access the boss bar
        @param title the title of the boss bar
        @param color the color of the boss bar
        @param style the style of the boss bar
        @param flags an optional list of flags to set on the boss bar
        @return the created boss bar
        """
        ...

    @staticmethod
        def getBossBars() -> Iterator[KeyedBossBar]:
        """
        Gets an unmodifiable iterator through all persistent bossbars.

        @return a bossbar iterator
        """
        ...

    @staticmethod
        def getBossBar(@NotNull key: NamespacedKey) -> Optional[KeyedBossBar]:
        """
        Gets the {@link KeyedBossBar} specified by this key.

        @param key unique bossbar key
        @return bossbar or null if not exists
        """
        ...

    @staticmethod
    def removeBossBar(@NotNull key: NamespacedKey) -> bool:
        """
        Removes a {@link KeyedBossBar} specified by this key.

        @param key unique bossbar key
        @return true if removal succeeded or false
        """
        ...

    @staticmethod
        def getEntity(@NotNull uuid: UUID) -> Optional[Entity]:
        """
        Gets an entity on the server by its UUID

        @param uuid the UUID of the entity
        @return the entity with the given UUID, or null if it isn't found
        """
        ...

    @staticmethod
        def getAdvancement(@NotNull key: NamespacedKey) -> Optional[Advancement]:
        """
        Get the advancement specified by this key.

        @param key unique advancement key
        @return advancement or null if not exists
        """
        ...

    @staticmethod
        def advancementIterator() -> Iterator[Advancement]:
        """
        Get an iterator through all advancements.

        @return an advancement iterator
        """
        ...

    @staticmethod
        def createBlockData(@NotNull material: Material) -> BlockData:
        """
        Creates a new {@link BlockData} instance for the specified Material.

        @param material the material
        @return new data instance
        """
        ...

    @staticmethod
        def createBlockData(@NotNull material: Material, @Nullable consumer: Consumer[BlockData]) -> BlockData:
        """
        Creates a new {@link BlockData} instance for the specified Material.

        @param material the material
        @param consumer consumer to run on new instance before returning
        @return new data instance
        """
        ...

    @staticmethod
        def createBlockData(@NotNull data: str) -> BlockData:
        """
        Creates a new {@link BlockData} instance with material and properties parsed from provided data.

        @param data data string
        @return new data instance
        """
        ...

    @staticmethod
        @Contract("null, null -> fail")
    def createBlockData(@Nullable material: Material, @Nullable data: str) -> BlockData:
        """
        Creates a new {@link BlockData} instance for the specified Material.

        @param material the material
        @param data data string
        @return new data instance
        """
        ...

    @staticmethod
        def getTag(@NotNull registry: str, @NotNull tag: NamespacedKey, @NotNull clazz: Class[T]) -> Optional[Tag[T]]:
        """
        Gets a tag which has already been defined within the server.

        @param registry the tag registry to look at
        @param tag the name of the tag
        @param clazz the class of the tag entries
        @return the tag or null
        """
        ...

    @staticmethod
        def getTags(@NotNull registry: str, @NotNull clazz: Class[T]) -> Iterable[Tag[T]]:
        """
        Gets a all tags which have been defined within the server.

        @param registry the tag registry to look at
        @param clazz the class of the tag entries
        @return all defined tags
        """
        ...

    @staticmethod
        def getLootTable(@NotNull key: NamespacedKey) -> Optional[LootTable]:
        """
        Gets the specified {@link LootTable}.

        @param key the name of the LootTable
        @return the LootTable, or null if no LootTable is found with that name
        """
        ...

    @staticmethod
        def selectEntities(@NotNull sender: CommandSender, @NotNull selector: str) -> List[Entity]:
        """
        Selects entities using the given Vanilla selector.

        @param sender the sender to execute as, must be provided
        @param selector the selection string
        @return a list of the selected entities
        """
        ...

    @staticmethod
        def getStructureManager() -> StructureManager:
        """
        Gets the structure manager for loading and saving structures.

        @return the structure manager
        """
        ...

    @staticmethod
        def getRegistry(@NotNull tClass: Class[T]) -> Optional[Registry[T]]:
        """
        Returns the registry for the given class.

        @param tClass of the registry to get
        @return the corresponding registry or null if not present
        """
        ...

    @staticmethod
        def getUnsafe() -> UnsafeValues:
        """
        @return the unsafe values instance
        """
        ...
from typing import Collection, Dict, Optional, Tuple, Union
from java.net import InetAddress, InetSocketAddress
from java.time import Duration, Instant
from java.util import Date, Map, UUID, CompletableFuture
from org.bukkit import (
    BanEntry,
    DyeColor,
    Effect,
    GameMode,
    Input,
    Instrument,
    Location,
    Material,
    NamespacedKey,
    Note,
    OfflinePlayer,
    Particle,
    Server,
    ServerLinks,
    Sound,
    SoundCategory,
    WeatherType,
    WorldBorder,
)
from org.bukkit.advancement import Advancement, AdvancementProgress
from org.bukkit.ban import IpBanList, ProfileBanList
from org.bukkit.block import Block, BlockState, Sign
from org.bukkit.block.data import BlockData
from org.bukkit.block.sign import Side
from org.bukkit.conversations import Conversable
from org.bukkit.event.block import BlockBreakEvent, BlockDropItemEvent
from org.bukkit.event.player import (
    PlayerExpCooldownChangeEvent,
    PlayerResourcePackStatusEvent,
)
from org.bukkit.inventory import EquipmentSlot, ItemStack
from org.bukkit.map import MapView
from org.bukkit.plugin import Plugin
from org.bukkit.plugin.messaging import PluginMessageRecipient
from org.bukkit.potion import PotionEffect, PotionEffectType
from org.bukkit.profile import PlayerProfile
from org.bukkit.scoreboard import Scoreboard
from org.bukkit.entity import HumanEntity
from org.jetbrains.annotations import ApiStatus

class Player(HumanEntity, OfflinePlayer, Conversable, PluginMessageRecipient):
    """
    Represents a player, connected or not
    """

        def getName(self) -> str:
        """Gets the name of the player."""
        ...

        def getDisplayName(self) -> str:
        """
        Gets the "friendly" name to display of this player. This may include
        color.
        """
        ...

    def setDisplayName(self, name: Optional[str]) -> None:
        """
        Sets the "friendly" name to display of this player. This may include
        color.
        """
        ...

        def getPlayerListName(self) -> str:
        """Gets the name that is shown on the player list."""
        ...

    def setPlayerListName(self, name: Optional[str]) -> None:
        """
        Sets the name that is shown on the in-game player list.
        """
        ...

    def getPlayerListOrder(self) -> int:
        """Gets the relative order that the player is shown on the player list."""
        ...

    def setPlayerListOrder(self, order: int) -> None:
        """
        Sets the relative order that the player is shown on the in-game player
        list.
        """
        ...


    def getPlayerListHeader(self) -> Optional[str]:
        """Gets the currently displayed player list header for this player."""
        ...


    def getPlayerListFooter(self) -> Optional[str]:
        """Gets the currently displayed player list footer for this player."""
        ...

    def setPlayerListHeader(self, header: Optional[str]) -> None:
        """Sets the currently displayed player list header for this player."""
        ...

    def setPlayerListFooter(self, footer: Optional[str]) -> None:
        """Sets the currently displayed player list footer for this player."""
        ...

    def setPlayerListHeaderFooter(
        self, header: Optional[str], footer: Optional[str]
    ) -> None:
        """Sets the currently displayed player list header and footer for this player."""
        ...

    def setCompassTarget(self, loc: Location) -> None:
        """Set the target of the player's compass."""
        ...

        def getCompassTarget(self) -> Location:
        """Get the previously set compass target."""
        ...


    def getAddress(self) -> Optional[InetSocketAddress]:
        """Gets the socket address of this player."""
        ...

    def isTransferred(self) -> bool:
        """Gets if this connection has been transferred from another server."""
        ...

        def retrieveCookie(self, key: NamespacedKey) -> CompletableFuture[Optional[bytes]]:
        """
        Retrieves a cookie from this player.
        """
        ...

    def storeCookie(self, key: NamespacedKey, value: bytes) -> None:
        """Stores a cookie in this player's client."""
        ...

    def transfer(self, host: str, port: int) -> None:
        """Requests this player to connect to a different server specified by host and port."""
        ...

    def sendRawMessage(self, message: str) -> None:
        """Sends this sender a message raw."""
        ...

    def kickPlayer(self, message: Optional[str]) -> None:
        """Kicks player with custom kick message."""
        ...


    def ban(
        self,
        reason: Optional[str],
        expires: Optional[Date],
        source: Optional[str],
        kickPlayer: bool,
    ) -> Optional[BanEntry[PlayerProfile]]:
        """Adds this user to the ProfileBanList."""
        ...


    def ban(
        self,
        reason: Optional[str],
        expires: Optional[Instant],
        source: Optional[str],
        kickPlayer: bool,
    ) -> Optional[BanEntry[PlayerProfile]]:
        """Adds this user to the ProfileBanList."""
        ...


    def ban(
        self,
        reason: Optional[str],
        duration: Optional[Duration],
        source: Optional[str],
        kickPlayer: bool,
    ) -> Optional[BanEntry[PlayerProfile]]:
        """Adds this user to the ProfileBanList."""
        ...


    def banIp(
        self,
        reason: Optional[str],
        expires: Optional[Date],
        source: Optional[str],
        kickPlayer: bool,
    ) -> Optional[BanEntry[InetAddress]]:
        """Adds this user's current IP address to the IpBanList."""
        ...


    def banIp(
        self,
        reason: Optional[str],
        expires: Optional[Instant],
        source: Optional[str],
        kickPlayer: bool,
    ) -> Optional[BanEntry[InetAddress]]:
        """Adds this user's current IP address to the IpBanList."""
        ...


    def banIp(
        self,
        reason: Optional[str],
        duration: Optional[Duration],
        source: Optional[str],
        kickPlayer: bool,
    ) -> Optional[BanEntry[InetAddress]]:
        """Adds this user's current IP address to the IpBanList."""
        ...

    def chat(self, msg: str) -> None:
        """Says a message (or runs a command)."""
        ...

    def performCommand(self, command: str) -> bool:
        """Makes the player perform the given command."""
        ...

    def isOnGround(self) -> bool:
        """Returns true if the entity is supported by a block."""
        ...

    def isSneaking(self) -> bool:
        """Returns if the player is in sneak mode."""
        ...

    def setSneaking(self, sneak: bool) -> None:
        """Sets the sneak mode of the player."""
        ...

    def isSprinting(self) -> bool:
        """Gets whether the player is sprinting or not."""
        ...

    def setSprinting(self, sprinting: bool) -> None:
        """Sets whether the player is sprinting or not."""
        ...

    def saveData(self) -> None:
        """Saves the player's current location, health, inventory, motion, and other information."""
        ...

    def loadData(self) -> None:
        """Loads the player's current location, health, inventory, motion, and other information."""
        ...

    def setSleepingIgnored(self, isSleeping: bool) -> None:
        """Sets whether the player is ignored as not sleeping."""
        ...

    def isSleepingIgnored(self) -> bool:
        """Returns whether the player is sleeping ignored."""
        ...


    def getBedSpawnLocation(self) -> Optional[Location]:
        """Gets the Location where the player will spawn at their bed."""
        ...


    def getRespawnLocation(self) -> Optional[Location]:
        """Gets the Location where the player will spawn at."""
        ...

    def setBedSpawnLocation(self, location: Optional[Location]) -> None:
        """Sets the Location where the player will spawn at their bed."""
        ...

    def setRespawnLocation(self, location: Optional[Location]) -> None:
        """Sets the Location where the player will respawn."""
        ...

    def setBedSpawnLocation(self, location: Optional[Location], force: bool) -> None:
        """Sets the Location where the player will spawn at their bed."""
        ...

    def setRespawnLocation(self, location: Optional[Location], force: bool) -> None:
        """Sets the Location where the player will respawn."""
        ...

    def getEnderPearls(self) -> Collection[EnderPearl]:
        """Gets the ender pearls currently associated with this entity."""
        ...

    def getCurrentInput(self) -> Input:
        """Gets the current movement input, as last provided by the player."""
        ...

    def playNote(self, loc: Location, instrument: Instrument, note: Note) -> None:
        """Play a note for the player at a location."""
        ...

    def playSound(
        self, location: Location, sound: Sound, volume: float, pitch: float
    ) -> None:
        """Play a sound for a player at the location."""
        ...

    def playSound(
        self, location: Location, sound: str, volume: float, pitch: float
    ) -> None:
        """Play a sound for a player at the location."""
        ...

    def playSound(
        self,
        location: Location,
        sound: Sound,
        category: SoundCategory,
        volume: float,
        pitch: float,
    ) -> None:
        """Play a sound for a player at the location."""
        ...

    def playSound(
        self,
        location: Location,
        sound: str,
        category: SoundCategory,
        volume: float,
        pitch: float,
    ) -> None:
        """Play a sound for a player at the location."""
        ...

    def playSound(
        self,
        location: Location,
        sound: Sound,
        category: SoundCategory,
        volume: float,
        pitch: float,
        seed: int,
    ) -> None:
        """Play a sound for a player at the location."""
        ...

    def playSound(
        self,
        location: Location,
        sound: str,
        category: SoundCategory,
        volume: float,
        pitch: float,
        seed: int,
    ) -> None:
        """Play a sound for a player at the location."""
        ...

    def playSound(
        self, entity: Entity, sound: Sound, volume: float, pitch: float
    ) -> None:
        """Play a sound for a player at the location of the entity."""
        ...

    def playSound(
        self, entity: Entity, sound: str, volume: float, pitch: float
    ) -> None:
        """Play a sound for a player at the location of the entity."""
        ...

    def playSound(
        self,
        entity: Entity,
        sound: Sound,
        category: SoundCategory,
        volume: float,
        pitch: float,
    ) -> None:
        """Play a sound for a player at the location of the entity."""
        ...

    def playSound(
        self,
        entity: Entity,
        sound: str,
        category: SoundCategory,
        volume: float,
        pitch: float,
    ) -> None:
        """Play a sound for a player at the location of the entity."""
        ...

    def playSound(
        self,
        entity: Entity,
        sound: Sound,
        category: SoundCategory,
        volume: float,
        pitch: float,
        seed: int,
    ) -> None:
        """Play a sound for a player at the location of the entity."""
        ...

    def playSound(
        self,
        entity: Entity,
        sound: str,
        category: SoundCategory,
        volume: float,
        pitch: float,
        seed: int,
    ) -> None:
        """Play a sound for a player at the location of the entity."""
        ...

    def stopSound(self, sound: Sound) -> None:
        """Stop the specified sound from playing."""
        ...

    def stopSound(self, sound: str) -> None:
        """Stop the specified sound from playing."""
        ...

    def stopSound(self, sound: Sound, category: Optional[SoundCategory]) -> None:
        """Stop the specified sound from playing."""
        ...

    def stopSound(self, sound: str, category: Optional[SoundCategory]) -> None:
        """Stop the specified sound from playing."""
        ...

    def stopSound(self, category: SoundCategory) -> None:
        """Stop the specified sound category from playing."""
        ...

    def stopAllSounds(self) -> None:
        """Stop all sounds from playing."""
        ...

    @Deprecated(since="1.6.2")
    def playEffect(self, loc: Location, effect: Effect, data: int) -> None:
        """Plays an effect to just this player."""
        ...

    def playEffect(self, loc: Location, effect: Effect, data: Optional[T]) -> None:
        """Plays an effect to just this player."""
        ...

    def breakBlock(self, block: Block) -> bool:
        """Force this player to break a Block using the item in their main hand."""
        ...

    @Deprecated(since="1.6.2")
    def sendBlockChange(self, loc: Location, material: Material, data: byte) -> None:
        """Send a block change."""
        ...

    def sendBlockChange(self, loc: Location, block: BlockData) -> None:
        """Send a block change."""
        ...

    def sendBlockChanges(self, blocks: Collection[BlockState]) -> None:
        """Send a multi-block change."""
        ...

    def sendBlockChanges(
        self, blocks: Collection[BlockState], suppressLightUpdates: bool
    ) -> None:
        """Send a multi-block change."""
        ...

    def sendBlockDamage(self, loc: Location, progress: float) -> None:
        """Send block damage."""
        ...

    def sendBlockDamage(self, loc: Location, progress: float, source: Entity) -> None:
        """Send block damage."""
        ...

    def sendBlockDamage(self, loc: Location, progress: float, sourceId: int) -> None:
        """Send block damage."""
        ...

    def sendEquipmentChange(
        self, entity: LivingEntity, slot: EquipmentSlot, item: Optional[ItemStack]
    ) -> None:
        """Send an equipment change for the target entity."""
        ...

    def sendEquipmentChange(
        self, entity: LivingEntity, items: Dict[EquipmentSlot, ItemStack]
    ) -> None:
        """Send multiple equipment changes for the target entity."""
        ...

    def sendSignChange(self, loc: Location, lines: Optional[Tuple[str]]) -> None:
        """Send a sign change."""
        ...

    def sendSignChange(
        self, loc: Location, lines: Optional[Tuple[str]], dyeColor: DyeColor
    ) -> None:
        """Send a sign change."""
        ...

    def sendSignChange(
        self,
        loc: Location,
        lines: Optional[Tuple[str]],
        dyeColor: DyeColor,
        hasGlowingText: bool,
    ) -> None:
        """Send a sign change."""
        ...


    def sendBlockUpdate(self, loc: Location, tileState: TileState) -> None:
        """Send a TileState change."""
        ...

    def sendPotionEffectChange(
        self, entity: LivingEntity, effect: PotionEffect
    ) -> None:
        """Change a potion effect for the target entity."""
        ...

    def sendPotionEffectChangeRemove(
        self, entity: LivingEntity, type: PotionEffectType
    ) -> None:
        """Remove a potion effect for the target entity."""
        ...

    def sendMap(self, map: MapView) -> None:
        """Render a map and send it to the player in its entirety."""
        ...

    def sendHurtAnimation(self, yaw: float) -> None:
        """Send a hurt animation."""
        ...

    def sendLinks(self, links: ServerLinks) -> None:
        """Sends the given server links to the player."""
        ...

    def addCustomChatCompletions(self, completions: Collection[str]) -> None:
        """Add custom chat completion suggestions shown to the player while typing a message."""
        ...

    def removeCustomChatCompletions(self, completions: Collection[str]) -> None:
        """Remove custom chat completion suggestions shown to the player while typing a message."""
        ...

    def setCustomChatCompletions(self, completions: Collection[str]) -> None:
        """Set the list of chat completion suggestions shown to the player while typing a message."""
        ...

    @ApiStatus.Internal
    def updateInventory(self) -> None:
        """Forces an update of the player's entire inventory."""
        ...


    def getPreviousGameMode(self) -> Optional[GameMode]:
        """Gets this player's previous GameMode."""
        ...

    def setPlayerTime(self, time: int, relative: bool) -> None:
        """Sets the current time on the player's client."""
        ...

    def getPlayerTime(self) -> int:
        """Returns the player's current timestamp."""
        ...

    def getPlayerTimeOffset(self) -> int:
        """Returns the player's current time offset relative to server time."""
        ...

    def isPlayerTimeRelative(self) -> bool:
        """Returns true if the player's time is relative to the server time."""
        ...

    def resetPlayerTime(self) -> None:
        """Restores the normal condition where the player's time is synchronized with the server time."""
        ...

    def setPlayerWeather(self, type: WeatherType) -> None:
        """Sets the type of weather the player will see."""
        ...


    def getPlayerWeather(self) -> Optional[WeatherType]:
        """Returns the type of weather the player is currently experiencing."""
        ...

    def resetPlayerWeather(self) -> None:
        """Restores the normal condition where the player's weather is controlled by server conditions."""
        ...

    def getExpCooldown(self) -> int:
        """Gets the player's cooldown between picking up experience orbs."""
        ...

    def setExpCooldown(self, ticks: int) -> None:
        """Sets the player's cooldown between picking up experience orbs."""
        ...

    def giveExp(self, amount: int) -> None:
        """Gives the player the amount of experience specified."""
        ...

    def giveExpLevels(self, amount: int) -> None:
        """Gives the player the amount of experience levels specified."""
        ...

    def getExp(self) -> float:
        """Gets the player's current experience points towards the next level."""
        ...

    def setExp(self, exp: float) -> None:
        """Sets the player's current experience points towards the next level."""
        ...

    def getLevel(self) -> int:
        """Gets the player's current experience level."""
        ...

    def setLevel(self, level: int) -> None:
        """Sets the player's current experience level."""
        ...

    def getTotalExperience(self) -> int:
        """Gets the player's total experience points."""
        ...

    def setTotalExperience(self, exp: int) -> None:
        """Sets the player's current experience points."""
        ...

    def sendExperienceChange(self, progress: float) -> None:
        """Send an experience change."""
        ...

    def sendExperienceChange(self, progress: float, level: int) -> None:
        """Send an experience change."""
        ...

    def getAllowFlight(self) -> bool:
        """Determines if the Player is allowed to fly via jump key double-tap."""
        ...

    def setAllowFlight(self, flight: bool) -> None:
        """Sets if the Player is allowed to fly via jump key double-tap."""
        ...

    @Deprecated(since="1.12.2")
    def hidePlayer(self, player: Player) -> None:
        """Hides a player from this player."""
        ...

    def hidePlayer(self, plugin: Plugin, player: Player) -> None:
        """Hides a player from this player."""
        ...

    @Deprecated(since="1.12.2")
    def showPlayer(self, player: Player) -> None:
        """Allows this player to see a player that was previously hidden."""
        ...

    def showPlayer(self, plugin: Plugin, player: Player) -> None:
        """Allows this player to see a player that was previously hidden."""
        ...

    def canSee(self, player: Player) -> bool:
        """Checks to see if a player has been hidden from this player."""
        ...

    def hideEntity(self, plugin: Plugin, entity: Entity) -> None:
        """Visually hides an entity from this player."""
        ...

    def showEntity(self, plugin: Plugin, entity: Entity) -> None:
        """Allows this player to see an entity that was previously hidden."""
        ...

    def canSee(self, entity: Entity) -> bool:
        """Checks to see if an entity has been visually hidden from this player."""
        ...

    def isFlying(self) -> bool:
        """Checks to see if this player is currently flying or not."""
        ...

    def setFlying(self, value: bool) -> None:
        """Makes this player start or stop flying."""
        ...

    def setFlySpeed(self, value: float) -> None:
        """Sets the speed at which a client will fly."""
        ...

    def setWalkSpeed(self, value: float) -> None:
        """Sets the speed at which a client will walk."""
        ...

    def getFlySpeed(self) -> float:
        """Gets the current allowed speed that a client can fly."""
        ...

    def getWalkSpeed(self) -> float:
        """Gets the current allowed speed that a client can walk."""
        ...

    @Deprecated(since="1.7.2")
    def setTexturePack(self, url: str) -> None:
        """Request that the player's client download and switch texture packs."""
        ...

    def setResourcePack(self, url: str) -> None:
        """Request that the player's client download and switch resource packs."""
        ...

    def setResourcePack(self, url: str, hash: Optional[bytes]) -> None:
        """Request that the player's client download and switch resource packs."""
        ...

    def setResourcePack(
        self, url: str, hash: Optional[bytes], prompt: Optional[str]
    ) -> None:
        """Request that the player's client download and switch resource packs."""
        ...

    def setResourcePack(self, url: str, hash: Optional[bytes], force: bool) -> None:
        """Request that the player's client download and switch resource packs."""
        ...

    def setResourcePack(
        self, url: str, hash: Optional[bytes], prompt: Optional[str], force: bool
    ) -> None:
        """Request that the player's client download and switch resource packs."""
        ...

    def setResourcePack(
        self,
        id: UUID,
        url: str,
        hash: Optional[bytes],
        prompt: Optional[str],
        force: bool,
    ) -> None:
        """Request that the player's client download and switch resource packs."""
        ...

    def addResourcePack(
        self,
        id: UUID,
        url: str,
        hash: Optional[bytes],
        prompt: Optional[str],
        force: bool,
    ) -> None:
        """Request that the player's client download and include another resource pack."""
        ...

    def removeResourcePack(self, id: UUID) -> None:
        """Request that the player's client remove a resource pack sent by the server."""
        ...

    def removeResourcePacks(self) -> None:
        """Request that the player's client remove all loaded resource pack sent by the server."""
        ...

        def getScoreboard(self) -> Scoreboard:
        """Gets the Scoreboard displayed to this player."""
        ...

    def setScoreboard(self, scoreboard: Scoreboard) -> None:
        """Sets the player's visible Scoreboard."""
        ...


    def getWorldBorder(self) -> Optional[WorldBorder]:
        """Gets the WorldBorder visible to this Player."""
        ...

    def setWorldBorder(self, border: Optional[WorldBorder]) -> None:
        """Sets the WorldBorder visible to this Player."""
        ...

    def sendHealthUpdate(
        self, health: float, foodLevel: int, saturation: float
    ) -> None:
        """Send a health update to the player."""
        ...

    def sendHealthUpdate(self) -> None:
        """Send a health update to the player using its known server values."""
        ...

    def isHealthScaled(self) -> bool:
        """Gets if the client is displayed a 'scaled' health."""
        ...

    def setHealthScaled(self, scale: bool) -> None:
        """Sets if the client is displayed a 'scaled' health."""
        ...

    def setHealthScale(self, scale: float) -> None:
        """Sets the number to scale health to for the client."""
        ...

    def getHealthScale(self) -> float:
        """Gets the number that health is scaled to for the client."""
        ...


    def getSpectatorTarget(self) -> Optional[Entity]:
        """Gets the entity which is followed by the camera when in GameMode.SPECTATOR."""
        ...

    def setSpectatorTarget(self, entity: Optional[Entity]) -> None:
        """Sets the entity which is followed by the camera when in GameMode.SPECTATOR."""
        ...

    @Deprecated(since="1.8.7")
    def sendTitle(self, title: Optional[str], subtitle: Optional[str]) -> None:
        """Sends a title and a subtitle message to the player."""
        ...

    def sendTitle(
        self,
        title: Optional[str],
        subtitle: Optional[str],
        fadeIn: int,
        stay: int,
        fadeOut: int,
    ) -> None:
        """Sends a title and a subtitle message to the player."""
        ...

    def resetTitle(self) -> None:
        """Resets the title displayed to the player."""
        ...

    def spawnParticle(self, particle: Particle, location: Location, count: int) -> None:
        """Spawns the particle at the target location."""
        ...

    def spawnParticle(
        self, particle: Particle, x: float, y: float, z: float, count: int
    ) -> None:
        """Spawns the particle at the target location."""
        ...

    def spawnParticle(
        self, particle: Particle, location: Location, count: int, data: Optional[T]
    ) -> None:
        """Spawns the particle at the target location."""
        ...

    def spawnParticle(
        self,
        particle: Particle,
        x: float,
        y: float,
        z: float,
        count: int,
        data: Optional[T],
    ) -> None:
        """Spawns the particle at the target location."""
        ...

    def spawnParticle(
        self,
        particle: Particle,
        location: Location,
        count: int,
        offsetX: float,
        offsetY: float,
        offsetZ: float,
    ) -> None:
        """Spawns the particle at the target location."""
        ...

    def spawnParticle(
        self,
        particle: Particle,
        x: float,
        y: float,
        z: float,
        count: int,
        offsetX: float,
        offsetY: float,
        offsetZ: float,
    ) -> None:
        """Spawns the particle at the target location."""
        ...

    def spawnParticle(
        self,
        particle: Particle,
        location: Location,
        count: int,
        offsetX: float,
        offsetY: float,
        offsetZ: float,
        extra: float,
    ) -> None:
        """Spawns the particle at the target location."""
        ...

    def spawnParticle(
        self,
        particle: Particle,
        x: float,
        y: float,
        z: float,
        count: int,
        offsetX: float,
        offsetY: float,
        offsetZ: float,
        extra: float,
    ) -> None:
        """Spawns the particle at the target location."""
        ...

    def spawnParticle(
        self,
        particle: Particle,
        location: Location,
        count: int,
        offsetX: float,
        offsetY: float,
        offsetZ: float,
        extra: float,
        data: Optional[T],
    ) -> None:
        """Spawns the particle at the target location."""
        ...

    def spawnParticle(
        self,
        particle: Particle,
        x: float,
        y: float,
        z: float,
        count: int,
        offsetX: float,
        offsetY: float,
        offsetZ: float,
        extra: float,
        data: Optional[T],
    ) -> None:
        """Spawns the particle at the target location."""
        ...

    def spawnParticle(
        self,
        particle: Particle,
        location: Location,
        count: int,
        offsetX: float,
        offsetY: float,
        offsetZ: float,
        extra: float,
        data: Optional[T],
        force: bool,
    ) -> None:
        """Spawns the particle at the target location."""
        ...

    def spawnParticle(
        self,
        particle: Particle,
        x: float,
        y: float,
        z: float,
        count: int,
        offsetX: float,
        offsetY: float,
        offsetZ: float,
        extra: float,
        data: Optional[T],
        force: bool,
    ) -> None:
        """Spawns the particle at the target location."""
        ...

    def getAdvancementProgress(self, advancement: Advancement) -> AdvancementProgress:
        """Return the player's progression on the specified advancement."""
        ...

    def getClientViewDistance(self) -> int:
        """Get the player's current client side view distance."""
        ...

    def getPing(self) -> int:
        """Gets the player's estimated ping in milliseconds."""
        ...

        def getLocale(self) -> str:
        """Gets the player's current locale."""
        ...

    def updateCommands(self) -> None:
        """Update the list of commands sent to the client."""
        ...

    def openBook(self, book: ItemStack) -> None:
        """Open a Material.WRITTEN_BOOK for a Player."""
        ...

    def openSign(self, sign: Sign) -> None:
        """Open a Sign for editing by the Player."""
        ...

    def openSign(self, sign: Sign, side: Side) -> None:
        """Open a Sign for editing by the Player."""
        ...

    def showDemoScreen(self) -> None:
        """Shows the demo screen to the player."""
        ...

    def isAllowingServerListings(self) -> bool:
        """Gets whether the player has the "Allow Server Listings" setting enabled."""
        ...

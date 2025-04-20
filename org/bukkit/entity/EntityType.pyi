from typing import Type, Dict, Optional, Union

from org.bukkit import Bukkit
from org.bukkit.Keyed import Keyed
from org.bukkit.Location import Location
from org.bukkit.NamespacedKey import NamespacedKey
from org.bukkit.Translatable import Translatable
from org.bukkit.World import World
from org.bukkit.entity import Entity
from org.bukkit.entity import LivingEntity
from org.bukkit.entity.boat import AcaciaBoat, AcaciaChestBoat, BambooChestRaft, BambooRaft, BirchBoat, BirchChestBoat, CherryBoat, CherryChestBoat, DarkOakBoat, DarkOakChestBoat, JungleBoat, JungleChestBoat, MangroveBoat, MangroveChestBoat, OakBoat, OakChestBoat, PaleOakBoat, PaleOakChestBoat, SpruceBoat, SpruceChestBoat
from org.bukkit.entity.minecart import CommandMinecart, ExplosiveMinecart, HopperMinecart, PoweredMinecart, RideableMinecart, SpawnerMinecart, StorageMinecart
from org.bukkit.inventory import ItemStack
from org.bukkit.potion import PotionEffectType
from org.bukkit.registry import RegistryAware
from org.jetbrains.annotations import Contract, NotNull, Nullable

class EntityType(Keyed, Translatable, RegistryAware):
    """
    These strings MUST match the strings in nms.EntityTypes and are case sensitive.
    """

    ITEM: 'EntityType'
    EXPERIENCE_ORB: 'EntityType'
    AREA_EFFECT_CLOUD: 'EntityType'
    ELDER_GUARDIAN: 'EntityType'
    WITHER_SKELETON: 'EntityType'
    STRAY: 'EntityType'
    EGG: 'EntityType'
    LEASH_KNOT: 'EntityType'
    PAINTING: 'EntityType'
    ARROW: 'EntityType'
    SNOWBALL: 'EntityType'
    FIREBALL: 'EntityType'
    SMALL_FIREBALL: 'EntityType'
    ENDER_PEARL: 'EntityType'
    EYE_OF_ENDER: 'EntityType'
    SPLASH_POTION: 'EntityType'
    LINGERING_POTION: 'EntityType'
    EXPERIENCE_BOTTLE: 'EntityType'
    ITEM_FRAME: 'EntityType'
    WITHER_SKULL: 'EntityType'
    TNT: 'EntityType'
    FALLING_BLOCK: 'EntityType'
    FIREWORK_ROCKET: 'EntityType'
    HUSK: 'EntityType'
    SPECTRAL_ARROW: 'EntityType'
    SHULKER_BULLET: 'EntityType'
    DRAGON_FIREBALL: 'EntityType'
    ZOMBIE_VILLAGER: 'EntityType'
    SKELETON_HORSE: 'EntityType'
    ZOMBIE_HORSE: 'EntityType'
    ARMOR_STAND: 'EntityType'
    DONKEY: 'EntityType'
    MULE: 'EntityType'
    EVOKER_FANGS: 'EntityType'
    EVOKER: 'EntityType'
    VEX: 'EntityType'
    VINDICATOR: 'EntityType'
    ILLUSIONER: 'EntityType'
    COMMAND_BLOCK_MINECART: 'EntityType'
    MINECART: 'EntityType'
    CHEST_MINECART: 'EntityType'
    FURNACE_MINECART: 'EntityType'
    TNT_MINECART: 'EntityType'
    HOPPER_MINECART: 'EntityType'
    SPAWNER_MINECART: 'EntityType'
    CREEPER: 'EntityType'
    SKELETON: 'EntityType'
    SPIDER: 'EntityType'
    GIANT: 'EntityType'
    ZOMBIE: 'EntityType'
    SLIME: 'EntityType'
    GHAST: 'EntityType'
    ZOMBIFIED_PIGLIN: 'EntityType'
    ENDERMAN: 'EntityType'
    CAVE_SPIDER: 'EntityType'
    SILVERFISH: 'EntityType'
    BLAZE: 'EntityType'
    MAGMA_CUBE: 'EntityType'
    ENDER_DRAGON: 'EntityType'
    WITHER: 'EntityType'
    BAT: 'EntityType'
    WITCH: 'EntityType'
    ENDERMITE: 'EntityType'
    GUARDIAN: 'EntityType'
    SHULKER: 'EntityType'
    PIG: 'EntityType'
    SHEEP: 'EntityType'
    COW: 'EntityType'
    CHICKEN: 'EntityType'
    SQUID: 'EntityType'
    WOLF: 'EntityType'
    MOOSHROOM: 'EntityType'
    SNOW_GOLEM: 'EntityType'
    OCELOT: 'EntityType'
    IRON_GOLEM: 'EntityType'
    HORSE: 'EntityType'
    RABBIT: 'EntityType'
    POLAR_BEAR: 'EntityType'
    LLAMA: 'EntityType'
    LLAMA_SPIT: 'EntityType'
    PARROT: 'EntityType'
    VILLAGER: 'EntityType'
    END_CRYSTAL: 'EntityType'
    TURTLE: 'EntityType'
    PHANTOM: 'EntityType'
    TRIDENT: 'EntityType'
    COD: 'EntityType'
    SALMON: 'EntityType'
    PUFFERFISH: 'EntityType'
    TROPICAL_FISH: 'EntityType'
    DROWNED: 'EntityType'
    DOLPHIN: 'EntityType'
    CAT: 'EntityType'
    PANDA: 'EntityType'
    PILLAGER: 'EntityType'
    RAVAGER: 'EntityType'
    TRADER_LLAMA: 'EntityType'
    WANDERING_TRADER: 'EntityType'
    FOX: 'EntityType'
    BEE: 'EntityType'
    HOGLIN: 'EntityType'
    PIGLIN: 'EntityType'
    STRIDER: 'EntityType'
    ZOGLIN: 'EntityType'
    PIGLIN_BRUTE: 'EntityType'
    AXOLOTL: 'EntityType'
    GLOW_ITEM_FRAME: 'EntityType'
    GLOW_SQUID: 'EntityType'
    GOAT: 'EntityType'
    MARKER: 'EntityType'
    ALLAY: 'EntityType'
    FROG: 'EntityType'
    TADPOLE: 'EntityType'
    WARDEN: 'EntityType'
    CAMEL: 'EntityType'
    BLOCK_DISPLAY: 'EntityType'
    INTERACTION: 'EntityType'
    ITEM_DISPLAY: 'EntityType'
    SNIFFER: 'EntityType'
    TEXT_DISPLAY: 'EntityType'
    BREEZE: 'EntityType'
    WIND_CHARGE: 'EntityType'
    BREEZE_WIND_CHARGE: 'EntityType'
    ARMADILLO: 'EntityType'
    BOGGED: 'EntityType'
    OMINOUS_ITEM_SPAWNER: 'EntityType'
    ACACIA_BOAT: 'EntityType'
    ACACIA_CHEST_BOAT: 'EntityType'
    BAMBOO_RAFT: 'EntityType'
    BAMBOO_CHEST_RAFT: 'EntityType'
    BIRCH_BOAT: 'EntityType'
    BIRCH_CHEST_BOAT: 'EntityType'
    CHERRY_BOAT: 'EntityType'
    CHERRY_CHEST_BOAT: 'EntityType'
    DARK_OAK_BOAT: 'EntityType'
    DARK_OAK_CHEST_BOAT: 'EntityType'
    JUNGLE_BOAT: 'EntityType'
    JUNGLE_CHEST_BOAT: 'EntityType'
    MANGROVE_BOAT: 'EntityType'
    MANGROVE_CHEST_BOAT: 'EntityType'
    OAK_BOAT: 'EntityType'
    OAK_CHEST_BOAT: 'EntityType'
    PALE_OAK_BOAT: 'EntityType'
    PALE_OAK_CHEST_BOAT: 'EntityType'
    SPRUCE_BOAT: 'EntityType'
    SPRUCE_CHEST_BOAT: 'EntityType'
    CREAKING: 'EntityType'
    FISHING_BOBBER: 'EntityType'
    LIGHTNING_BOLT: 'EntityType'
    PLAYER: 'EntityType'
    UNKNOWN: 'EntityType'

    def __init__(self, name: Optional[str], clazz: Optional[Type[Entity]], type_id: int, independent: bool = True) -> None:
        self.name: Optional[str] = name
        self.clazz: Optional[Type[Entity]] = clazz
        self.type_id: int = type_id
        self.independent: bool = independent
        self.living: bool = clazz is not None and issubclass(clazz, LivingEntity)
        self.key: Optional[NamespacedKey] = NamespacedKey.minecraft(name) if name is not None else None

    @Deprecated
        def get_name(self) -> Optional[str]:
        """Gets the entity type name."""
        return self.name

        @Override
    @Deprecated
    def get_key(self) -> NamespacedKey:
        """Gets the key of this entity type."""
        return self.get_key_or_throw()

        def get_entity_class(self) -> Optional[Type[Entity]]:
        """Gets the entity class."""
        return self.clazz

    @Deprecated
    def get_type_id(self) -> int:
        """Gets the entity type id."""
        return self.type_id

    @Deprecated
    @Contract("null -> null")
        @staticmethod
    def from_name(name: Optional[str]) -> Optional['EntityType']:
        """Gets an entity type from its name."""
        return None

    @Deprecated
        @staticmethod
    def from_id(id: int) -> Optional['EntityType']:
        """Gets an entity from its id."""
        return None

    def is_spawnable(self) -> bool:
        """Checks if the entity type can be spawned."""
        return self.independent

    def is_alive(self) -> bool:
        """Checks if the entity type is alive."""
        return self.living

        @Override
    def get_translation_key(self) -> str:
        """Gets the translation key for this entity type."""
        return Bukkit.getUnsafe().getTranslationKey(self)

    def is_enabled_by_feature(self, world: World) -> bool:
        """Checks if this EntityType is enabled by feature in a world."""
        return Bukkit.getDataPackManager().isEnabledByFeature(self, world)

        @Override
    def get_key_or_throw(self) -> NamespacedKey:
        """Gets the key or throws an exception if not registered."""
        return self.key

        @Override
    def get_key_or_null(self) -> Optional[NamespacedKey]:
        """Gets the key or returns None if not present."""
        return self.key

    @Override
    def is_registered(self) -> bool:
        """Checks if this entity type is registered."""
        return self != EntityType.UNKNOWN
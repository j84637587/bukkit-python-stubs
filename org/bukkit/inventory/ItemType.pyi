from typing import TypeVar, Callable, Optional, Dict, Any
from collections import defaultdict
from org.bukkit import Keyed, Material, NamespacedKey, Registry, Translatable, World
from org.bukkit.attribute import Attribute, AttributeModifier
from org.bukkit.block import BlockType
from org.bukkit.inventory.meta import ArmorMeta, AxolotlBucketMeta, BannerMeta, BlockStateMeta, BookMeta, BundleMeta, ColorableArmorMeta, CompassMeta, CrossbowMeta, EnchantmentStorageMeta, FireworkEffectMeta, FireworkMeta, ItemMeta, KnowledgeBookMeta, LeatherArmorMeta, MapMeta, MusicInstrumentMeta, OminousBottleMeta, PotionMeta, ShieldMeta, SkullMeta, SpawnEggMeta, SuspiciousStewMeta, TropicalFishBucketMeta
from org.bukkit.registry import RegistryAware
from org.jetbrains.annotations import ApiStatus, NotNull, Nullable

M = TypeVar('M', bound=ItemMeta)

class ItemType(Keyed, Translatable, RegistryAware):
    """
    While this API is in a public interface, it is not intended for use by
    plugins until further notice. The purpose of these types is to make
    {@link Material} more maintenance friendly, but will in due time be the
    official replacement for the aforementioned enum. Entirely incompatible
    changes may occur. Do not use this API in plugins.
    """

        def typed(self) -> 'Typed[ItemMeta]':
        """
        Yields this item type as a typed version of itself with a plain {@link ItemMeta} representing it.

        @return: the typed item type.
        """
        pass

        def typed(self, itemMetaType: type[M]) -> 'Typed[M]':
        """
        Yields this item type as a typed version of itself with a plain {@link ItemMeta} representing it.

        @param itemMetaType: the class type of the {@link ItemMeta} to type this {@link ItemType} with.
        @return: the typed item type.
        """
        pass

        def createItemStack(self) -> 'ItemStack':
        """
        Constructs a new itemstack with this item type that has the amount 1.

        @return: the constructed item stack.
        """
        pass

        def createItemStack(self, amount: int) -> 'ItemStack':
        """
        Constructs a new itemstack with this item type.

        @param amount: the amount of the item stack.
        @return: the constructed item stack.
        """
        pass

    def hasBlockType(self) -> bool:
        """
        Returns true if this ItemType has a corresponding {@link BlockType}.

        @return: true if there is a corresponding BlockType, otherwise false
        """
        pass

        def getBlockType(self) -> BlockType:
        """
        Returns the corresponding {@link BlockType} for the given ItemType.

        @return: the corresponding BlockType
        """
        pass

        def getItemMetaClass(self) -> type[ItemMeta]:
        """
        Gets the ItemMeta class of this ItemType

        @return: the ItemMeta class of this ItemType
        """
        pass

    def getMaxStackSize(self) -> int:
        """
        Gets the maximum amount of this item type that can be held in a stack

        @return: Maximum stack size for this item type
        """
        pass

    def getMaxDurability(self) -> short:
        """
        Gets the maximum durability of this item type

        @return: Maximum durability for this item type
        """
        pass

    def isEdible(self) -> bool:
        """
        Checks if this item type is edible.

        @return: true if this item type is edible.
        """
        pass

    def isRecord(self) -> bool:
        """
        @return: True if this item type represents a playable music disk.
        """
        pass

    def isFuel(self) -> bool:
        """
        Checks if this item type can be used as fuel in a Furnace

        @return: true if this item type can be used as fuel.
        """
        pass

    def isCompostable(self) -> bool:
        """
        Checks whether this item type is compostable (can be inserted into a composter).

        @return: true if this item type is compostable
        """
        pass

    def getCompostChance(self) -> float:
        """
        Get the chance that this item type will successfully compost. The
        returned value is between 0 and 1 (inclusive).

        @return: the chance that this item type will successfully compost
        """
        pass

        def getCraftingRemainingItem(self) -> Optional['ItemType']:
        """
        Determines the remaining item in a crafting grid after crafting with this ingredient.

        @return: the item left behind when crafting, or null if nothing is.
        """
        pass

        def getDefaultAttributeModifiers(self, slot: 'EquipmentSlot') -> Dict[Attribute, AttributeModifier]:
        """
        Return an immutable copy of all default {@link Attribute}s and their
        {@link AttributeModifier}s for a given {@link EquipmentSlot}.

        @param slot: the {@link EquipmentSlot} to check
        @return: the immutable {@link Multimap} with the respective default
        Attributes and modifiers, or an empty map if no attributes are set.
        """
        pass

    def isEnabledByFeature(self, world: World) -> bool:
        """
        Gets if the ItemType is enabled by the features in a world.

        @param world: the world to check
        @return: true if this ItemType can be used in this World.
        """
        pass

        def getKey(self) -> NamespacedKey:
        """
        {@inheritDoc}

        @return: the key
        """
        pass

        def asMaterial(self) -> Optional[Material]:
        """
        Tries to convert this ItemType into a Material

        @return: the converted Material or null
        """
        pass

class Typed(ItemType):
    """
    Typed represents a subtype of {@link ItemType}s that have a known item meta type
    at compile time.

    @param <M> the generic type of the item meta that represents the item type.
    """

        def getItemMetaClass(self) -> type[M]:
        """
        Gets the ItemMeta class of this ItemType

        @return: the ItemMeta class of this ItemType
        """
        pass

        def createItemStack(self, metaConfigurator: Optional[Callable[[M], None]] = None) -> 'ItemStack':
        """
        Constructs a new item stack with this item type with the amount 1.

        @param metaConfigurator: an optional consumer of the items {@link ItemMeta} that is called.
        @return: the created and configured item stack.
        """
        pass

        def createItemStack(self, amount: int, metaConfigurator: Optional[Callable[[M], None]] = None) -> 'ItemStack':
        """
        Constructs a new item stack with this item type.

        @param amount: the amount of itemstack.
        @param metaConfigurator: an optional consumer of the items {@link ItemMeta} that is called.
        @return: the created and configured item stack.
        """
        pass
from typing import List, Optional, Type
from org.bukkit import Bukkit
from org.bukkit import Keyed
from org.bukkit import NamespacedKey
from org.bukkit import RegistryAware
from org.bukkit.potion import PotionEffect
from org.bukkit.potion import PotionEffectType
from com.google.common.base import Preconditions
from com.google.common.base import Suppliers
from org.jetbrains.annotations import ApiStatus
from org.jetbrains.annotations import NotNull
from org.jetbrains.annotations import Nullable

"""
This enum reflects and matches each potion state that can be obtained from
the Creative mode inventory
"""
class PotionType(Keyed, RegistryAware):
    WATER: 'PotionType'
    MUNDANE: 'PotionType'
    THICK: 'PotionType'
    AWKWARD: 'PotionType'
    NIGHT_VISION: 'PotionType'
    LONG_NIGHT_VISION: 'PotionType'
    INVISIBILITY: 'PotionType'
    LONG_INVISIBILITY: 'PotionType'
    LEAPING: 'PotionType'
    LONG_LEAPING: 'PotionType'
    STRONG_LEAPING: 'PotionType'
    FIRE_RESISTANCE: 'PotionType'
    LONG_FIRE_RESISTANCE: 'PotionType'
    SWIFTNESS: 'PotionType'
    LONG_SWIFTNESS: 'PotionType'
    STRONG_SWIFTNESS: 'PotionType'
    SLOWNESS: 'PotionType'
    LONG_SLOWNESS: 'PotionType'
    STRONG_SLOWNESS: 'PotionType'
    WATER_BREATHING: 'PotionType'
    LONG_WATER_BREATHING: 'PotionType'
    HEALING: 'PotionType'
    STRONG_HEALING: 'PotionType'
    HARMING: 'PotionType'
    STRONG_HARMING: 'PotionType'
    POISON: 'PotionType'
    LONG_POISON: 'PotionType'
    STRONG_POISON: 'PotionType'
    REGENERATION: 'PotionType'
    LONG_REGENERATION: 'PotionType'
    STRONG_REGENERATION: 'PotionType'
    STRENGTH: 'PotionType'
    LONG_STRENGTH: 'PotionType'
    STRONG_STRENGTH: 'PotionType'
    WEAKNESS: 'PotionType'
    LONG_WEAKNESS: 'PotionType'
    LUCK: 'PotionType'
    TURTLE_MASTER: 'PotionType'
    LONG_TURTLE_MASTER: 'PotionType'
    STRONG_TURTLE_MASTER: 'PotionType'
    SLOW_FALLING: 'PotionType'
    LONG_SLOW_FALLING: 'PotionType'
    WIND_CHARGED: 'PotionType'
    WEAVING: 'PotionType'
    OOZING: 'PotionType'
    INFESTED: 'PotionType'

    def __init__(self, key: str) -> None:
        self.key: NamespacedKey
        self.internalPotionDataSupplier: Type['InternalPotionData']

    """
    @return the potion effect type of this potion type
    @deprecated Potions can have multiple effects use {@link #getPotionEffects()}
    """
        def getEffectType(self) -> Optional[PotionEffectType]:
        pass

    """
    @return a list of all effects this potion type has
    """
        def getPotionEffects(self) -> List[PotionEffect]:
        pass

    """
    @return if this potion type is instant
    @deprecated PotionType can have multiple effects, some of which can be instant and others not.
    Use {@link PotionEffectType#isInstant()} in combination with {@link #getPotionEffects()} and {@link PotionEffect#getType()}
    """
    @Deprecated(since="1.20.2")
    def isInstant(self) -> bool:
        pass

    """
    Checks if the potion type has an upgraded state.
    This refers to whether or not the potion type can be Tier 2,
    such as Potion of Fire Resistance II.

    @return true if the potion type can be upgraded;
    """
    def isUpgradeable(self) -> bool:
        pass

    """
    Checks if the potion type has an extended state.
    This refers to the extended duration potions

    @return true if the potion type can be extended
    """
    def isExtendable(self) -> bool:
        pass

    def getMaxLevel(self) -> int:
        pass

        def getKeyOrThrow(self) -> NamespacedKey:
        pass

        def getKeyOrNull(self) -> Optional[NamespacedKey]:
        pass

    def isRegistered(self) -> bool:
        pass

    """
    @param effectType the effect to get by
    @return the matching potion type
    @deprecated Misleading
    """
    @Deprecated(since="1.9")
        @staticmethod
    def getByEffect(effectType: Optional[PotionEffectType]) -> Optional['PotionType']:
        pass

    """
    {@inheritDoc}

    @see #getKeyOrThrow()
    @see #isRegistered()
    @deprecated A key might not always be present, use {@link #getKeyOrThrow()} instead.
    """
        @Deprecated(since="1.21.4")
    def getKey(self) -> NamespacedKey:
        pass

    """
    @deprecated Do not use, interface will get removed, and the plugin won't run
    """
    @Deprecated(since="1.20.2")
        class InternalPotionData:
        def getEffectType(self) -> PotionEffectType:
            pass

        def getPotionEffects(self) -> List[PotionEffect]:
            pass

        def isInstant(self) -> bool:
            pass

        def isUpgradeable(self) -> bool:
            pass

        def isExtendable(self) -> bool:
            pass

        def getMaxLevel(self) -> int:
            pass
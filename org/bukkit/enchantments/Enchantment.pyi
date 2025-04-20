from typing import Optional, List

from org.bukkit import Keyed, NamespacedKey, Registry, Translatable
from org.bukkit.inventory import ItemStack


class Enchantment(Keyed, Translatable):
    """
    The various type of enchantments that may be added to armour or weapons
    """

    PROTECTION: 'Enchantment'
    FIRE_PROTECTION: 'Enchantment'
    FEATHER_FALLING: 'Enchantment'
    BLAST_PROTECTION: 'Enchantment'
    PROJECTILE_PROTECTION: 'Enchantment'
    RESPIRATION: 'Enchantment'
    AQUA_AFFINITY: 'Enchantment'
    THORNS: 'Enchantment'
    DEPTH_STRIDER: 'Enchantment'
    FROST_WALKER: 'Enchantment'
    BINDING_CURSE: 'Enchantment'
    SHARPNESS: 'Enchantment'
    SMITE: 'Enchantment'
    BANE_OF_ARTHROPODS: 'Enchantment'
    KNOCKBACK: 'Enchantment'
    FIRE_ASPECT: 'Enchantment'
    LOOTING: 'Enchantment'
    SWEEPING_EDGE: 'Enchantment'
    EFFICIENCY: 'Enchantment'
    SILK_TOUCH: 'Enchantment'
    UNBREAKING: 'Enchantment'
    FORTUNE: 'Enchantment'
    POWER: 'Enchantment'
    PUNCH: 'Enchantment'
    FLAME: 'Enchantment'
    INFINITY: 'Enchantment'
    LUCK_OF_THE_SEA: 'Enchantment'
    LURE: 'Enchantment'
    LOYALTY: 'Enchantment'
    IMPALING: 'Enchantment'
    RIPTIDE: 'Enchantment'
    CHANNELING: 'Enchantment'
    MULTISHOT: 'Enchantment'
    QUICK_CHARGE: 'Enchantment'
    PIERCING: 'Enchantment'
    DENSITY: 'Enchantment'
    BREACH: 'Enchantment'
    WIND_BURST: 'Enchantment'
    MENDING: 'Enchantment'
    VANISHING_CURSE: 'Enchantment'
    SOUL_SPEED: 'Enchantment'
    SWIFT_SNEAK: 'Enchantment'

    @staticmethod
    def get_enchantment(key: str) -> 'Enchantment':
        """
        Retrieves an enchantment by its key.
        """
        return Registry.ENCHANTMENT.getOrThrow(NamespacedKey.minecraft(key))

    def get_name(self) -> str:
        """
        Gets the unique name of this enchantment.

        :return: Unique name
        :deprecated: enchantments are badly named, use get_key() instead.
        """
        ...

    def get_max_level(self) -> int:
        """
        Gets the maximum level that this Enchantment may become.

        :return: Maximum level of the Enchantment
        """
        ...

    def get_start_level(self) -> int:
        """
        Gets the level that this Enchantment should start at.

        :return: Starting level of the Enchantment
        """
        ...

    def get_item_target(self) -> 'EnchantmentTarget':
        """
        Gets the type of ItemStack that may fit this Enchantment.

        :return: Target type of the Enchantment
        :deprecated: enchantment groupings are now managed by tags, not categories
        """
        ...

    def is_treasure(self) -> bool:
        """
        Checks if this enchantment is a treasure enchantment.

        :return: true if the enchantment is a treasure enchantment
        :deprecated: enchantment types are now managed by tags
        """
        ...

    def is_cursed(self) -> bool:
        """
        Checks if this enchantment is a cursed enchantment.

        :return: true if the enchantment is cursed
        :deprecated: cursed enchantments are no longer special. Will return true
        only for Enchantment.BINDING_CURSE and Enchantment.VANISHING_CURSE.
        """
        ...

    def conflicts_with(self, other: 'Enchantment') -> bool:
        """
        Check if this enchantment conflicts with another enchantment.

        :param other: The enchantment to check against
        :return: True if there is a conflict.
        """
        ...

    def can_enchant_item(self, item: ItemStack) -> bool:
        """
        Checks if this Enchantment may be applied to the given ItemStack.

        :param item: Item to test
        :return: True if the enchantment may be applied, otherwise False
        """
        ...

    def get_key(self) -> NamespacedKey:
        """
        Gets the key of this enchantment.

        :return: The key of this enchantment
        :deprecated: A key might not always be present, use get_key_or_throw() instead.
        """
        ...

    @staticmethod
    def get_by_key(key: Optional[NamespacedKey]) -> Optional['Enchantment']:
        """
        Gets the Enchantment at the specified key.

        :param key: key to fetch
        :return: Resulting Enchantment, or None if not found
        :deprecated: only for backwards compatibility, use Registry.get(NamespacedKey) instead
        """
        ...

    @staticmethod
    def get_by_name(name: Optional[str]) -> Optional['Enchantment']:
        """
        Gets the Enchantment at the specified name.

        :param name: Name to fetch
        :return: Resulting Enchantment, or None if not found
        :deprecated: enchantments are badly named, use get_by_key(org.bukkit.NamespacedKey) instead.
        """
        ...

    @staticmethod
    def values() -> List['Enchantment']:
        """
        Gets an array of all the registered Enchantment.

        :return: Array of enchantments
        :deprecated: use Registry.ENCHANTMENT.iterator() instead
        """
        ...
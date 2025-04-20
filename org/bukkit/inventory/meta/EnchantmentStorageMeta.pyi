from typing import Dict
from org.bukkit.Material import Material
from org.bukkit.enchantments.Enchantment import Enchantment
from org.jetbrains.annotations import NotNull

"""
EnchantmentMeta is specific to items that can <i>store</i> enchantments, as
opposed to being enchanted. {@link Material#ENCHANTED_BOOK} is an example
of an item with enchantment storage.
"""
class EnchantmentStorageMeta(ItemMeta):

    """
    Checks for the existence of any stored enchantments.

    @return true if an enchantment exists on this meta
    """
    def has_stored_enchants(self) -> bool: ...

    """
    Checks for storage of the specified enchantment.

    @param ench enchantment to check
    @return true if this enchantment is stored in this meta
    """
    def has_stored_enchant(self, ench: NotNull[Enchantment]) -> bool: ...

    """
    Checks for the level of the stored enchantment.

    @param ench enchantment to check
    @return The level that the specified stored enchantment has, or 0 if
        none
    """
    def get_stored_enchant_level(self, ench: NotNull[Enchantment]) -> int: ...

    """
    Gets a copy the stored enchantments in this ItemMeta.

    @return An immutable copy of the stored enchantments
    """
    def get_stored_enchants(self) -> NotNull[Dict[Enchantment, int]]: ...

    """
    Stores the specified enchantment in this item meta.

    @param ench Enchantment to store
    @param level Level for the enchantment
    @param ignoreLevelRestriction this indicates the enchantment should be
        applied, ignoring the level limit
    @return true if the item meta changed as a result of this call, false
        otherwise
    @throws IllegalArgumentException if enchantment is null
    """
    def add_stored_enchant(self, ench: NotNull[Enchantment], level: int, ignore_level_restriction: bool) -> bool: ...

    """
    Remove the specified stored enchantment from this item meta.

    @param ench Enchantment to remove
    @return true if the item meta changed as a result of this call, false
        otherwise
    @throws IllegalArgumentException if enchantment is null
    """
    def remove_stored_enchant(self, ench: NotNull[Enchantment]) -> bool: ...

    """
    Checks if the specified enchantment conflicts with any enchantments in
    this ItemMeta.

    @param ench enchantment to test
    @return true if the enchantment conflicts, false otherwise
    """
    def has_conflicting_stored_enchant(self, ench: NotNull[Enchantment]) -> bool: ...

    @Override
        def clone(self) -> EnchantmentStorageMeta: ...
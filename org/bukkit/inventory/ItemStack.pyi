from typing import Dict, Optional, Union
from org.bukkit import Bukkit, Material, NamespacedKey, Registry, Translatable
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.bukkit.enchantments import Enchantment
from org.bukkit.inventory.meta import Damageable, ItemMeta
from org.bukkit.material import MaterialData
from com.google.common.base import Preconditions
from com.google.common.collect import ImmutableMap

"""
Represents a stack of items.
<p>
<b>IMPORTANT: An <i>Item</i>Stack is only designed to contain <i>items</i>. Do not
use this class to encapsulate Materials for which {@link Material#isItem()}
returns false.</b>
"""
class ItemStack(Cloneable, ConfigurationSerializable, Translatable):
    type: Material
    amount: int
    data: Optional[MaterialData]
    meta: Optional[ItemMeta]

    def __init__(self) -> None:
        """Defaults stack size to 1, with no extra data."""
        ...

    def __init__(self, type: Material) -> None:
        """Defaults stack size to 1, with no extra data.
        
        <p>
        <b>IMPORTANT: An <i>Item</i>Stack is only designed to contain
        <i>items</i>. Do not use this class to encapsulate Materials for which
        {@link Material#isItem()} returns false.</b>
        
        @param type item material
        """
        ...

    def __init__(self, type: Material, amount: int) -> None:
        """An item stack with no extra data.
        
        <p>
        <b>IMPORTANT: An <i>Item</i>Stack is only designed to contain
        <i>items</i>. Do not use this class to encapsulate Materials for which
        {@link Material#isItem()} returns false.</b>
        
        @param type item material
        @param amount stack size
        """
        ...

    def __init__(self, type: Material, amount: int, damage: int) -> None:
        """An item stack with the specified damage / durability
        
        @param type item material
        @param amount stack size
        @param damage durability / damage
        @deprecated see {@link #setDurability(short)}
        """
        ...

    def __init__(self, type: Material, amount: int, damage: int, data: Optional[bytes]) -> None:
        """@param type the type
        @param amount the amount in the stack
        @param damage the damage value of the item
        @param data the data value or null
        @deprecated this method uses an ambiguous data byte object
        """
        ...

    def __init__(self, stack: 'ItemStack') -> None:
        """Creates a new item stack derived from the specified stack
        
        @param stack the stack to copy
        @throws IllegalArgumentException if the specified stack is null or
            returns an item meta not created by the item factory
        """
        ...

    def getType(self) -> Material:
        """Gets the type of this item
        
        @return Type of the items in this stack
        """
        ...

    def setType(self, type: Material) -> None:
        """Sets the type of this item
        
        <p>
        Note that in doing so you will reset the MaterialData for this stack.
        <p>
        <b>IMPORTANT: An <i>Item</i>Stack is only designed to contain
        <i>items</i>. Do not use this class to encapsulate Materials for which
        {@link Material#isItem()} returns false.</b>
        
        @param type New type to set the items in this stack to
        """
        ...

    def getAmount(self) -> int:
        """Gets the amount of items in this stack
        
        @return Amount of items in this stack
        """
        ...

    def setAmount(self, amount: int) -> None:
        """Sets the amount of items in this stack
        
        @param amount New amount of items in this stack
        """
        ...

    def getData(self) -> Optional[MaterialData]:
        """Gets the MaterialData for this stack of items
        
        @return MaterialData for this item
        """
        ...

    def setData(self, data: Optional[MaterialData]) -> None:
        """Sets the MaterialData for this stack of items
        
        @param data New MaterialData for this item
        """
        ...

    def setDurability(self, durability: int) -> None:
        """Sets the durability of this item
        
        @param durability Durability of this item
        @deprecated durability is now part of ItemMeta. To avoid confusion and
        misuse, {@link #getItemMeta()}, {@link #setItemMeta(ItemMeta)} and
        {@link Damageable#setDamage(int)} should be used instead. This is because
        any call to this method will be overwritten by subsequent setting of
        ItemMeta which was created before this call.
        """
        ...

    def getDurability(self) -> int:
        """Gets the durability of this item
        
        @return Durability of this item
        @deprecated see {@link #setDurability(short)}
        """
        ...

    def getMaxStackSize(self) -> int:
        """Get the maximum stack size for this item. If this item has a max stack
        size component ({@link ItemMeta#hasMaxStackSize()}), the value of that
        component will be returned. Otherwise, this item's Material's {@link
        Material#getMaxStackSize() default maximum stack size} will be returned
        instead.
        
        @return The maximum you can stack this item to.
        """
        ...

    def createData(self, data: bytes) -> None:
        """Creates data for the item stack."""
        ...

    def __str__(self) -> str:
        """Overrides the default string representation."""
        ...

    def __eq__(self, obj: object) -> bool:
        """Overrides the default equality check."""
        ...

    def isSimilar(self, stack: Optional['ItemStack']) -> bool:
        """This method is the same as equals, but does not consider stack size
        (amount).
        
        @param stack the item stack to compare to
        @return true if the two stacks are equal, ignoring the amount
        """
        ...

    def clone(self) -> 'ItemStack':
        """Clones this ItemStack."""
        ...

    def __hash__(self) -> int:
        """Overrides the default hash function."""
        ...

    def containsEnchantment(self, ench: Enchantment) -> bool:
        """Checks if this ItemStack contains the given {@link Enchantment}
        
        @param ench Enchantment to test
        @return True if this has the given enchantment
        """
        ...

    def getEnchantmentLevel(self, ench: Enchantment) -> int:
        """Gets the level of the specified enchantment on this item stack
        
        @param ench Enchantment to check
        @return Level of the enchantment, or 0
        """
        ...

    def getEnchantments(self) -> Dict[Enchantment, int]:
        """Gets a map containing all enchantments and their levels on this item.
        
        @return Map of enchantments.
        """
        ...

    def addEnchantments(self, enchantments: Dict[Enchantment, int]) -> None:
        """Adds the specified enchantments to this item stack.
        
        <p>
        This method is the same as calling {@link
        #addEnchantment(org.bukkit.enchantments.Enchantment, int)} for each
        element of the map.
        
        @param enchantments Enchantments to add
        @throws IllegalArgumentException if the specified enchantments is null
        @throws IllegalArgumentException if any specific enchantment or level
            is null. <b>Warning</b>: Some enchantments may be added before this
            exception is thrown.
        """
        ...

    def addEnchantment(self, ench: Enchantment, level: int) -> None:
        """Adds the specified {@link Enchantment} to this item stack.
        
        <p>
        If this item stack already contained the given enchantment (at any
        level), it will be replaced.
        
        @param ench Enchantment to add
        @param level Level of the enchantment
        @throws IllegalArgumentException if enchantment null, or enchantment is
            not applicable
        """
        ...

    def addUnsafeEnchantments(self, enchantments: Dict[Enchantment, int]) -> None:
        """Adds the specified enchantments to this item stack in an unsafe manner.
        
        <p>
        This method is the same as calling {@link
        #addUnsafeEnchantment(org.bukkit.enchantments.Enchantment, int)} for
        each element of the map.
        
        @param enchantments Enchantments to add
        """
        ...

    def addUnsafeEnchantment(self, ench: Enchantment, level: int) -> None:
        """Adds the specified {@link Enchantment} to this item stack.
        
        <p>
        If this item stack already contained the given enchantment (at any
        level), it will be replaced.
        <p>
        This method is unsafe and will ignore level restrictions or item type.
        Use at your own discretion.
        
        @param ench Enchantment to add
        @param level Level of the enchantment
        """
        ...

    def removeEnchantment(self, ench: Enchantment) -> int:
        """Removes the specified {@link Enchantment} if it exists on this
        ItemStack
        
        @param ench Enchantment to remove
        @return Previous level, or 0
        """
        ...

    def removeEnchantments(self) -> None:
        """Removes all enchantments on this ItemStack."""
        ...

    def serialize(self) -> Dict[str, Union[int, str, ItemMeta]]:
        """Required method for configuration serialization
        
        @return serialized item stack
        """
        ...

    @staticmethod
    def deserialize(args: Dict[str, Union[int, str]]) -> 'ItemStack':
        """Required method for configuration serialization
        
        @param args map to deserialize
        @return deserialized item stack
        @see ConfigurationSerializable
        """
        ...

    def getItemMeta(self) -> Optional[ItemMeta]:
        """Get a copy of this ItemStack's {@link ItemMeta}.
        
        @return a copy of the current ItemStack's ItemData
        """
        ...

    def hasItemMeta(self) -> bool:
        """Checks to see if any meta data has been defined.
        
        @return Returns true if some meta data has been set for this item
        """
        ...

    def setItemMeta(self, itemMeta: Optional[ItemMeta]) -> bool:
        """Set the ItemMeta of this ItemStack.
        
        @param itemMeta new ItemMeta, or null to indicate meta data be cleared.
        @return True if successfully applied ItemMeta, see {@link
            ItemFactory#isApplicable(ItemMeta, ItemStack)}
        @throws IllegalArgumentException if the item meta was not created by
            the {@link ItemFactory}
        """
        ...

    def setItemMeta0(self, itemMeta: Optional[ItemMeta], material: Material) -> bool:
        """Cannot be overridden, so it's safe for constructor call"""
        ...

    def getTranslationKey(self) -> str:
        """@return translation key"""
        ...
from org.bukkit.Color import Color
from org.bukkit.Material import Material
from org.bukkit.Server import Server
from org.bukkit.World import World
from org.bukkit.enchantments.Enchantment import Enchantment
from org.bukkit.entity.Entity import Entity
from org.bukkit.entity.EntityType import EntityType
from org.bukkit.inventory.meta.BookMeta import BookMeta
from org.bukkit.inventory.meta.ItemMeta import ItemMeta
from org.bukkit.inventory.meta.SkullMeta import SkullMeta
from typing import Optional

class ItemFactory:
    """
    An instance of the ItemFactory can be obtained with {@link
    Server#getItemFactory()}.
    <p>
    The ItemFactory is solely responsible for creating item meta containers to
    apply on item stacks.
    """

    def get_item_meta(self, material: Material) -> Optional[ItemMeta]:
        """
        This creates a new item meta for the material.

        @param material The material to consider as base for the meta
        @return a new ItemMeta that could be applied to an item stack of the
            specified material
        """
        pass

    def is_applicable(self, meta: Optional[ItemMeta], stack: Optional[ItemStack]) -> bool:
        """
        This method checks the item meta to confirm that it is applicable (no
        data lost if applied) to the specified ItemStack.
        <p>
        A {@link SkullMeta} would not be valid for a sword, but a normal {@link
        ItemMeta} from an enchanted dirt block would.

        @param meta Meta to check
        @param stack Item that meta will be applied to
        @return true if the meta can be applied without losing data, false
            otherwise
        @throws IllegalArgumentException if the meta was not created by this
            factory
        """
        pass

    def is_applicable(self, meta: Optional[ItemMeta], material: Optional[Material]) -> bool:
        """
        This method checks the item meta to confirm that it is applicable (no
        data lost if applied) to the specified Material.
        <p>
        A {@link SkullMeta} would not be valid for a sword, but a normal {@link
        ItemMeta} from an enchanted dirt block would.

        @param meta Meta to check
        @param material Material that meta will be applied to
        @return true if the meta can be applied without losing data, false
            otherwise
        @throws IllegalArgumentException if the meta was not created by this
            factory
        """
        pass

    def equals(self, meta1: Optional[ItemMeta], meta2: Optional[ItemMeta]) -> bool:
        """
        This method is used to compare two item meta data objects.

        @param meta1 First meta to compare, and may be null to indicate no data
        @param meta2 Second meta to compare, and may be null to indicate no
            data
        @return false if one of the meta has data the other does not, otherwise
            true
        @throws IllegalArgumentException if either meta was not created by this
            factory
        """
        pass

    def as_meta_for(self, meta: ItemMeta, stack: ItemStack) -> Optional[ItemMeta]:
        """
        Returns an appropriate item meta for the specified stack.
        <p>
        The item meta returned will always be a valid meta for a given
        ItemStack of the specified material. It may be a more or less specific
        meta, and could also be the same meta or meta type as the parameter.
        The item meta returned will also always be the most appropriate meta.
        <p>
        Example, if a {@link SkullMeta} is being applied to a book, this method
        would return a {@link BookMeta} containing all information in the
        specified meta that is applicable to an {@link ItemMeta}, the highest
        common interface.

        @param meta the meta to convert
        @param stack the stack to convert the meta for
        @return An appropriate item meta for the specified item stack. No
            guarantees are made as to if a copy is returned. This will be null
            for a stack of air.
        @throws IllegalArgumentException if the specified meta was not created
            by this factory
        """
        pass

    def as_meta_for(self, meta: ItemMeta, material: Material) -> Optional[ItemMeta]:
        """
        Returns an appropriate item meta for the specified material.
        <p>
        The item meta returned will always be a valid meta for a given
        ItemStack of the specified material. It may be a more or less specific
        meta, and could also be the same meta or meta type as the parameter.
        The item meta returned will also always be the most appropriate meta.
        <p>
        Example, if a {@link SkullMeta} is being applied to a book, this method
        would return a {@link BookMeta} containing all information in the
        specified meta that is applicable to an {@link ItemMeta}, the highest
        common interface.

        @param meta the meta to convert
        @param material the material to convert the meta for
        @return An appropriate item meta for the specified item material. No
            guarantees are made as to if a copy is returned. This will be null for air.
        @throws IllegalArgumentException if the specified meta was not created
            by this factory
        """
        pass

    def get_default_leather_color(self) -> Color:
        """
        Returns the default color for all leather armor.

        @return the default color for leather armor
        """
        pass

    def create_item_stack(self, input: str) -> ItemStack:
        """
        Create a new {@link ItemStack} given the supplied input.
        <p>
        The input should match the same input as expected by Minecraft's {@code /give}
        command. For example,
        <pre>"minecraft:diamond_sword[minecraft:enchantments={levels:{"minecraft:sharpness": 3}}]"</pre>
        would yield an ItemStack of {@link Material#DIAMOND_SWORD} with an {@link ItemMeta}
        containing a level 3 {@link Enchantment#SHARPNESS} enchantment.

        @param input the item input string
        @return the created ItemStack
        @throws IllegalArgumentException if the input string was provided in an
            invalid or unsupported format
        """
        pass

    def get_spawn_egg(self, type: EntityType) -> Optional[Material]:
        """
        Gets a {@link Material} representing the spawn egg for the provided
        {@link EntityType}. <br>
        Will return null for EntityTypes that do not have a corresponding spawn egg.

        @param type the entity type
        @return the Material of this EntityTypes spawn egg or null
        """
        pass

    def enchant_item(self, entity: Entity, item: ItemStack, level: int, allow_treasures: bool) -> ItemStack:
        """
        Enchants the given item at the provided level.
        <br>
        If an item that is air is passed through an error is thrown.

        @param entity the entity to use as a source of randomness
        @param item the item to enchant
        @param level the level to use, which is the level in the enchantment table
        @param allow_treasures allows treasure enchants, e.g. mending, if true.
        @return a new ItemStack containing the result of the Enchantment
        """
        pass

    def enchant_item(self, world: World, item: ItemStack, level: int, allow_treasures: bool) -> ItemStack:
        """
        Enchants the given item at the provided level.
        <br>
        If an item that is air is passed through an error is thrown.

        @param world the world to use as a source of randomness
        @param item the item to enchant
        @param level the level to use, which is the level in the enchantment table
        @param allow_treasures allow the treasure enchants, e.g. mending, if true.
        @return a new ItemStack containing the result of the Enchantment
        """
        pass

    def enchant_item(self, item: ItemStack, level: int, allow_treasures: bool) -> ItemStack:
        """
        Enchants the given item at the provided level.
        <br>
        If an item that is air is passed through an error is thrown.

        @param item the item to enchant
        @param level the level to use, which is the level in the enchantment table
        @param allow_treasures allow treasure enchantments, e.g. mending, if true.
        @return a new ItemStack containing the result of the Enchantment
        """
        pass
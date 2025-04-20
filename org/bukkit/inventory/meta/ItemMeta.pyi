from collections.abc import Collection
from typing import List, Map, Set, Optional, Dict
from org.bukkit.NamespacedKey import NamespacedKey
from org.bukkit.Sound import Sound
from org.bukkit.Tag import Tag
from org.bukkit.attribute.Attribute import Attribute
from org.bukkit.attribute.AttributeModifier import AttributeModifier
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.bukkit.damage.DamageType import DamageType
from org.bukkit.enchantments.Enchantment import Enchantment
from org.bukkit.inventory.EquipmentSlot import EquipmentSlot
from org.bukkit.inventory.ItemFactory import ItemFactory
from org.bukkit.inventory.ItemFlag import ItemFlag
from org.bukkit.inventory.ItemRarity import ItemRarity
from org.bukkit.inventory.ItemStack import ItemStack
from org.bukkit.inventory.meta.components.BlocksAttacksComponent import BlocksAttacksComponent
from org.bukkit.inventory.meta.components.CustomModelDataComponent import CustomModelDataComponent
from org.bukkit.inventory.meta.components.EquippableComponent import EquippableComponent
from org.bukkit.inventory.meta.components.FoodComponent import FoodComponent
from org.bukkit.inventory.meta.components.JukeboxPlayableComponent import JukeboxPlayableComponent
from org.bukkit.inventory.meta.components.ToolComponent import ToolComponent
from org.bukkit.inventory.meta.components.UseCooldownComponent import UseCooldownComponent
from org.bukkit.inventory.meta.components.WeaponComponent import WeaponComponent
from org.bukkit.inventory.meta.components.consumable.ConsumableComponent import ConsumableComponent
from org.bukkit.inventory.meta.tags.CustomItemTagContainer import CustomItemTagContainer
from org.bukkit.persistence.PersistentDataHolder import PersistentDataHolder
from org.bukkit.tag.DamageTypeTags import DamageTypeTags
from org.jetbrains.annotations import ApiStatus, NotNull, Nullable


class ItemMeta(ConfigurationSerializable, PersistentDataHolder):
    """
    This type represents the storage mechanism for auxiliary item data.
    <p>
    An implementation will handle the creation and application for ItemMeta.
    This class should not be implemented by a plugin in a live environment.
    """

    def has_display_name(self) -> bool:
        """Checks for existence of a display name."""
        ...

        def get_display_name(self) -> str:
        """Gets the display name that is set."""
        ...

    def set_display_name(self, name: Optional[str]) -> None:
        """Sets the display name."""
        ...

    def has_item_name(self) -> bool:
        """Checks for existence of an item name."""
        ...

        def get_item_name(self) -> str:
        """Gets the item name that is set."""
        ...

    def set_item_name(self, name: Optional[str]) -> None:
        """Sets the item name."""
        ...

    def has_localized_name(self) -> bool:
        """Checks for existence of a localized name."""
        ...

        def get_localized_name(self) -> str:
        """Gets the localized display name that is set."""
        ...

    def set_localized_name(self, name: Optional[str]) -> None:
        """Sets the localized name."""
        ...

    def has_lore(self) -> bool:
        """Checks for existence of lore."""
        ...

        def get_lore(self) -> List[str]:
        """Gets the lore that is set."""
        ...

    def set_lore(self, lore: Optional[List[str]]) -> None:
        """Sets the lore for this item."""
        ...

    def has_custom_model_data(self) -> bool:
        """Checks for existence of custom model data."""
        ...

    def get_custom_model_data(self) -> int:
        """Gets the custom model data that is set."""
        ...

        def get_custom_model_data_component(self) -> CustomModelDataComponent:
        """Gets the custom model data set on this item, or creates an empty custom model data instance."""
        ...

    def set_custom_model_data(self, data: Optional[int]) -> None:
        """Sets the custom model data."""
        ...

    def has_custom_model_data_component(self) -> bool:
        """Checks if the custom model data component is set."""
        ...

    def set_custom_model_data_component(self, custom_model_data: Optional[CustomModelDataComponent]) -> None:
        """Sets the custom model data component."""
        ...

    def has_enchantable(self) -> bool:
        """Gets if the enchantable component is set."""
        ...

    def get_enchantable(self) -> int:
        """Gets the enchantable component."""
        ...

    def set_enchantable(self, enchantable: Optional[int]) -> None:
        """Sets the enchantable."""
        ...

    def has_enchants(self) -> bool:
        """Checks for the existence of any enchantments."""
        ...

    def has_enchant(self, ench: Enchantment) -> bool:
        """Checks for existence of the specified enchantment."""
        ...

    def get_enchant_level(self, ench: Enchantment) -> int:
        """Checks for the level of the specified enchantment."""
        ...

        def get_enchants(self) -> Map[Enchantment, int]:
        """Returns a copy of the enchantments in this ItemMeta."""
        ...

    def add_enchant(self, ench: Enchantment, level: int, ignore_level_restriction: bool) -> bool:
        """Adds the specified enchantment to this item meta."""
        ...

    def remove_enchant(self, ench: Enchantment) -> bool:
        """Removes the specified enchantment from this item meta."""
        ...

    def remove_enchantments(self) -> None:
        """Removes all enchantments from this item meta."""
        ...

    def has_conflicting_enchant(self, ench: Enchantment) -> bool:
        """Checks if the specified enchantment conflicts with any enchantments in this ItemMeta."""
        ...

    def add_item_flags(self, *item_flags: ItemFlag) -> None:
        """Set itemflags which should be ignored when rendering a ItemStack in the Client."""
        ...

    def remove_item_flags(self, *item_flags: ItemFlag) -> None:
        """Remove specific set of itemFlags."""
        ...

        def get_item_flags(self) -> Set[ItemFlag]:
        """Get current set itemFlags."""
        ...

    def has_item_flag(self, flag: ItemFlag) -> bool:
        """Check if the specified flag is present on this item."""
        ...

    def is_hide_tooltip(self) -> bool:
        """Gets if this item has hide_tooltip set."""
        ...

    def set_hide_tooltip(self, hide_tooltip: bool) -> None:
        """Sets if this item has hide_tooltip set."""
        ...

    def has_tooltip_style(self) -> bool:
        """Gets if this item has a custom tooltip style."""
        ...

        def get_tooltip_style(self) -> NamespacedKey:
        """Gets the custom tooltip style."""
        ...

    def set_tooltip_style(self, tooltip_style: Optional[NamespacedKey]) -> None:
        """Sets the custom tooltip style."""
        ...

    def has_item_model(self) -> bool:
        """Gets if this item has a custom item model."""
        ...

        def get_item_model(self) -> NamespacedKey:
        """Gets the custom item model."""
        ...

    def set_item_model(self, item_model: Optional[NamespacedKey]) -> None:
        """Sets the custom item model."""
        ...

    def is_unbreakable(self) -> bool:
        """Return if the unbreakable tag is true."""
        ...

    def set_unbreakable(self, unbreakable: bool) -> None:
        """Sets the unbreakable tag."""
        ...

    def has_enchantment_glint_override(self) -> bool:
        """Gets if an enchantment_glint_override is set."""
        ...

        def get_enchantment_glint_override(self) -> bool:
        """Gets the enchantment_glint_override."""
        ...

    def set_enchantment_glint_override(self, override: Optional[bool]) -> None:
        """Sets the enchantment_glint_override."""
        ...

    def is_glider(self) -> bool:
        """Checks if this item is a glider."""
        ...

    def set_glider(self, glider: bool) -> None:
        """Sets if this item is a glider."""
        ...

    def is_fire_resistant(self) -> bool:
        """Checks if this item is fire_resistant."""
        ...

    def set_fire_resistant(self, fire_resistant: bool) -> None:
        """Sets if this item is fire_resistant."""
        ...

    def has_damage_resistant(self) -> bool:
        """Gets if this item is resistant to certain types of damage."""
        ...

        def get_damage_resistant(self) -> Tag[DamageType]:
        """Gets the type of damage this item will be resistant to when in entity form."""
        ...

    def set_damage_resistant(self, tag: Optional[Tag[DamageType]]) -> None:
        """Sets the type of damage this item will be resistant to when in entity form."""
        ...

    def has_max_stack_size(self) -> bool:
        """Gets if the max_stack_size is set."""
        ...

    def get_max_stack_size(self) -> int:
        """Gets the max_stack_size."""
        ...

    def set_max_stack_size(self, max: Optional[int]) -> None:
        """Sets the max_stack_size."""
        ...

    def has_rarity(self) -> bool:
        """Gets if the rarity is set."""
        ...

        def get_rarity(self) -> ItemRarity:
        """Gets the item rarity."""
        ...

    def set_rarity(self, rarity: Optional[ItemRarity]) -> None:
        """Sets the item rarity."""
        ...

    def has_use_remainder(self) -> bool:
        """Checks if the use remainder is set."""
        ...

        def get_use_remainder(self) -> ItemStack:
        """Gets the item which this item will convert to when used."""
        ...

    def set_use_remainder(self, remainder: Optional[ItemStack]) -> None:
        """Sets the item which this item will convert to when used."""
        ...

    def has_use_cooldown(self) -> bool:
        """Checks if the use cooldown is set."""
        ...

        def get_use_cooldown(self) -> UseCooldownComponent:
        """Gets the use cooldown set on this item, or creates an empty cooldown instance."""
        ...

    def set_use_cooldown(self, cooldown: Optional[UseCooldownComponent]) -> None:
        """Sets the item use cooldown."""
        ...

    def has_food(self) -> bool:
        """Checks if the food is set."""
        ...

        def get_food(self) -> FoodComponent:
        """Gets the food set on this item, or creates an empty food instance."""
        ...

    def set_food(self, food: Optional[FoodComponent]) -> None:
        """Sets the item food."""
        ...

    def has_consumable(self) -> bool:
        """Checks if the consumable is set."""
        ...

        def get_consumable(self) -> ConsumableComponent:
        """Gets the consumable set on this item, or creates an empty consumable instance."""
        ...

    def set_consumable(self, consumable: Optional[ConsumableComponent]) -> None:
        """Sets the item consumable."""
        ...

    def has_tool(self) -> bool:
        """Checks if the tool is set."""
        ...

        def get_tool(self) -> ToolComponent:
        """Gets the tool set on this item, or creates an empty tool instance."""
        ...

    def set_tool(self, tool: Optional[ToolComponent]) -> None:
        """Sets the item tool."""
        ...

    def has_weapon(self) -> bool:
        """Checks if the weapon is set."""
        ...

        def get_weapon(self) -> WeaponComponent:
        """Gets the weapon set on this item, or creates an empty weapon instance."""
        ...

    def set_weapon(self, weapon: Optional[WeaponComponent]) -> None:
        """Sets the item weapon."""
        ...

    def has_blocks_attacks(self) -> bool:
        """Checks if the BlocksAttacksComponent is set."""
        ...

        def get_blocks_attacks(self) -> BlocksAttacksComponent:
        """Gets the BlocksAttacksComponent set on this item, or creates an empty BlocksAttacksComponent instance."""
        ...

    def set_blocks_attacks(self, blocks_attacks: Optional[BlocksAttacksComponent]) -> None:
        """Sets the item BlocksAttacksComponent."""
        ...

    def has_equippable(self) -> bool:
        """Checks if the equippable is set."""
        ...

        def get_equippable(self) -> EquippableComponent:
        """Gets the equippable set on this item, or creates an empty equippable instance."""
        ...

    def set_equippable(self, equippable: Optional[EquippableComponent]) -> None:
        """Sets the equippable tool."""
        ...

    def has_jukebox_playable(self) -> bool:
        """Checks if the jukebox playable is set."""
        ...

        def get_jukebox_playable(self) -> JukeboxPlayableComponent:
        """Gets the jukebox playable component set on this item."""
        ...

    def set_jukebox_playable(self, jukebox_playable: Optional[JukeboxPlayableComponent]) -> None:
        """Sets the item jukebox playable."""
        ...

    def has_break_sound(self) -> bool:
        """Gets if the break sound is set."""
        ...

        def get_break_sound(self) -> Sound:
        """Gets the sound to play when the item is broken."""
        ...

    def set_break_sound(self, sound: Optional[Sound]) -> None:
        """Sets the sound to play when the item is broken."""
        ...

    def has_attribute_modifiers(self) -> bool:
        """Checks for the existence of any AttributeModifiers."""
        ...

        def get_attribute_modifiers(self) -> Multimap[Attribute, AttributeModifier]:
        """Return an immutable copy of all Attributes and their modifiers in this ItemMeta."""
        ...

        def get_attribute_modifiers(self, slot: EquipmentSlot) -> Multimap[Attribute, AttributeModifier]:
        """Return an immutable copy of all Attributes and their modifiers for a given EquipmentSlot."""
        ...

        def get_attribute_modifiers(self, attribute: Attribute) -> Collection[AttributeModifier]:
        """Return an immutable collection of AttributeModifiers for a given Attribute."""
        ...

    def add_attribute_modifier(self, attribute: Attribute, modifier: AttributeModifier) -> bool:
        """Add an Attribute and its Modifier."""
        ...

    def set_attribute_modifiers(self, attribute_modifiers: Optional[Multimap[Attribute, AttributeModifier]]) -> None:
        """Set all Attributes and their AttributeModifiers."""
        ...

    def remove_attribute_modifier(self, attribute: Attribute) -> bool:
        """Remove all AttributeModifiers associated with the given Attribute."""
        ...

    def remove_attribute_modifier(self, slot: EquipmentSlot) -> bool:
        """Remove all Attributes and AttributeModifiers for a given EquipmentSlot."""
        ...

    def remove_attribute_modifier(self, attribute: Attribute, modifier: AttributeModifier) -> bool:
        """Remove a specific Attribute and AttributeModifier."""
        ...

        def get_as_string(self) -> str:
        """Get this ItemMeta as an NBT string."""
        ...

        def get_as_component_string(self) -> str:
        """Get this ItemMeta as a component-compliant string."""
        ...

        @Deprecated(since="1.14")
    def get_custom_tag_container(self) -> CustomItemTagContainer:
        """Return a public custom tag container capable of storing tags on the item."""
        ...

        def set_version(self, version: int) -> None:
        """Internal use only! Do not use under any circumstances!"""
        ...

        def clone(self) -> ItemMeta:
        """Create a clone of this ItemMeta."""
        ...
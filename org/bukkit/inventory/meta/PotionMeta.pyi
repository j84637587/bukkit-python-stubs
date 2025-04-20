from typing import List, Optional
from org.bukkit.Color import Color
from org.bukkit.potion.PotionData import PotionData
from org.bukkit.potion.PotionEffect import PotionEffect
from org.bukkit.potion.PotionEffectType import PotionEffectType
from org.bukkit.potion.PotionType import PotionType
from org.bukkit.inventory.meta.ItemMeta import ItemMeta

"""
Represents a potion or item that can have custom effects.
"""
class PotionMeta(ItemMeta):

    """
    Sets the underlying potion data

    @param data PotionData to set the base potion state to
    @deprecated Upgraded / extended potions are now their own {@link PotionType} use {@link #setBasePotionType} instead.
    """
    def set_base_potion_data(self, data: Optional[PotionData]) -> None: ...

    """
    Returns the potion data about the base potion

    @return a PotionData object
    @deprecated Upgraded / extended potions are now their own {@link PotionType} use {@link #getBasePotionType()} instead.
    """
    def get_base_potion_data(self) -> Optional[PotionData]: ...

    """
    Sets the underlying potion type

    @param type PotionType to set the base potion state to
    """
    def set_base_potion_type(self, type: Optional[PotionType]) -> None: ...

    """
    Returns the potion type about the base potion

    @return a PotionType object
    """
    def get_base_potion_type(self) -> Optional[PotionType]: ...

    """
    Checks for the presence of a base potion type

    @return true if a base potion type is present
    """
    def has_base_potion_type(self) -> bool: ...

    """
    Checks for the presence of custom potion effects.

    @return true if custom potion effects are applied
    """
    def has_custom_effects(self) -> bool: ...

    """
    Gets an immutable list containing all custom potion effects applied to
    this potion.
    <p>
    Plugins should check that hasCustomEffects() returns true before calling
    this method.

    @return the immutable list of custom potion effects
    """
    def get_custom_effects(self) -> List[PotionEffect]: ...

    """
    Adds a custom potion effect to this potion.

    @param effect the potion effect to add
    @param overwrite true if any existing effect of the same type should be
    overwritten
    @return true if the potion meta changed as a result of this call
    """
    def add_custom_effect(self, effect: PotionEffect, overwrite: bool) -> bool: ...

    """
    Removes a custom potion effect from this potion.

    @param type the potion effect type to remove
    @return true if the potion meta changed as a result of this call
    """
    def remove_custom_effect(self, type: PotionEffectType) -> bool: ...

    """
    Checks for a specific custom potion effect type on this potion.

    @param type the potion effect type to check for
    @return true if the potion has this effect
    """
    def has_custom_effect(self, type: PotionEffectType) -> bool: ...

    """
    Moves a potion effect to the top of the potion effect list.
    <p>
    This causes the client to display the potion effect in the potion's name.

    @param type the potion effect type to move
    @return true if the potion meta changed as a result of this call
    @deprecated use {@link #setBasePotionType(org.bukkit.potion.PotionType)}
    """
    def set_main_effect(self, type: PotionEffectType) -> bool: ...

    """
    Removes all custom potion effects from this potion.

    @return true if the potion meta changed as a result of this call
    """
    def clear_custom_effects(self) -> bool: ...

    """
    Checks for existence of a potion color.

    @return true if this has a custom potion color
    """
    def has_color(self) -> bool: ...

    """
    Gets the potion color that is set. A custom potion color will alter the
    display of the potion in an inventory slot.
    <p>
    Plugins should check that hasColor() returns <code>true</code> before
    calling this method.

    @return the potion color that is set
    """
    def get_color(self) -> Optional[Color]: ...

    """
    Sets the potion color. A custom potion color will alter the display of
    the potion in an inventory slot.

    @param color the color to set
    """
    def set_color(self, color: Optional[Color]) -> None: ...

    """
    Checks for existence of a custom potion name translation suffix.

    @return true if this has a custom potion name
    """
    def has_custom_name(self) -> bool: ...

    """
    Gets the potion name translation suffix that is set.
    <p>
    Plugins should check that hasCustomName() returns <code>true</code>
    before calling this method.

    @return the potion name that is set
    """
    def get_custom_name(self) -> Optional[str]: ...

    """
    Sets the potion name translation suffix.

    @param name the name to set
    """
    def set_custom_name(self, name: Optional[str]) -> None: ...

    """
    Checks for existence of a potion duration scale.

    @return true if this has a potion duration scale.
    """
    def has_duration_scale(self) -> bool: ...

    """
    Gets the potion duration scale that is set.
    <p>
    Plugins should check that hasDurationScale() returns <code>true</code>
    before calling this method.

    @return the scale factor applied to all potion effect durations
    """
    def get_duration_scale(self) -> Optional[float]: ...

    """
    Gets the potion duration scale.

    @param scale the scale factor applied to all potion effect durations
    """
    def set_duration_scale(self, scale: Optional[float]) -> None: ...

    def clone(self) -> 'PotionMeta': ...
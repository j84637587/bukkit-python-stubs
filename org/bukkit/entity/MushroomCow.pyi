from typing import List
from org.bukkit.potion import PotionEffect
from org.bukkit.potion import PotionEffectType
from org.jetbrains.annotations import NotNull

"""
Represents a mushroom {@link AbstractCow}
"""
class MushroomCow(AbstractCow):

    """
    Checks for the presence of custom potion effects to be applied to the
    next suspicious stew received from milking this {@link MushroomCow}.

    @return true if custom potion effects are applied to the stew
    """
    def has_effects_for_next_stew(self) -> bool: ...

    """
    Gets an immutable list containing all custom potion effects applied to
    the next suspicious stew received from milking this {@link MushroomCow}.
    <p>
    Plugins should check that has_custom_effects() returns true before calling
    this method.

    @return an immutable list of custom potion effects
    """
        def get_effects_for_next_stew(self) -> List[PotionEffect]: ...

    """
    Adds a custom potion effect to be applied to the next suspicious stew
    received from milking this {@link MushroomCow}.

    @param effect the potion effect to add
    @param overwrite true if any existing effect of the same type should be
    overwritten
    @return true if the effects to be applied to the suspicious stew changed
    as a result of this call
    """
    def add_effect_to_next_stew(self, effect: @NotNull PotionEffect, overwrite: bool) -> bool: ...

    """
    Removes a custom potion effect from being applied to the next suspicious
    stew received from milking this {@link MushroomCow}.

    @param type the potion effect type to remove
    @return true if the effects to be applied to the suspicious stew changed
    as a result of this call
    """
    def remove_effect_from_next_stew(self, type: @NotNull PotionEffectType) -> bool: ...

    """
    Checks for a specific custom potion effect type to be applied to the next
    suspicious stew received from milking this {@link MushroomCow}.

    @param type the potion effect type to check for
    @return true if the suspicious stew to be generated has this effect
    """
    def has_effect_for_next_stew(self, type: @NotNull PotionEffectType) -> bool: ...

    """
    Removes all custom potion effects to be applied to the next suspicious
    stew received from milking this {@link MushroomCow}.
    """
    def clear_effects_for_next_stew(self) -> None: ...

    """
    Get the variant of this cow.

    @return cow variant
    """
        def get_variant(self) -> 'Variant': ...

    """
    Set the variant of this cow.

    @param variant cow variant
    """
    def set_variant(self, variant: @NotNull 'Variant') -> None: ...

    """
    Represents the variant of a cow - ie its color.
    """
    class Variant:
        """
        Red mushroom cow.
        """
        RED = ...

        """
        Brown mushroom cow.
        """
        BROWN = ...
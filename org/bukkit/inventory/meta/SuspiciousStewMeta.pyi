from typing import List
from org.bukkit.potion import PotionEffect
from org.bukkit.potion import PotionEffectType
from org.bukkit.inventory.meta import ItemMeta
from typing import Protocol

class SuspiciousStewMeta(ItemMeta, Protocol):
    """
    Represents a suspicious stew that can have custom effects.
    """

    def has_custom_effects(self) -> bool:
        """
        Checks for the presence of custom potion effects.

        Returns:
            true if custom potion effects are applied
        """
        ...

    def get_custom_effects(self) -> List[PotionEffect]:
        """
        Gets an immutable list containing all custom potion effects applied to
        this suspicious stew.
        Plugins should check that has_custom_effects() returns true before calling
        this method.

        Returns:
            the immutable list of custom potion effects
        """
        ...

    def add_custom_effect(self, effect: PotionEffect, overwrite: bool) -> bool:
        """
        Adds a custom potion effect to this suspicious stew.

        Args:
            effect: the potion effect to add
            overwrite: true if any existing effect of the same type should be
            overwritten

        Returns:
            true if the suspicious stew meta changed as a result of this call
        """
        ...

    def remove_custom_effect(self, type: PotionEffectType) -> bool:
        """
        Removes a custom potion effect from this suspicious stew.

        Args:
            type: the potion effect type to remove

        Returns:
            true if the suspicious stew meta changed as a result of this call
        """
        ...

    def has_custom_effect(self, type: PotionEffectType) -> bool:
        """
        Checks for a specific custom potion effect type on this suspicious stew.

        Args:
            type: the potion effect type to check for

        Returns:
            true if the suspicious stew has this effect
        """
        ...

    def clear_custom_effects(self) -> bool:
        """
        Removes all custom potion effects from this suspicious stew.

        Returns:
            true if the suspicious stew meta changed as a result of this call
        """
        ...

    def clone(self) -> 'SuspiciousStewMeta':
        ...
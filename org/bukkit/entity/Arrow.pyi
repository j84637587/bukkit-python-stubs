from typing import List, Optional
from org.bukkit.Color import Color
from org.bukkit.potion.PotionData import PotionData
from org.bukkit.potion.PotionEffect import PotionEffect
from org.bukkit.potion.PotionEffectType import PotionEffectType
from org.bukkit.potion.PotionType import PotionType
from org.jetbrains.annotations import NotNull, Nullable

class Arrow(AbstractArrow):
    """
    Interface representing an Arrow entity.
    """

    @Deprecated(since="1.20.6")
    def set_base_potion_data(self, data: Optional[PotionData]) -> None:
        """
        Sets the underlying potion data.

        :param data: PotionData to set the base potion state to
        :deprecated: Upgraded / extended potions are now their own {@link PotionType} use {@link #setBasePotionType} instead.
        """
        ...

    @Deprecated(since="1.20.6")
        def get_base_potion_data(self) -> Optional[PotionData]:
        """
        Returns the potion data about the base potion.

        :return: a PotionData object
        :deprecated: Upgraded / extended potions are now their own {@link PotionType} use {@link #getBasePotionType()} instead.
        """
        ...

    def set_base_potion_type(self, type: Optional[PotionType]) -> None:
        """
        Sets the underlying potion type.

        :param type: PotionType to set the base potion state to
        """
        ...

        def get_base_potion_type(self) -> Optional[PotionType]:
        """
        Returns the potion type about the base potion.

        :return: a PotionType object
        """
        ...

        def get_color(self) -> Optional[Color]:
        """
        Gets the color of this arrow.

        :return: arrow {@link Color} or null if not color is set
        """
        ...

    def set_color(self, color: Optional[Color]) -> None:
        """
        Sets the color of this arrow. Will be applied as a tint to its particles.

        :param color: arrow color, null to clear the color
        """
        ...

    def has_custom_effects(self) -> bool:
        """
        Checks for the presence of custom potion effects.

        :return: true if custom potion effects are applied
        """
        ...

        def get_custom_effects(self) -> List[PotionEffect]:
        """
        Gets an immutable list containing all custom potion effects applied to this arrow.
        Plugins should check that hasCustomEffects() returns true before calling this method.

        :return: the immutable list of custom potion effects
        """
        ...

    def add_custom_effect(self, effect: PotionEffect, overwrite: bool) -> bool:
        """
        Adds a custom potion effect to this arrow.

        :param effect: the potion effect to add
        :param overwrite: true if any existing effect of the same type should be overwritten
        :return: true if the effect was added as a result of this call
        """
        ...

    def remove_custom_effect(self, type: PotionEffectType) -> bool:
        """
        Removes a custom potion effect from this arrow.

        :param type: the potion effect type to remove
        :return: true if an effect was removed as a result of this call
        :raises IllegalArgumentException: if this operation would leave the Arrow in a state with no Custom Effects and PotionType.UNCRAFTABLE
        """
        ...

    def has_custom_effect(self, type: Optional[PotionEffectType]) -> bool:
        """
        Checks for a specific custom potion effect type on this arrow.

        :param type: the potion effect type to check for
        :return: true if the potion has this effect
        """
        ...

    def clear_custom_effects(self) -> None:
        """
        Removes all custom potion effects from this arrow.

        :raises IllegalArgumentException: if this operation would leave the Arrow in a state with no Custom Effects and PotionType.UNCRAFTABLE
        """
        ...
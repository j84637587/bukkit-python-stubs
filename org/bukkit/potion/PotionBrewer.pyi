from typing import Collection
from org.bukkit.potion import PotionEffect, PotionEffectType, PotionType

class PotionBrewer:
    """
    Represents a brewer that can create {@link PotionEffect}s.
    """

    def create_effect(self, potion: PotionEffectType, duration: int, amplifier: int) -> PotionEffect:
        """
        Creates a {@link PotionEffect} from the given {@link PotionEffectType},
        applying duration modifiers and checks.

        :param potion: The type of potion
        :param duration: The duration in ticks
        :param amplifier: The amplifier of the effect
        :return: The resulting potion effect
        """
        ...

    def get_effects_from_damage(self, damage: int) -> Collection[PotionEffect]:
        """
        Returns a collection of {@link PotionEffect} that would be applied from
        a potion with the given data value.

        :param damage: The data value of the potion
        :return: The list of effects
        :deprecated: Non-Functional
        """
        ...

    def get_effects(self, type: PotionType, upgraded: bool, extended: bool) -> Collection[PotionEffect]:
        """
        Returns a collection of {@link PotionEffect} that would be applied from
        a potion with the given type.

        :param type: The type of the potion
        :param upgraded: Whether the potion is upgraded
        :param extended: Whether the potion is extended
        :return: The list of effects
        :deprecated: Upgraded / extended potions are now their own {@link PotionType} use {@link PotionType#getPotionEffects()} instead
        """
        ...
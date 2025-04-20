from typing import List, Protocol
from org.bukkit import Bukkit, Keyed, NamespacedKey, Registry, Translatable, RegistryAware
from org.bukkit.util import OldEnum
from google.common.base import Preconditions
import locale

class Attribute(OldEnum['Attribute'], Keyed, Translatable, RegistryAware, Protocol):
    """
    Types of attributes which may be present on an {@link Attributable}.
    """

    MAX_HEALTH: 'Attribute'
    FOLLOW_RANGE: 'Attribute'
    KNOCKBACK_RESISTANCE: 'Attribute'
    MOVEMENT_SPEED: 'Attribute'
    FLYING_SPEED: 'Attribute'
    ATTACK_DAMAGE: 'Attribute'
    ATTACK_KNOCKBACK: 'Attribute'
    ATTACK_SPEED: 'Attribute'
    ARMOR: 'Attribute'
    ARMOR_TOUGHNESS: 'Attribute'
    FALL_DAMAGE_MULTIPLIER: 'Attribute'
    LUCK: 'Attribute'
    MAX_ABSORPTION: 'Attribute'
    SAFE_FALL_DISTANCE: 'Attribute'
    SCALE: 'Attribute'
    STEP_HEIGHT: 'Attribute'
    GRAVITY: 'Attribute'
    JUMP_STRENGTH: 'Attribute'
    BURNING_TIME: 'Attribute'
    EXPLOSION_KNOCKBACK_RESISTANCE: 'Attribute'
    MOVEMENT_EFFICIENCY: 'Attribute'
    OXYGEN_BONUS: 'Attribute'
    WATER_MOVEMENT_EFFICIENCY: 'Attribute'
    TEMPT_RANGE: 'Attribute'
    BLOCK_INTERACTION_RANGE: 'Attribute'
    ENTITY_INTERACTION_RANGE: 'Attribute'
    BLOCK_BREAK_SPEED: 'Attribute'
    MINING_EFFICIENCY: 'Attribute'
    SNEAKING_SPEED: 'Attribute'
    SUBMERGED_MINING_SPEED: 'Attribute'
    SWEEPING_DAMAGE_RATIO: 'Attribute'
    SPAWN_REINFORCEMENTS: 'Attribute'

    @staticmethod
    def get_attribute(key: str) -> 'Attribute':
        """
        Retrieves an attribute by its key.

        :param key: The key of the attribute.
        :return: The attribute associated with the given key.
        """
        return Registry.ATTRIBUTE.getOrThrow(NamespacedKey.minecraft(key))

    def get_key(self) -> NamespacedKey:
        """
        {@inheritDoc}

        @see #getKeyOrThrow()
        @see #isRegistered()
        @deprecated A key might not always be present, use {@link #getKeyOrThrow()} instead.
        """
        ...

    @staticmethod
    def value_of(name: str) -> 'Attribute':
        """
        @param name of the attribute.
        @return the attribute with the given name.
        @deprecated only for backwards compatibility, use {@link Registry#get(NamespacedKey)} instead.
        """
        ...

    @staticmethod
    def values() -> List['Attribute']:
        """
        @return an array of all known attributes.
        @deprecated use {@link Registry#iterator()}.
        """
        ...
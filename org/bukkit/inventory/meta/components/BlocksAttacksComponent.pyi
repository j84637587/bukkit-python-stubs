from typing import List, Collection, Optional
from org.bukkit import Sound
from org.bukkit import Tag
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.bukkit.damage import DamageType
from org.jetbrains.annotations import ApiStatus, NotNull, Nullable

"""
Represents a component which can turn any item into a shield-like item which
blocks attack damage.
"""
class BlocksAttacksComponent(ConfigurationSerializable):

    def get_block_delay_seconds(self) -> float:
        """
        Gets the delay on equip before this item will block attacks.

        @return: the delay in seconds
        """
        ...

    def set_block_delay_seconds(self, seconds: float) -> None:
        """
        Sets the delay on equip before this item will block attacks.

        @param seconds: the delay in seconds to set
        """
        ...

    def get_disable_cooldown_scale(self) -> float:
        """
        Gets the multiplier applied to the item cooldown when attacked by a
        disabling attack.

        @return: the scale
        """
        ...

    def set_disable_cooldown_scale(self, scale: float) -> None:
        """
        Sets the multiplier applied to the item cooldown when attacked by a
        disabling attack.

        @param scale: the scale to set. Must be 0 or a positive integer
        """
        ...

        def get_damage_reductions(self) -> List['DamageReduction']:
        """
        Get the list of {@link DamageReduction DamageReductions} that apply to
        this item.

        @return: all damage reductions. The mutability of the returned list cannot
        be guaranteed, but its contents are mutable and can have their values
        changed
        """
        ...

    def set_damage_reductions(self, reductions: List['DamageReduction']) -> None:
        """
        Set the list of {@link DamageReduction DamageReductions} to apply to this
        item. This will remove any existing damage reductions.

        @param reductions: the reductions to set
        """
        ...

        def add_damage_reduction(self, type: DamageType, base: float, factor: float, horizontal_blocking_angle: float) -> 'DamageReduction':
        """
        Add a new damage reduction to this component, which blocks specific types
        of attacks.

        @param type: the type of attack
        @param base: the constant amount of damage to be blocked
        @param factor: the proportion of damage to be blocked
        @param horizontal_blocking_angle: the maximum angle at which attacks will be
        blocked
        @return: the {@link DamageReduction} instance that was added to this item
        """
        ...

        def add_damage_reduction(self, types: Collection[DamageType], base: float, factor: float, horizontal_blocking_angle: float) -> 'DamageReduction':
        """
        Add a new damage reduction to this component, which blocks specific types
        of attacks.

        @param types: the types of attack
        @param base: the constant amount of damage to be blocked
        @param factor: the proportion of damage to be blocked
        @param horizontal_blocking_angle: the maximum angle at which attacks will be
        blocked
        @return: the {@link DamageReduction} instance that was added to this item
        """
        ...

        def add_damage_reduction(self, tag: Tag[DamageType], base: float, factor: float, horizontal_blocking_angle: float) -> 'DamageReduction':
        """
        Add a new damage reduction to this component, which blocks specific types
        of attacks.

        @param tag: the type of attacks
        @param base: the constant amount of damage to be blocked
        @param factor: the proportion of damage to be blocked
        @param horizontal_blocking_angle: the maximum angle at which attacks will be
        blocked
        @return: the {@link DamageReduction} instance that was added to this item
        """
        ...

    def remove_damage_reduction(self, reduction: 'DamageReduction') -> bool:
        """
        Remove the given {@link DamageReduction} from this item.

        @param reduction: the reduction to remove
        @return: true if the reduction was removed, false if this component did
        not contain a matching reduction
        """
        ...

    def get_item_damage_threshold(self) -> float:
        """
        Gets the amount of damage required to be dealt before damage is also
        applied to the item.

        @return: threshold damage amount
        """
        ...

    def set_item_damage_threshold(self, threshold: float) -> None:
        """
        Sets the amount of damage required to be dealt before damage is also
        applied to the item.

        @param threshold: new threshold damage amount
        """
        ...

    def get_item_damage_base(self) -> float:
        """
        Gets the constant amount of damage applied to the item if the threshold
        is reached.

        @return: base item damage
        """
        ...

    def set_item_damage_base(self, base: float) -> None:
        """
        Sets the constant amount of damage applied to the item if the threshold
        is reached.

        @param base: new base item damage
        """
        ...

    def get_item_damage_factor(self) -> float:
        """
        Gets the proportion of damage applied to the item if the threshold is
        reached.

        @return: item damage factor
        """
        ...

    def set_item_damage_factor(self, factor: float) -> None:
        """
        Sets the proportion of damage applied to the item if the threshold is
        reached.

        @param factor: new item damage factor
        """
        ...

        def get_block_sound(self) -> Optional[Sound]:
        """
        Gets the sound to play when the item blocks an attack.

        @return: the sound
        """
        ...

    def set_block_sound(self, sound: Optional[Sound]) -> None:
        """
        Sets the sound to play when the item blocks an attack.

        @param sound: sound or null for current default
        """
        ...

        def get_disable_sound(self) -> Optional[Sound]:
        """
        Gets the sound to play when the item is disabled.

        @return: the sound
        """
        ...

    def set_disable_sound(self, sound: Optional[Sound]) -> None:
        """
        Sets the sound to play when the item is disabled.

        @param sound: sound or null for current default
        """
        ...

        def get_bypassed_by(self) -> Optional[Tag[DamageType]]:
        """
        Gets the type of damage that will bypass blocking by this item.

        @return: damage type
        """
        ...

    def set_bypassed_by(self, tag: Optional[Tag[DamageType]]) -> None:
        """
        Sets the type of damage that will bypass blocking by this item.

        @param tag: the tag, or null to clear
        """
        ...


class DamageReduction(ConfigurationSerializable):

        def get_types(self) -> Optional[Collection[DamageType]]:
        """
        Gets the types to which this reduction applies.

        @return: the damage types
        """
        ...

    def set_types(self, type: Optional[DamageType]) -> None:
        """
        Sets the types to which this reduction applies.

        @param type: the damage types
        """
        ...

    def set_types(self, types: Optional[Collection[DamageType]]) -> None:
        """
        Sets the types to which this reduction applies.

        @param types: the damage types
        """
        ...

    def set_types(self, tag: Optional[Tag[DamageType]]) -> None:
        """
        Sets the types to which this reduction applies.

        @param tag: the damage tag
        """
        ...

    def get_base(self) -> float:
        """
        Gets the constant amount of damage to be blocked.

        @return: base block amount
        """
        ...

    def set_base(self, base: float) -> None:
        """
        Sets the constant amount of damage to be blocked.

        @param base: new base amount
        """
        ...

    def get_factor(self) -> float:
        """
        Gets the proportion of damage to be blocked.

        @return: base blocking factor
        """
        ...

    def set_factor(self, factor: float) -> None:
        """
        Sets the proportion of damage to be blocked.

        @param factor: new blocking factor
        """
        ...

    def get_horizontal_blocking_angle(self) -> float:
        """
        Gets the maximum angle at which attacks will be blocked (defaults to
        90).

        @return: maximum blocking angle
        """
        ...

    def set_horizontal_blocking_angle(self, horizontal_blocking_angle: float) -> None:
        """
        Sets the maximum angle at which attacks will be blocked (defaults to
        90).

        @param horizontal_blocking_angle: new blocking angle
        """
        ...
from typing import Collection, List, Set, TypeVar, Generic, Optional
from org.bukkit import FluidCollisionMode, Location, Material, Sound, World
from org.bukkit.attribute import Attributable
from org.bukkit.block import Block
from org.bukkit.entity.memory import MemoryKey
from org.bukkit.inventory import EntityEquipment, ItemStack
from org.bukkit.potion import PotionEffect, PotionEffectType
from org.bukkit.projectiles import ProjectileSource
from org.bukkit.scoreboard import Scoreboard, Team
from org.bukkit.util import RayTraceResult, Vector
from org.jetbrains.annotations import NotNull, Nullable

T = TypeVar('T')

class LivingEntity(Attributable, ProjectileSource):
    """
    Represents a living entity, such as a monster or player
    """

    def get_eye_height(self) -> float:
        """
        Gets the height of the living entity's eyes above its Location.

        @return height of the living entity's eyes above its location
        """
        ...

    def get_eye_height_ignore_pose(self, ignore_pose: bool) -> float:
        """
        Gets the height of the living entity's eyes above its Location.

        @param ignorePose if set to true, the effects of pose changes, eg
            sneaking and gliding will be ignored
        @return height of the living entity's eyes above its location
        """
        ...

        def get_eye_location(self) -> Location:
        """
        Get a Location detailing the current eye position of the living entity.

        @return a location at the eyes of the living entity
        """
        ...

        def get_line_of_sight(self, transparent: Optional[Set[Material]], max_distance: int) -> List[Block]:
        """
        Gets all blocks along the living entity's line of sight.

        @param transparent Set containing all transparent block Materials (set to
            null for only air)
        @param maxDistance this is the maximum distance to scan (may be limited
            by server by at least 100 blocks, no less)
        @return list containing all blocks along the living entity's line of
            sight
        """
        ...

        def get_target_block(self, transparent: Optional[Set[Material]], max_distance: int) -> Block:
        """
        Gets the block that the living entity has targeted.

        @param transparent Set containing all transparent block Materials (set to
            null for only air)
        @param maxDistance this is the maximum distance to scan (may be limited
            by server by at least 100 blocks, no less)
        @return block that the living entity has targeted
        """
        ...

        def get_last_two_target_blocks(self, transparent: Optional[Set[Material]], max_distance: int) -> List[Block]:
        """
        Gets the last two blocks along the living entity's line of sight.

        @param transparent Set containing all transparent block Materials (set to
            null for only air)
        @param maxDistance this is the maximum distance to scan. This may be
            further limited by the server, but never to less than 100 blocks
        @return list containing the last 2 blocks along the living entity's
            line of sight
        """
        ...

        def get_target_block_exact(self, max_distance: int) -> Block:
        """
        Gets the block that the living entity has targeted.

        @param maxDistance the maximum distance to scan
        @return block that the living entity has targeted
        """
        ...

        def get_target_block_exact_with_mode(self, max_distance: int, fluid_collision_mode: NotNull FluidCollisionMode) -> Block:
        """
        Gets the block that the living entity has targeted.

        @param maxDistance the maximum distance to scan
        @param fluidCollisionMode the fluid collision mode
        @return block that the living entity has targeted
        """
        ...

        def ray_trace_blocks(self, max_distance: float) -> RayTraceResult:
        """
        Performs a ray trace that provides information on the targeted block.

        @param maxDistance the maximum distance to scan
        @return information on the targeted block, or <code>null</code> if there
            is no targeted block in range
        """
        ...

        def ray_trace_blocks_with_mode(self, max_distance: float, fluid_collision_mode: NotNull FluidCollisionMode) -> RayTraceResult:
        """
        Performs a ray trace that provides information on the targeted block.

        @param maxDistance the maximum distance to scan
        @param fluidCollisionMode the fluid collision mode
        @return information on the targeted block, or <code>null</code> if there
            is no targeted block in range
        """
        ...

    def get_remaining_air(self) -> int:
        """
        Returns the amount of air that the living entity has remaining, in
        ticks.

        @return amount of air remaining
        """
        ...

    def set_remaining_air(self, ticks: int) -> None:
        """
        Sets the amount of air that the living entity has remaining, in ticks.

        @param ticks amount of air remaining
        """
        ...

    def get_maximum_air(self) -> int:
        """
        Returns the maximum amount of air the living entity can have, in ticks.

        @return maximum amount of air
        """
        ...

    def set_maximum_air(self, ticks: int) -> None:
        """
        Sets the maximum amount of air the living entity can have, in ticks.

        @param ticks maximum amount of air
        """
        ...

        def get_item_in_use(self) -> ItemStack:
        """
        Gets the item that the player is using (eating food, drawing back a bow,
        blocking, etc.)

        @return the item being used by the player, or null if they are not using
        an item
        """
        ...

    def get_item_in_use_ticks(self) -> int:
        """
        Gets the number of ticks remaining for the current item's usage.

        @return The number of ticks remaining
        """
        ...

    def set_item_in_use_ticks(self, ticks: int) -> None:
        """
        Sets the number of ticks that remain for the current item's usage.
        Applies to items that take time to use, like eating food, drawing a bow,
        or throwing a trident.

        @param ticks The number of ticks remaining
        """
        ...

    def get_arrow_cooldown(self) -> int:
        """
        Gets the time in ticks until the next arrow leaves the entity's body.

        @return ticks until arrow leaves
        """
        ...

    def set_arrow_cooldown(self, ticks: int) -> None:
        """
        Sets the time in ticks until the next arrow leaves the entity's body.

        @param ticks time until arrow leaves
        """
        ...

    def get_arrows_in_body(self) -> int:
        """
        Gets the amount of arrows in an entity's body.

        @return amount of arrows in body
        """
        ...

    def set_arrows_in_body(self, count: int) -> None:
        """
        Set the amount of arrows in the entity's body.

        @param count amount of arrows in entity's body
        """
        ...

    def get_maximum_no_damage_ticks(self) -> int:
        """
        Returns the living entity's current maximum no damage ticks.

        @return maximum no damage ticks
        """
        ...

    def set_maximum_no_damage_ticks(self, ticks: int) -> None:
        """
        Sets the living entity's current maximum no damage ticks.

        @param ticks maximum amount of no damage ticks
        """
        ...

    def get_last_damage(self) -> float:
        """
        Returns the living entity's last damage taken in the current no damage
        ticks time.

        @return damage taken since the last no damage ticks time period
        """
        ...

    def set_last_damage(self, damage: float) -> None:
        """
        Sets the damage dealt within the current no damage ticks time period.

        @param damage amount of damage
        """
        ...

    def get_no_damage_ticks(self) -> int:
        """
        Returns the living entity's current no damage ticks.

        @return amount of no damage ticks
        """
        ...

    def set_no_damage_ticks(self, ticks: int) -> None:
        """
        Sets the living entity's current no damage ticks.

        @param ticks amount of no damage ticks
        """
        ...

    def get_no_action_ticks(self) -> int:
        """
        Get the ticks that this entity has performed no action.

        @return amount of no action ticks
        """
        ...

    def set_no_action_ticks(self, ticks: int) -> None:
        """
        Set the ticks that this entity has performed no action.

        @param ticks amount of no action ticks
        """
        ...

        def get_killer(self) -> 'Player':
        """
        Gets the player identified as the killer of the living entity.

        @return killer player, or null if none found
        """
        ...

    def add_potion_effect(self, effect: NotNull PotionEffect) -> bool:
        """
        Adds the given {@link PotionEffect} to the living entity.

        @param effect PotionEffect to be added
        @return whether the effect could be added
        """
        ...

    def add_potion_effect_with_force(self, effect: NotNull PotionEffect, force: bool) -> bool:
        """
        Adds the given {@link PotionEffect} to the living entity.

        @param effect PotionEffect to be added
        @param force whether conflicting effects should be removed
        @return whether the effect could be added
        @deprecated no need to force since multiple effects of the same type are
        now supported.
        """
        ...

    def add_potion_effects(self, effects: NotNull Collection[PotionEffect]) -> bool:
        """
        Attempts to add all of the given {@link PotionEffect} to the living
        entity.

        @param effects the effects to add
        @return whether all of the effects could be added
        """
        ...

    def has_potion_effect(self, type: NotNull PotionEffectType) -> bool:
        """
        Returns whether the living entity already has an existing effect of
        the given {@link PotionEffectType} applied to it.

        @param type the potion type to check
        @return whether the living entity has this potion effect active on them
        """
        ...

        def get_potion_effect(self, type: NotNull PotionEffectType) -> Optional[PotionEffect]:
        """
        Returns the active {@link PotionEffect} of the specified type.

        @param type the potion type to check
        @return the effect active on this entity, or null if not active.
        """
        ...

    def remove_potion_effect(self, type: NotNull PotionEffectType) -> None:
        """
        Removes any effects present of the given {@link PotionEffectType}.

        @param type the potion type to remove
        """
        ...

        def get_active_potion_effects(self) -> Collection[PotionEffect]:
        """
        Returns all currently active {@link PotionEffect}s on the living
        entity.

        @return a collection of {@link PotionEffect}s
        """
        ...

    def has_line_of_sight(self, other: NotNull 'Entity') -> bool:
        """
        Checks whether the living entity has block line of sight to another.

        @param other the entity to determine line of sight to
        @return true if there is a line of sight, false if not
        """
        ...

    def get_remove_when_far_away(self) -> bool:
        """
        Returns if the living entity despawns when away from players or not.

        @return true if the living entity is removed when away from players
        """
        ...

    def set_remove_when_far_away(self, remove: bool) -> None:
        """
        Sets whether or not the living entity despawns when away from players
        or not.

        @param remove the removal status
        """
        ...

        def get_equipment(self) -> EntityEquipment:
        """
        Gets the inventory with the equipment worn by the living entity.

        @return the living entity's inventory
        """
        ...

    def set_can_pickup_items(self, pickup: bool) -> None:
        """
        Sets whether or not the living entity can pick up items.

        @param pickup whether or not the living entity can pick up items
        """
        ...

    def get_can_pickup_items(self) -> bool:
        """
        Gets if the living entity can pick up items.

        @return whether or not the living entity can pick up items
        """
        ...

    def is_leashed(self) -> bool:
        """
        Returns whether the entity is currently leashed.

        @return whether the entity is leashed
        """
        ...

        def get_leash_holder(self) -> 'Entity':
        """
        Gets the entity that is currently leading this entity.

        @return the entity holding the leash
        @throws IllegalStateException if not currently leashed
        """
        ...

    def set_leash_holder(self, holder: Optional['Entity']) -> bool:
        """
        Sets the leash on this entity to be held by the supplied entity.

        @param holder the entity to leash this entity to, or null to unleash
        @return whether the operation was successful
        """
        ...

    def is_gliding(self) -> bool:
        """
        Checks to see if an entity is gliding, such as using an Elytra.

        @return True if this entity is gliding.
        """
        ...

    def set_gliding(self, gliding: bool) -> None:
        """
        Makes entity start or stop gliding.

        @param gliding True if the entity is gliding.
        """
        ...

    def is_swimming(self) -> bool:
        """
        Checks to see if an entity is swimming.

        @return True if this entity is swimming.
        """
        ...

    def set_swimming(self, swimming: bool) -> None:
        """
        Makes entity start or stop swimming.

        @param swimming True if the entity is swimming.
        """
        ...

    def is_riptiding(self) -> bool:
        """
        Checks to see if an entity is currently riptiding.

        @return True if this entity is currently riptiding.
        """
        ...

    def set_riptiding(self, riptiding: bool) -> None:
        """
        Makes entity start or stop riptiding.

        @param riptiding whether the entity should start riptiding.
        """
        ...

    def is_sleeping(self) -> bool:
        """
        Returns whether this entity is slumbering.

        @return slumber state
        """
        ...

    def is_climbing(self) -> bool:
        """
        Gets if the entity is climbing.

        @return if the entity is climbing
        """
        ...

    def set_ai(self, ai: bool) -> None:
        """
        Sets whether an entity will have AI.

        @param ai whether the mob will have AI or not.
        """
        ...

    def has_ai(self) -> bool:
        """
        Checks whether an entity has AI.

        @return true if the entity has AI, otherwise false.
        """
        ...

    def attack(self, target: NotNull 'Entity') -> None:
        """
        Makes this entity attack the given entity with a melee attack.

        @param target entity to attack.
        """
        ...

    def swing_main_hand(self) -> None:
        """
        Makes this entity swing their main hand.
        """
        ...

    def swing_off_hand(self) -> None:
        """
        Makes this entity swing their off hand.
        """
        ...

    def play_hurt_animation(self, yaw: float) -> None:
        """
        Makes this entity flash red as if they were damaged.

        @param yaw The direction the damage is coming from in relation to the
        entity, where 0 is in front of the player, 90 is to the right, 180 is
        behind, and 270 is to the left
        """
        ...

    def set_collidable(self, collidable: bool) -> None:
        """
        Set if this entity will be subject to collisions with other entities.

        @param collidable collision status
        """
        ...

    def is_collidable(self) -> bool:
        """
        Gets if this entity is subject to collisions with other entities.

        @return collision status
        """
        ...

        def get_collidable_exemptions(self) -> Set[UUID]:
        """
        Gets a mutable set of UUIDs of the entities which are exempt from the
        entity's collidable rule.

        @return the collidable exemption set
        """
        ...

        def get_memory(self, memory_key: NotNull MemoryKey[T]) -> Optional[T]:
        """
        Returns the value of the memory specified.

        @param memoryKey memory to access
        @param <T> the type of the return value
        @return a instance of the memory section value or null if not present
        """
        ...

    def set_memory(self, memory_key: NotNull MemoryKey[T], memory_value: Optional[T]) -> None:
        """
        Sets the value of the memory specified.

        @param memoryKey the memory to access
        @param memoryValue a typed memory value
        """
        ...

        def get_hurt_sound(self) -> Sound:
        """
        Get the {@link Sound} this entity will make when damaged.

        @return the hurt sound, or null if the entity does not make any sound
        """
        ...

        def get_death_sound(self) -> Sound:
        """
        Get the {@link Sound} this entity will make on death.

        @return the death sound, or null if the entity does not make any sound
        """
        ...

        def get_fall_damage_sound(self, fall_height: int) -> Sound:
        """
        Get the {@link Sound} this entity will make when falling from the given
        height (in blocks).

        @param fallHeight the fall height in blocks
        @return the fall damage sound
        """
        ...

        def get_fall_damage_sound_small(self) -> Sound:
        """
        Get the {@link Sound} this entity will make when falling from a small
        height.

        @return the fall damage sound
        """
        ...

        def get_fall_damage_sound_big(self) -> Sound:
        """
        Get the {@link Sound} this entity will make when falling from a large
        height.

        @return the fall damage sound
        """
        ...

        def get_drinking_sound(self, item_stack: NotNull ItemStack) -> Sound:
        """
        Get the {@link Sound} this entity will make when drinking the given
        {@link ItemStack}.

        @param itemStack the item stack being drank
        @return the drinking sound
        """
        ...

        def get_eating_sound(self, item_stack: NotNull ItemStack) -> Sound:
        """
        Get the {@link Sound} this entity will make when eating the given
        {@link ItemStack}.

        @param itemStack the item stack being eaten
        @return the eating sound
        """
        ...

    def can_breathe_underwater(self) -> bool:
        """
        Returns true if this entity can breathe underwater and will not take
        suffocation damage when its air supply reaches zero.

        @return <code>true</code> if the entity can breathe underwater
        """
        ...

        @Deprecated(since="1.20.5")
    def get_category(self) -> 'EntityCategory':
        """
        Get the category to which this entity belongs.

        @return the entity category
        """
        ...

    def set_invisible(self, invisible: bool) -> None:
        """
        Sets whether the entity is invisible or not.

        @param invisible If the entity is invisible
        """
        ...

    def is_invisible(self) -> bool:
        """
        Gets whether the entity is invisible or not.

        @return Whether the entity is invisible
        """
        ...
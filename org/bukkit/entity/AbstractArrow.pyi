from org.bukkit.block import Block
from org.bukkit.inventory import ItemStack
from org.jetbrains.annotations import ApiStatus, NotNull, Nullable
from typing import Literal

"""
Represents an arrow.
"""
class AbstractArrow(Projectile):

    """
    Gets the knockback strength for an arrow, which is the
    {@link org.bukkit.enchantments.Enchantment#KNOCKBACK KnockBack} level
    of the bow that shot it.

    @return the knockback strength value
    @see #getWeapon()
    @deprecated a function of the firing weapon
    """
    def get_knockback_strength(self) -> int: ...

    """
    Sets the knockback strength for an arrow.

    @param knockbackStrength the knockback strength value
    @see #setWeapon(org.bukkit.inventory.ItemStack)
    @deprecated a function of the firing weapon
    """
    def set_knockback_strength(self, knockback_strength: int) -> None: ...

    """
    Gets the base amount of damage this arrow will do.

    Defaults to 2.0 for a normal arrow with
    <code>0.5 * (1 + power level)</code> added for arrows fired from
    enchanted bows.

    @return base damage amount
    """
    def get_damage(self) -> float: ...

    """
    Sets the base amount of damage this arrow will do.

    @param damage new damage amount
    """
    def set_damage(self, damage: float) -> None: ...

    """
    Gets the number of times this arrow can pierce through an entity.

    @return pierce level
    """
    def get_pierce_level(self) -> int: ...

    """
    Sets the number of times this arrow can pierce through an entity.

    Must be between 0 and 127 times.

    @param pierceLevel new pierce level
    """
    def set_pierce_level(self, pierce_level: int) -> None: ...

    """
    Gets whether this arrow is critical.
    <p>
    Critical arrows have increased damage and cause particle effects.
    <p>
    Critical arrows generally occur when a player fully draws a bow before
    firing.

    @return true if it is critical
    """
    def is_critical(self) -> bool: ...

    """
    Sets whether or not this arrow should be critical.

    @param critical whether or not it should be critical
    """
    def set_critical(self, critical: bool) -> None: ...

    """
    Gets whether this arrow is in a block or not.
    <p>
    Arrows in a block are motionless and may be picked up by players.

    @return true if in a block
    """
    def is_in_block(self) -> bool: ...

    """
    Gets the block to which this arrow is attached.

    @return the attached block or null if not attached
    """
        def get_attached_block(self) -> Block: ...

    """
    Gets the current pickup status of this arrow.

    @return the pickup status of this arrow.
    """
        def get_pickup_status(self) -> 'PickupStatus': ...

    """
    Sets the current pickup status of this arrow.

    @param status new pickup status of this arrow.
    """
    def set_pickup_status(self, status: 'PickupStatus') -> None: ...

    """
    Gets if this arrow was shot from a crossbow.

    @return if shot from a crossbow
    """
    def is_shot_from_crossbow(self) -> bool: ...

    """
    Sets if this arrow was shot from a crossbow.

    @param shotFromCrossbow if shot from a crossbow
    @see #setWeapon(org.bukkit.inventory.ItemStack)
    @deprecated a function of the firing weapon instead
    """
    @Deprecated(since="1.21")
    def set_shot_from_crossbow(self, shot_from_crossbow: bool) -> None: ...

    """
    Gets the ItemStack which will be picked up from this arrow.

    @return The picked up ItemStack
    """
            def get_item(self) -> ItemStack: ...

    """
    Sets the ItemStack which will be picked up from this arrow.

    @param item ItemStack set to be picked up
    """
        def set_item(self, item: ItemStack) -> None: ...

    """
    Gets the ItemStack which fired this arrow.

    @return The firing ItemStack
    """
            def get_weapon(self) -> ItemStack: ...

    """
    Sets the ItemStack which fired this arrow.

    @param item The firing ItemStack
    """
        def set_weapon(self, item: ItemStack) -> None: ...

    """
    Represents the pickup status of this arrow.
    """
    class PickupStatus:
        """
        The arrow cannot be picked up.
        """
        DISALLOWED: Literal['DISALLOWED']
        """
        The arrow can be picked up.
        """
        ALLOWED: Literal['ALLOWED']
        """
        The arrow can only be picked up by players in creative mode.
        """
        CREATIVE_ONLY: Literal['CREATIVE_ONLY']
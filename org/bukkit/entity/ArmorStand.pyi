from org.bukkit.inventory import EntityEquipment
from org.bukkit.inventory import EquipmentSlot
from org.bukkit.inventory import ItemStack
from org.bukkit.util import EulerAngle
from typing import Optional, Literal

class ArmorStand(LivingEntity):
    """
    ArmorStand interface representing an armor stand entity in the game.
    """

    @Deprecated(since="1.15.2")
    def get_item_in_hand(self) -> ItemStack:
        """Returns the item the armor stand is currently holding."""
        ...

    @Deprecated(since="1.15.2")
    def set_item_in_hand(self, item: Optional[ItemStack]) -> None:
        """Sets the item the armor stand is currently holding."""
        ...

    @Deprecated(since="1.15.2")
    def get_boots(self) -> ItemStack:
        """Returns the item currently being worn by the armor stand on its feet."""
        ...

    @Deprecated(since="1.15.2")
    def set_boots(self, item: Optional[ItemStack]) -> None:
        """Sets the item currently being worn by the armor stand on its feet."""
        ...

    @Deprecated(since="1.15.2")
    def get_leggings(self) -> ItemStack:
        """Returns the item currently being worn by the armor stand on its legs."""
        ...

    @Deprecated(since="1.15.2")
    def set_leggings(self, item: Optional[ItemStack]) -> None:
        """Sets the item currently being worn by the armor stand on its legs."""
        ...

    @Deprecated(since="1.15.2")
    def get_chestplate(self) -> ItemStack:
        """Returns the item currently being worn by the armor stand on its chest."""
        ...

    @Deprecated(since="1.15.2")
    def set_chestplate(self, item: Optional[ItemStack]) -> None:
        """Sets the item currently being worn by the armor stand on its chest."""
        ...

    @Deprecated(since="1.15.2")
    def get_helmet(self) -> ItemStack:
        """Returns the item currently being worn by the armor stand on its head."""
        ...

    @Deprecated(since="1.15.2")
    def set_helmet(self, item: Optional[ItemStack]) -> None:
        """Sets the item currently being worn by the armor stand on its head."""
        ...

    def get_body_pose(self) -> EulerAngle:
        """Returns the armor stand's body's current pose."""
        ...

    def set_body_pose(self, pose: EulerAngle) -> None:
        """Sets the armor stand's body's current pose."""
        ...

    def get_left_arm_pose(self) -> EulerAngle:
        """Returns the armor stand's left arm's current pose."""
        ...

    def set_left_arm_pose(self, pose: EulerAngle) -> None:
        """Sets the armor stand's left arm's current pose."""
        ...

    def get_right_arm_pose(self) -> EulerAngle:
        """Returns the armor stand's right arm's current pose."""
        ...

    def set_right_arm_pose(self, pose: EulerAngle) -> None:
        """Sets the armor stand's right arm's current pose."""
        ...

    def get_left_leg_pose(self) -> EulerAngle:
        """Returns the armor stand's left leg's current pose."""
        ...

    def set_left_leg_pose(self, pose: EulerAngle) -> None:
        """Sets the armor stand's left leg's current pose."""
        ...

    def get_right_leg_pose(self) -> EulerAngle:
        """Returns the armor stand's right leg's current pose."""
        ...

    def set_right_leg_pose(self, pose: EulerAngle) -> None:
        """Sets the armor stand's right leg's current pose."""
        ...

    def get_head_pose(self) -> EulerAngle:
        """Returns the armor stand's head's current pose."""
        ...

    def set_head_pose(self, pose: EulerAngle) -> None:
        """Sets the armor stand's head's current pose."""
        ...

    def has_base_plate(self) -> bool:
        """Returns whether the armor stand has a base plate."""
        ...

    def set_base_plate(self, base_plate: bool) -> None:
        """Sets whether the armor stand has a base plate."""
        ...

    def is_visible(self) -> bool:
        """Returns whether the armor stand should be visible or not."""
        ...

    def set_visible(self, visible: bool) -> None:
        """Sets whether the armor stand should be visible or not."""
        ...

    def has_arms(self) -> bool:
        """Returns whether this armor stand has arms."""
        ...

    def set_arms(self, arms: bool) -> None:
        """Sets whether this armor stand has arms."""
        ...

    def is_small(self) -> bool:
        """Returns whether this armor stand is scaled down."""
        ...

    def set_small(self, small: bool) -> None:
        """Sets whether this armor stand is scaled down."""
        ...

    def is_marker(self) -> bool:
        """Returns whether this armor stand is a marker."""
        ...

    def set_marker(self, marker: bool) -> None:
        """Sets whether this armor stand is a marker."""
        ...

    def add_equipment_lock(self, slot: EquipmentSlot, lock_type: 'LockType') -> None:
        """Locks the equipment slot with the specified locking mechanism."""
        ...

    def remove_equipment_lock(self, slot: EquipmentSlot, lock_type: 'LockType') -> None:
        """Remove a locking mechanism."""
        ...

    def has_equipment_lock(self, slot: EquipmentSlot, lock_type: 'LockType') -> bool:
        """Returns if the ArmorStand has the specified locking mechanism."""
        ...

    class LockType:
        """
        Represents types of locking mechanisms for ArmorStand equipment.
        """
        ADDING_OR_CHANGING: Literal['ADDING_OR_CHANGING']
        REMOVING_OR_CHANGING: Literal['REMOVING_OR_CHANGING']
        ADDING: Literal['ADDING']
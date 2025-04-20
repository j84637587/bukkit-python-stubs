from org.bukkit.Rotation import Rotation
from org.bukkit.inventory.ItemStack import ItemStack
from typing import Optional

"""
Represents an Item Frame
"""
class ItemFrame:
    """
    Get the item in this frame

    @return a defensive copy the item in this item frame
    """
    def get_item(self) -> ItemStack:
        ...

    """
    Set the item in this frame

    @param item the new item
    """
    def set_item(self, item: Optional[ItemStack]) -> None:
        ...

    """
    Set the item in this frame

    @param item the new item
    @param play_sound whether or not to play the item placement sound
    """
    def set_item(self, item: Optional[ItemStack], play_sound: bool) -> None:
        ...

    """
    Gets the chance of the item being dropped upon this frame's destruction.

    <ul>
    <li>A drop chance of 0.0F will never drop
    <li>A drop chance of 1.0F will always drop
    </ul>

    @return chance of the off hand item being dropped
    """
    def get_item_drop_chance(self) -> float:
        ...

    """
    Sets the chance of the off hand item being dropped upon this frame's
    destruction.

    <ul>
    <li>A drop chance of 0.0F will never drop
    <li>A drop chance of 1.0F will always drop
    </ul>

    @param chance the chance of off hand item being dropped
    """
    def set_item_drop_chance(self, chance: float) -> None:
        ...

    """
    Get the rotation of the frame's item

    @return the direction
    """
    def get_rotation(self) -> Rotation:
        ...

    """
    Set the rotation of the frame's item

    @param rotation the new rotation
    @raises IllegalArgumentException if rotation is null
    """
    def set_rotation(self, rotation: Rotation) -> None:
        ...

    """
    Returns whether the item frame is be visible or not.

    @return whether the item frame is visible or not
    """
    def is_visible(self) -> bool:
        ...

    """
    Sets whether the item frame should be visible or not.

    @param visible whether the item frame is visible or not
    """
    def set_visible(self, visible: bool) -> None:
        ...

    """
    Returns whether the item frame is "fixed" or not.

    When true it's not possible to destroy/move the frame (e.g. by damage,
    interaction, pistons, or missing supporting blocks), rotate the item or
    place/remove items.

    @return whether the item frame is fixed or not
    """
    def is_fixed(self) -> bool:
        ...

    """
    Sets whether the item frame should be fixed or not.

    When set to true it's not possible to destroy/move the frame (e.g. by
    damage, interaction, pistons, or missing supporting blocks), rotate the
    item or place/remove items.

    @param fixed whether the item frame is fixed or not
    """
    def set_fixed(self, fixed: bool) -> None:
        ...
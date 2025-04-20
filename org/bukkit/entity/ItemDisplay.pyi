from org.bukkit.inventory import ItemStack
from org.jetbrains.annotations import NotNull, Nullable

"""
Represents an item display entity.
"""
class ItemDisplay(Display):

    """
    Gets the displayed item stack.

    @return: the displayed item stack
    """
    def get_item_stack(self) -> ItemStack:
        ...

    """
    Sets the displayed item stack.

    @param item: the new item stack
    """
    def set_item_stack(self, item: ItemStack) -> None:
        ...

    """
    Gets the item display transform for this entity.

    Defaults to {@link ItemDisplayTransform#FIXED}.

    @return: item display transform
    """
    def get_item_display_transform(self) -> ItemDisplayTransform:
        ...

    """
    Sets the item display transform for this entity.

    Defaults to {@link ItemDisplayTransform#FIXED}.

    @param display: new display
    """
    def set_item_display_transform(self, display: ItemDisplayTransform) -> None:
        ...


class ItemDisplayTransform:
    NONE = ...
    THIRDPERSON_LEFTHAND = ...
    THIRDPERSON_RIGHTHAND = ...
    FIRSTPERSON_LEFTHAND = ...
    FIRSTPERSON_RIGHTHAND = ...
    HEAD = ...
    GUI = ...
    GROUND = ...
    FIXED = ...
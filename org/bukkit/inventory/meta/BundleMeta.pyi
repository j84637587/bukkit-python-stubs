from typing import List, Optional
from org.bukkit.inventory import ItemStack
from org.jetbrains.annotations import ApiStatus, NotNull, Nullable

class BundleMeta(ItemMeta):
    """
    Interface for BundleMeta.
    """

    def has_items(self) -> bool:
        """
        Returns whether the item has any items.

        Returns:
            bool: whether items are present
        """
        ...

        def get_items(self) -> List[ItemStack]:
        """
        Returns an immutable list of the items stored in this item.

        Returns:
            List[ItemStack]: items
        """
        ...

    def set_items(self, items: Optional[List[ItemStack]]) -> None:
        """
        Sets the items stored in this item.
        Removes all items when given None.

        Args:
            items (Optional[List[ItemStack]]): the items to set
        """
        ...

    def add_item(self, item: ItemStack) -> None:
        """
        Adds an item to this item.

        Args:
            item (ItemStack): item to add
        """
        ...
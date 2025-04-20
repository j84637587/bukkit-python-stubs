from org.bukkit.inventory import InventoryView
from org.bukkit.inventory import LecternInventory
from typing import Protocol

class LecternView(InventoryView, Protocol):
    """
    An instance of {@link InventoryView} which provides extra methods related to
    lectern view data.
    """

    def get_top_inventory(self) -> LecternInventory:
        """
        Gets the top inventory of the lectern view.
        """
        ...

    def get_page(self) -> int:
        """
        Gets the page that the LecternView is on.

        Returns:
            The page the book is on.
        """
        ...

    def set_page(self, page: int) -> None:
        """
        Sets the page of the lectern book.

        Args:
            page: the lectern book page.
        """
        ...
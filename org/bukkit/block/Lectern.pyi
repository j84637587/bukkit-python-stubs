from typing import Protocol
from org.bukkit.inventory import BlockInventoryHolder, Inventory

class TileState(Protocol):
    pass

class Lectern(TileState, BlockInventoryHolder, Protocol):
    """
    Represents a captured state of a lectern.
    """

    def get_page(self) -> int:
        """
        Get the current lectern page.

        :return: current page
        """
        ...

    def set_page(self, page: int) -> None:
        """
        Set the current lectern page.

        If the page is greater than the number of pages of the book currently in
        the inventory, then behavior is undefined.

        :param page: new page
        """
        ...

    def get_inventory(self) -> Inventory:
        """
        :return: inventory
        :see: Container#getInventory()
        """
        ...

    def get_snapshot_inventory(self) -> Inventory:
        """
        :return: snapshot inventory
        :see: Container#getSnapshotInventory()
        """
        ...
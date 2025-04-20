from org.bukkit.inventory import InventoryView
from org.bukkit.inventory import Merchant
from org.bukkit.inventory import MerchantInventory
from typing import Protocol

class MerchantView(InventoryView, Protocol):
    """
    An instance of {@link InventoryView} which provides extra methods related to
    merchant view data.
    """

    def get_top_inventory(self) -> MerchantInventory:
        """
        Gets the top inventory.

        @return: The top inventory.
        """
        ...

    def get_merchant(self) -> Merchant:
        """
        Gets the merchant that this view is for.

        @return: The merchant that this view uses.
        """
        ...
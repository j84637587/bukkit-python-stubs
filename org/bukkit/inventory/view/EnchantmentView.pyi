from org.bukkit.enchantments import EnchantmentOffer
from org.bukkit.inventory import EnchantingInventory
from org.bukkit.inventory import InventoryView
from typing import List

class EnchantmentView(InventoryView):
    """
    An instance of {@link InventoryView} which provides extra methods related to
    enchantment table view data.
    """

    def get_top_inventory(self) -> EnchantingInventory:
        """
        @return: The top enchanting inventory.
        """
        ...

    def get_enchantment_seed(self) -> int:
        """
        Gets the random enchantment seed used in this view.

        @return: The random seed used.
        """
        ...

    def get_offers(self) -> List[EnchantmentOffer]:
        """
        Gets the offers of this EnchantmentView.

        @return: The enchantment offers that are provided.
        """
        ...

    def set_offers(self, offers: List[EnchantmentOffer]) -> None:
        """
        Sets the offers to provide to the player.

        @param offers: The offers to provide.
        @raises IllegalArgumentException: if the array length isn't 3.
        """
        ...
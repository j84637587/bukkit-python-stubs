from org.bukkit.inventory import AnvilInventory
from org.bukkit.inventory import InventoryView
from typing import Optional

class AnvilView(InventoryView):
    """
    An instance of {@link InventoryView} which provides extra methods related to
    anvil view data.
    """

    def get_top_inventory(self) -> AnvilInventory:
        """
        Gets the top inventory.

        :return: The top inventory as an AnvilInventory.
        """
        ...

    def get_rename_text(self) -> Optional[str]:
        """
        Gets the rename text specified within the anvil's text field.

        :return: The text within the anvil's text field if an item is present
                 otherwise None.
        """
        ...

    def get_repair_item_count_cost(self) -> int:
        """
        Gets the amount of items needed to repair.

        :return: The amount of materials required to repair the item.
        """
        ...

    def get_repair_cost(self) -> int:
        """
        Gets the experience cost needed to repair.

        :return: The repair cost in experience.
        """
        ...

    def get_maximum_repair_cost(self) -> int:
        """
        Gets the maximum repair cost needed to repair.

        :return: The maximum repair cost in experience.
        """
        ...

    def set_repair_item_count_cost(self, amount: int) -> None:
        """
        Sets the amount of repair materials required to repair the item.

        :param amount: The amount of repair materials.
        """
        ...

    def set_repair_cost(self, cost: int) -> None:
        """
        Sets the repair cost in experience.

        :param cost: The experience cost to repair.
        """
        ...

    def set_maximum_repair_cost(self, levels: int) -> None:
        """
        Sets maximum repair cost in experience.

        :param levels: The levels to set.
        """
        ...
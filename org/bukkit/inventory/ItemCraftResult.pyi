from typing import List
from org.bukkit.inventory import ItemStack

class ItemCraftResult:
    """
    Container class containing the results of a Crafting event.
    <br>
    This class makes no guarantees about the nature or mutability of the returned
    values.
    """

    def get_result(self) -> ItemStack:
        """
        The resulting ItemStack that was crafted.

        @return ItemStack that was crafted.
        """
        ...

    def get_resulting_matrix(self) -> List[ItemStack]:
        """
        Gets the resulting matrix from the crafting operation.

        @return resulting matrix
        """
        ...

    def get_overflow_items(self) -> List[ItemStack]:
        """
        Gets the overflowed items for items that don't fit back into the crafting
        matrix.

        @return overflow items
        """
        ...
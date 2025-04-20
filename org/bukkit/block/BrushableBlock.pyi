from typing import Optional
from org.bukkit.inventory import ItemStack
from org.bukkit.loot import Lootable
from org.bukkit.block import TileState

class BrushableBlock(Lootable, TileState):
    """
    Represents a captured state of suspicious sand or gravel.
    """

    def get_item(self) -> Optional[ItemStack]:
        """
        Get the item which will be revealed when the sand is fully brushed away
        and uncovered.

        :return: the item
        """
        ...

    def set_item(self, item: Optional[ItemStack]) -> None:
        """
        Sets the item which will be revealed when the sand is fully brushed away
        and uncovered.

        :param item: the item
        """
        ...
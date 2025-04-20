from org.bukkit.block import ChiseledBookshelf
from typing import Optional

class ChiseledBookshelfInventory:
    """
    Interface to the inventory of a chiseled bookshelf.
    """

    def get_holder(self) -> Optional[ChiseledBookshelf]:
        ...
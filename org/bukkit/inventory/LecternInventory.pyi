from org.bukkit.block import Lectern
from typing import Optional

class LecternInventory(Inventory):
    """
    Interface to the inventory of a Lectern.
    """

    def get_holder(self) -> Optional[Lectern]:
        ...
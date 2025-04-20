from typing import Optional
from org.bukkit import DyeColor
from org.bukkit.loot import Lootable
from org.bukkit.block import Container, Lidded

class ShulkerBox(Container, Lootable, Lidded):
    """
    Represents a captured state of a ShulkerBox.
    """

    def get_color(self) -> Optional[DyeColor]:
        """
        Get the {@link DyeColor} corresponding to this ShulkerBox

        @return: the {@link DyeColor} of this ShulkerBox, or None if default
        """
        ...
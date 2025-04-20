# org/bukkit/inventory/ItemRarity.pyi

from enum import Enum

class ItemRarity(Enum):
    """
    A item's rarity determines the default color of its name. This enum is
    ordered from least rare to most rare.
    """
    COMMON: ItemRarity
    UNCOMMON: ItemRarity
    RARE: ItemRarity
    EPIC: ItemRarity
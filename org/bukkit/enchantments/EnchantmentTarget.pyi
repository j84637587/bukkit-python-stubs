from org.bukkit.Material import Material
from org.bukkit.inventory.ItemStack import ItemStack
from typing import Literal

class EnchantmentTarget:
    """
    Represents the applicable target for a {@link Enchantment}
    """

    ALL: Literal['ALL']
    ARMOR: Literal['ARMOR']
    ARMOR_FEET: Literal['ARMOR_FEET']
    ARMOR_LEGS: Literal['ARMOR_LEGS']
    ARMOR_TORSO: Literal['ARMOR_TORSO']
    ARMOR_HEAD: Literal['ARMOR_HEAD']
    WEAPON: Literal['WEAPON']
    TOOL: Literal['TOOL']
    BOW: Literal['BOW']
    FISHING_ROD: Literal['FISHING_ROD']
    BREAKABLE: Literal['BREAKABLE']
    WEARABLE: Literal['WEARABLE']
    TRIDENT: Literal['TRIDENT']
    CROSSBOW: Literal['CROSSBOW']
    VANISHABLE: Literal['VANISHABLE']

    def includes(self, item: Material) -> bool:
        """
        Check whether this target includes the specified item.

        :param item: The item to check
        :return: True if the target includes the item
        """
        ...

    def includes_item_stack(self, item: ItemStack) -> bool:
        """
        Check whether this target includes the specified item.

        :param item: The item to check
        :return: True if the target includes the item
        """
        ...
from org.bukkit import Color
from org.bukkit import Material
from org.bukkit.inventory import ItemFactory
from org.bukkit.inventory.meta import ItemMeta
from typing import Optional

"""
Represents leather armor ({@link Material#LEATHER_BOOTS}, {@link
Material#LEATHER_CHESTPLATE}, {@link Material#LEATHER_HELMET}, or {@link
Material#LEATHER_LEGGINGS}) that can be colored.
"""
class LeatherArmorMeta(ItemMeta):

    """
    Gets the color of the armor. If it has not been set otherwise, it will
    be {@link ItemFactory#getDefaultLeatherColor()}.

    @return: the color of the armor, never null
    """
    def get_color(self) -> Color:
        ...

    """
    Sets the color of the armor.

    @param color: the color to set. Setting it to null is equivalent to
        setting it to {@link ItemFactory#getDefaultLeatherColor()}.
    """
    def set_color(self, color: Optional[Color]) -> None:
        ...

    def clone(self) -> LeatherArmorMeta:
        ...
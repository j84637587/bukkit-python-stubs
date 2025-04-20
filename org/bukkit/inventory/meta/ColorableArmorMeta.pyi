from org.bukkit.inventory.meta import ArmorMeta
from org.bukkit.inventory.meta import LeatherArmorMeta
from typing import Protocol

class ColorableArmorMeta(ArmorMeta, LeatherArmorMeta, Protocol):
    """
    Represents armor that an entity can equip and can also be colored.
    """

    def clone(self) -> 'ColorableArmorMeta':
        ...
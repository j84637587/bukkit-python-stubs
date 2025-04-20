from org.bukkit.inventory.meta import ItemMeta
from org.bukkit.inventory.meta.trim import ArmorTrim
from typing import Optional

class ArmorMeta(ItemMeta):
    """
    Represents armor that an entity can equip.
    <p>
    <strong>Note: Armor trims are part of an experimental feature of Minecraft
    and hence subject to change.</strong>
    """

    def has_trim(self) -> bool:
        """
        Check whether or not this item has an armor trim.

        @return true if has a trim, false otherwise
        """
        ...

    def set_trim(self, trim: Optional[ArmorTrim]) -> None:
        """
        Set the {@link ArmorTrim}.

        @param trim the trim to set, or null to remove it
        """
        ...

    def get_trim(self) -> Optional[ArmorTrim]:
        """
        Get the {@link ArmorTrim}.

        @return the armor trim, or null if none
        """
        ...

    def clone(self) -> 'ArmorMeta':
        ...
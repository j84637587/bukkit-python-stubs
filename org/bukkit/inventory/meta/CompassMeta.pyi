from org.bukkit.Location import Location
from org.bukkit.inventory.meta.ItemMeta import ItemMeta
from typing import Optional

class CompassMeta(ItemMeta):
    """
    Represents a compass that can track a specific location.
    """

    def has_lodestone(self) -> bool:
        """
        Checks if this compass has been paired to a lodestone.

        :return: paired status
        """
        ...

    def get_lodestone(self) -> Optional[Location]:
        """
        Gets the location that this compass will point to.

        Check {@link #hasLodestone()} first!

        :return: lodestone location
        """
        ...

    def set_lodestone(self, lodestone: Optional[Location]) -> None:
        """
        Sets the location this lodestone compass will point to.

        :param lodestone: new location or null to clear
        """
        ...

    def is_lodestone_tracked(self) -> bool:
        """
        Gets if this compass is tracking a specific lodestone.

        If true the compass will only work if there is a lodestone at the tracked
        location.

        :return: lodestone tracked
        """
        ...

    def set_lodestone_tracked(self, tracked: bool) -> None:
        """
        Sets if this compass is tracking a specific lodestone.

        If true the compass will only work if there is a lodestone at the tracked
        location.

        :param tracked: new tracked status
        """
        ...

    def clone(self) -> 'CompassMeta':
        ...
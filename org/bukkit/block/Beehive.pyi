from typing import Optional
from org.bukkit import Location
from org.bukkit.entity import Bee

class Beehive(EntityBlockStorage[Bee]):
    """
    Represents a captured state of a bee hive.
    """

    def get_flower(self) -> Optional[Location]:
        """
        Get the hive's flower location.

        :return: flower location or None
        """
        ...

    def set_flower(self, location: Optional[Location]) -> None:
        """
        Set the hive's flower location.

        :param location: or None
        """
        ...

    def is_sedated(self) -> bool:
        """
        Check if the hive is sedated due to smoke from a nearby campfire.

        :return: True if hive is sedated
        """
        ...

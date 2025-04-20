from org.bukkit.inventory import BrewerInventory
from org.bukkit.inventory import InventoryView
from typing import NoReturn

class BrewingStandView(InventoryView):
    """
    An instance of {@link InventoryView} which provides extra methods related to
    brewing stand view data.
    """

    def get_top_inventory(self) -> BrewerInventory:
        """
        Retrieves the top inventory of the brewing stand.
        
        :return: The top inventory.
        """
        ...

    def get_fuel_level(self) -> int:
        """
        Gets the fuel level of this brewing stand.
        <p>
        The default maximum fuel level in minecraft is 20.

        :return: The amount of fuel level left.
        """
        ...

    def get_brewing_ticks(self) -> int:
        """
        Gets the amount of brewing ticks left.

        :return: The amount of ticks left for the brewing task.
        """
        ...

    def set_fuel_level(self, level: int) -> NoReturn:
        """
        Sets the fuel level left.

        :param level: the level of the fuel, which is no less than 0.
        :raises IllegalArgumentException: if the level is less than 0.
        """
        ...

    def set_brewing_ticks(self, ticks: int) -> NoReturn:
        """
        Sets the brewing ticks left.

        :param ticks: the ticks left, which is no less than 0.
        :raises IllegalArgumentException: if the ticks are less than 0.
        """
        ...
from org.bukkit.block import Furnace
from org.bukkit.inventory import FurnaceInventory, InventoryView
from typing import Protocol

class FurnaceView(InventoryView, Protocol):
    """
    An instance of {@link InventoryView} which provides extra methods related to
    furnace view data.
    """

    def get_top_inventory(self) -> FurnaceInventory:
        """
        @return: the top inventory
        """
        ...

    def get_cook_time(self) -> float:
        """
        The cook time for this view.
        <p>
        See {@link Furnace#getCookTime()} for more information.
        <p>
        @return: a number between 0 and 1
        """
        ...

    def get_burn_time(self) -> float:
        """
        The total burn time for this view.
        <p>
        See {@link Furnace#getBurnTime()} for more information.
        <p>
        @return: a number between 0 and 1
        """
        ...

    def is_burning(self) -> bool:
        """
        Checks whether or not the furnace is burning
        <p>
        @return: true given that the furnace is burning
        """
        ...

    def set_cook_time(self, cook_progress: int, cook_duration: int) -> None:
        """
        Sets the cook time
        <p>
        Setting cook time requires manipulation of both cookProgress and
        cookDuration. This method does a simple division to get total progress
        within the furnaces visual duration bar. For a clear visual effect
        (cookProgress / cookDuration) should return a number between 0 and 1
        inclusively.
        <p>
        @param cook_progress: the current of the cooking
        @param cook_duration: the total cook time
        """
        ...

    def set_burn_time(self, burn_progress: int, burn_duration: int) -> None:
        """
        Sets the burn time
        <p>
        Setting burn time requires manipulation of both burnProgress and
        burnDuration. This method does a simple division to get total progress
        within the furnaces visual burning bar. For a clear visual effect
        (burnProgress / burnDuration) should return a number between 0 and 1
        inclusively.
        <p>
        @param burn_progress: the progress towards the burnDuration
        @param burn_duration: the total duration the view should be lit
        """
        ...
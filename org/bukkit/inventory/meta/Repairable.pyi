from org.bukkit.inventory.meta import ItemMeta
from typing import Protocol

class Repairable(ItemMeta, Protocol):
    """
    Represents an item that can be repaired at an anvil.
    """

    def has_repair_cost(self) -> bool:
        """
        Checks to see if this has a repair penalty.

        :return: true if this has a repair penalty
        """
        ...

    def get_repair_cost(self) -> int:
        """
        Gets the repair penalty.

        :return: the repair penalty
        """
        ...

    def set_repair_cost(self, cost: int) -> None:
        """
        Sets the repair penalty.

        :param cost: repair penalty
        """
        ...

    def clone(self) -> 'Repairable':
        """
        Clones this Repairable instance.

        :return: a clone of this Repairable
        """
        ...
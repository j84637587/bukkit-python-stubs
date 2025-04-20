from typing import Set
from org.bukkit.Material import Material
from org.bukkit.inventory import InventoryHolder

class Piglin(InventoryHolder):
    """Represents a Piglin."""

    def is_able_to_hunt(self) -> bool:
        """Get whether the piglin is able to hunt hoglins.

        Returns:
            Whether the piglin is able to hunt hoglins
        """
        ...

    def set_is_able_to_hunt(self, flag: bool) -> None:
        """Sets whether the piglin is able to hunt hoglins.

        Args:
            flag: Whether the piglin is able to hunt hoglins.
        """
        ...

    def add_barter_material(self, material: Material) -> bool:
        """Adds a material to the allowed list of materials to barter with.

        Args:
            material: The material to add

        Returns:
            true if the item has been added successfully, false otherwise
        """
        ...

    def remove_barter_material(self, material: Material) -> bool:
        """Removes a material from the allowed list of materials to barter with.

        Note: It's not possible to override the default
        bartering item gold_ingots as payment. To block gold_ingots see
        {@link org.bukkit.event.entity.PiglinBarterEvent}.

        Args:
            material: The material to remove

        Returns:
            true if the item has been removed successfully, false otherwise
        """
        ...

    def add_material_of_interest(self, material: Material) -> bool:
        """Adds a material the piglin will pickup and store in his inventory.

        Args:
            material: The material you want the piglin to be interested in

        Returns:
            true if the item has been added successfully, false otherwise
        """
        ...

    def remove_material_of_interest(self, material: Material) -> bool:
        """Removes a material from the list of materials the piglin will pickup.

        Note: It's not possible to override the default list of
        item the piglin will pickup. To cancel pickup see
        {@link org.bukkit.event.entity.EntityPickupItemEvent}.

        Args:
            material: The material you want removed from the interest list

        Returns:
            true if the item has been removed successfully, false otherwise
        """
        ...

    def get_interest_list(self) -> Set[Material]:
        """Returns a immutable set of materials the piglins will pickup.

        Note: This set will not include the items that are set
        by default. To interact with those items see
        {@link org.bukkit.event.entity.EntityPickupItemEvent}.

        Returns:
            An immutable materials set
        """
        ...

    def get_barter_list(self) -> Set[Material]:
        """Returns a immutable set of materials the piglins will barter with.

        Note: This set will not include the items that are set
        by default. To interact with those items see
        {@link org.bukkit.event.entity.PiglinBarterEvent}.

        Returns:
            An immutable materials set
        """
        ...
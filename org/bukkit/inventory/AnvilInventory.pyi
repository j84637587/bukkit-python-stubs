from org.bukkit.inventory import Inventory
from org.bukkit.inventory.view import AnvilView
from typing import Optional

class AnvilInventory(Inventory):
    """
    Interface to the inventory of an Anvil.
    """

    @Deprecated
    def get_rename_text(self) -> Optional[str]:
        """
        Get the name to be applied to the repaired item. An empty string denotes
        the default item name.

        :return: the rename text
        :deprecated: use {@link AnvilView#getRenameText()}.
        """
        ...

    @Deprecated
    def get_repair_cost_amount(self) -> int:
        """
        Get the item cost (in amount) to complete the current repair.

        :return: the amount
        :deprecated: use {@link AnvilView#getRepairItemCountCost()}.
        """
        ...

    @Deprecated
    def set_repair_cost_amount(self, amount: int) -> None:
        """
        Set the item cost (in amount) to complete the current repair.

        :param amount: the amount
        :deprecated: use {@link AnvilView#setRepairItemCountCost(int)}.
        """
        ...

    @Deprecated
    def get_repair_cost(self) -> int:
        """
        Get the experience cost (in levels) to complete the current repair.

        :return: the experience cost
        :deprecated: use {@link AnvilView#getRepairCost()}.
        """
        ...

    @Deprecated
    def set_repair_cost(self, levels: int) -> None:
        """
        Set the experience cost (in levels) to complete the current repair.

        :param levels: the experience cost
        :deprecated: use {@link AnvilView#setRepairCost(int)}.
        """
        ...

    @Deprecated
    def get_maximum_repair_cost(self) -> int:
        """
        Get the maximum experience cost (in levels) to be allowed by the current
        repair. If the result of {@link #getRepairCost()} exceeds the returned
        value, the repair result will be air due to being "too expensive".
        <p>
        By default, this level is set to 40. Players in creative mode ignore the
        maximum repair cost.

        :return: the maximum experience cost
        :deprecated: use {@link AnvilView#getMaximumRepairCost()}.
        """
        ...

    @Deprecated
    def set_maximum_repair_cost(self, levels: int) -> None:
        """
        Set the maximum experience cost (in levels) to be allowed by the current
        repair. The default value set by vanilla Minecraft is 40.

        :param levels: the maximum experience cost
        :deprecated: use {@link AnvilView#setMaximumRepairCost(int)}.
        """
        ...
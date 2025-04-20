from typing import Set, Optional
from uuid import UUID
from org.bukkit.inventory import ItemStack
from org.bukkit.loot import LootTable
from org.jetbrains.annotations import ApiStatus, NotNull, Nullable

class Vault(TileState):
    """Represents a captured state of a vault."""

    def get_activation_range(self) -> float:
        """Gets the distance at which a player must enter for this vault to activate.

        Returns:
            float: the distance at which a player must enter for this vault to activate.
        """
        ...

    def set_activation_range(self, range: float) -> None:
        """Sets the distance at which a player must enter for this vault to activate.

        Args:
            range (float): the distance at which a player must enter for this vault to activate.
        """
        ...

    def get_deactivation_range(self) -> float:
        """Gets the distance at which a player must exit for the vault to deactivate.

        Returns:
            float: the distance at which a player must exit for the vault to deactivate.
        """
        ...

    def set_deactivation_range(self, range: float) -> None:
        """Sets the distance at which a player must exit for this vault to deactivate.

        Args:
            range (float): the distance at which a player must exit for this vault to deactivate.
        """
        ...

        def get_loot_table(self) -> LootTable:
        """Gets the LootTable this vault will pick rewards from.

        Returns:
            LootTable: the loot table
        """
        ...

    def set_loot_table(self, table: LootTable) -> None:
        """Sets the LootTable this vault will pick rewards from.

        Args:
            table (LootTable): the loot table
        """
        ...

        def get_display_loot_table(self) -> Optional[LootTable]:
        """Gets the LootTable this vault will display items from.

        If this value is null the regular loot table will be used to display items.

        Returns:
            Optional[LootTable]: the loot table to display items from
        """
        ...

    def set_display_loot_table(self, table: Optional[LootTable]) -> None:
        """Sets the LootTable this vault will display items from.

        If this value is set to null the regular loot table will be used to display items.

        Args:
            table (Optional[LootTable]): the loot table to display items from
        """
        ...

        def get_key_item(self) -> ItemStack:
        """Gets the ItemStack players must use to unlock this vault.

        Returns:
            ItemStack: the key item
        """
        ...

    def set_key_item(self, key_item: ItemStack) -> None:
        """Sets the ItemStack players must use to unlock this vault.

        Args:
            key_item (ItemStack): the key item
        """
        ...

        def get_rewarded_players(self) -> Set[UUID]:
        """Gets the players who have already received rewards from this vault.

        Returns:
            Set[UUID]: unmodifiable set of player UUIDs

        Raises:
            IllegalStateException: if this block state is not placed
        """
        ...
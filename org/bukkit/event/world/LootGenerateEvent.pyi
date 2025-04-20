from typing import Collection, List, Optional
from org.bukkit import World
from org.bukkit.entity import Entity
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.inventory import InventoryHolder, ItemStack
from org.bukkit.loot import LootContext, LootTable

class LootGenerateEvent(WorldEvent, Cancellable):
    """
    Called when a :class:`LootTable` is generated in the world for an
    :class:`InventoryHolder`.

    This event is NOT currently called when an entity's loot table has been
    generated (use :class:`EntityDeathEvent.getDrops()`, but WILL be called by
    plugins invoking
    :class:`LootTable.fillInventory(org.bukkit.inventory.Inventory, java.util.Random, LootContext)`.
    """

    handlers: HandlerList

    def __init__(self, world: World, entity: Optional[Entity], inventory_holder: Optional[InventoryHolder], loot_table: LootTable, loot_context: LootContext, items: List[ItemStack], plugin: bool) -> None:
        """
        Initialize the LootGenerateEvent.

        :param world: The world where the event is occurring.
        :param entity: The entity used as context for loot generation (if applicable).
        :param inventory_holder: The inventory holder in which the loot was generated.
        :param loot_table: The loot table used to generate loot.
        :param loot_context: The loot context used to provide context to the loot table's loot generation.
        :param items: The list of items to generate.
        :param plugin: Whether the event was caused by a plugin.
        """
        ...

    def get_entity(self) -> Optional[Entity]:
        """
        Get the entity used as context for loot generation (if applicable).

        For inventories where entities are not required to generate loot, such as
        hoppers, None will be returned.

        This is a convenience method for
        `getLootContext().getLootedEntity()`.

        :return: The entity.
        """
        ...

    def get_inventory_holder(self) -> Optional[InventoryHolder]:
        """
        Get the inventory holder in which the loot was generated.

        If the loot was generated as a result of the block being broken, the
        inventory holder will be None as this event is called post block break.

        :return: The inventory holder.
        """
        ...

    def get_loot_table(self) -> LootTable:
        """
        Get the loot table used to generate loot.

        :return: The loot table.
        """
        ...

    def get_loot_context(self) -> LootContext:
        """
        Get the loot context used to provide context to the loot table's loot
        generation.

        :return: The loot context.
        """
        ...

    def set_loot(self, loot: Optional[Collection[ItemStack]]) -> None:
        """
        Set the loot to be generated. None items will be treated as air.

        Note: the set collection is not the one which will be returned by
        `getLoot()`.

        :param loot: The loot to generate, None to clear all loot.
        """
        ...

    def get_loot(self) -> List[ItemStack]:
        """
        Get a mutable list of all loot to be generated.

        Any items added or removed from the returned list will be reflected in
        the loot generation. None items will be treated as air.

        :return: The loot to generate.
        """
        ...

    def is_plugin(self) -> bool:
        """
        Check whether or not this event was called as a result of a plugin
        invoking
        `LootTable.fillInventory(org.bukkit.inventory.Inventory, java.util.Random, LootContext)`.

        :return: True if plugin caused, False otherwise.
        """
        ...

    def set_cancelled(self, cancel: bool) -> None:
        ...
    
    def is_cancelled(self) -> bool:
        ...

    def get_handlers(self) -> HandlerList:
        ...

    @staticmethod
    def get_handler_list() -> HandlerList:
        ...
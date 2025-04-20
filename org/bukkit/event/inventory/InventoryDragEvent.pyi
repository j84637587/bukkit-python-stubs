from collections.abc import Mapping, Set
from typing import Optional, Dict

from org.bukkit.Location import Location
from org.bukkit.entity.HumanEntity import HumanEntity
from org.bukkit.entity.Player import Player
from org.bukkit.event.HandlerList import HandlerList
from org.bukkit.inventory.Inventory import Inventory
from org.bukkit.inventory.InventoryView import InventoryView
from org.bukkit.inventory.ItemStack import ItemStack
from org.bukkit.plugin.Plugin import Plugin
from org.bukkit.scheduler.BukkitScheduler import BukkitScheduler
from org.jetbrains.annotations import NotNull, Nullable

class InventoryDragEvent(InventoryInteractEvent):
    """
    This event is called when the player drags an item in their cursor across
    the inventory. The ItemStack is distributed across the slots the
    HumanEntity dragged over. The method of distribution is described by the
    DragType returned by {@link #getType()}.
    <p>
    Canceling this event will result in none of the changes described in
    {@link #getNewItems()} being applied to the Inventory.
    <p>
    Because InventoryDragEvent occurs within a modification of the Inventory,
    not all Inventory related methods are safe to use.
    <p>
    The following should never be invoked by an EventHandler for
    InventoryDragEvent using the HumanEntity or InventoryView associated with
    this event.
    <ul>
    <li>{@link HumanEntity#closeInventory()}
    <li>{@link HumanEntity#openInventory(Inventory)}
    <li>{@link HumanEntity#openWorkbench(Location, boolean)}
    <li>{@link HumanEntity#openEnchanting(Location, boolean)}
    <li>{@link InventoryView#close()}
    </ul>
    To invoke one of these methods, schedule a task using
    {@link BukkitScheduler#runTask(Plugin, Runnable)}, which will run the task
    on the next tick.  Also be aware that this is not an exhaustive list, and
    other methods could potentially create issues as well.
    <p>
    Assuming the EntityHuman associated with this event is an instance of a
    Player, manipulating the MaxStackSize or contents of an Inventory will
    require an Invocation of {@link Player#updateInventory()}.
    <p>
    Any modifications to slots that are modified by the results of this
    InventoryDragEvent will be overwritten. To change these slots, this event
    should be cancelled and the changes applied. Alternatively, scheduling a
    task using {@link BukkitScheduler#runTask(Plugin, Runnable)}, which would
    execute the task on the next tick, would work as well.
    """

    handlers: HandlerList

    def __init__(self, what: InventoryView, new_cursor: Optional[ItemStack], old_cursor: ItemStack, right: bool, slots: Mapping[int, ItemStack]) -> None:
        ...

        def getNewItems(self) -> Mapping[int, ItemStack]:
        ...

        def getRawSlots(self) -> Set[int]:
        ...

        def getInventorySlots(self) -> Set[int]:
        ...

        def getCursor(self) -> Optional[ItemStack]:
        ...

    def setCursor(self, new_cursor: Optional[ItemStack]) -> None:
        ...

        def getOldCursor(self) -> ItemStack:
        ...

        def getType(self) -> DragType:
        ...

        def getHandlers(self) -> HandlerList:
        ...

        @staticmethod
    def getHandlerList() -> HandlerList:
        ...
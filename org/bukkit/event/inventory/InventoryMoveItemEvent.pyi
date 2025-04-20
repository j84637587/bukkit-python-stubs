from typing import Any
from org.bukkit.event import Cancellable, Event, HandlerList
from org.bukkit.inventory import Inventory, ItemStack
from google.common.base import Preconditions
from org.jetbrains.annotations import NotNull

class InventoryMoveItemEvent(Event, Cancellable):
    handlers: HandlerList = HandlerList()

    def __init__(self,
                 sourceInventory: Inventory,
                 itemStack: ItemStack,
                 destinationInventory: Inventory,
                 didSourceInitiate: bool) -> None:
        """
        Called when some entity or block (e.g. hopper) tries to move items directly
        from one inventory to another.
        <p>
        When this event is called, the initiator may already have removed the item
        from the source inventory and is ready to move it into the destination
        inventory.
        <p>
        If this event is cancelled, the items will be returned to the source
        inventory, if needed.
        <p>
        If this event is not cancelled, the initiator will try to put the ItemStack
        into the destination inventory. If this is not possible and the ItemStack
        has not been modified, the source inventory slot will be restored to its
        former state. Otherwise any additional items will be discarded.
        """
        Preconditions.checkArgument(itemStack is not None, "ItemStack cannot be null")
        self.sourceInventory: Inventory = sourceInventory
        self.itemStack: ItemStack = itemStack
        self.destinationInventory: Inventory = destinationInventory
        self.didSourceInitiate: bool = didSourceInitiate
        self.cancelled: bool = False

        def getSource(self) -> Inventory:
        """
        Gets the Inventory that the ItemStack is being taken from

        @return Inventory that the ItemStack is being taken from
        """
        return self.sourceInventory

        def getItem(self) -> ItemStack:
        """
        Gets the ItemStack being moved; if modified, the original item will not
        be removed from the source inventory.

        @return ItemStack
        """
        return self.itemStack.clone()

    def setItem(self, itemStack: ItemStack) -> None:
        """
        Sets the ItemStack being moved; if this is different from the original
        ItemStack, the original item will not be removed from the source
        inventory.

        @param itemStack The ItemStack
        """
        Preconditions.checkArgument(itemStack is not None, "ItemStack cannot be null.  Cancel the event if you want nothing to be transferred.")
        self.itemStack = itemStack.clone()

        def getDestination(self) -> Inventory:
        """
        Gets the Inventory that the ItemStack is being put into

        @return Inventory that the ItemStack is being put into
        """
        return self.destinationInventory

        def getInitiator(self) -> Inventory:
        """
        Gets the Inventory that initiated the transfer. This will always be
        either the destination or source Inventory.

        @return Inventory that initiated the transfer
        """
        return self.sourceInventory if self.didSourceInitiate else self.destinationInventory

    def isCancelled(self) -> bool:
        return self.cancelled

    def setCancelled(self, cancel: bool) -> None:
        self.cancelled = cancel

        def getHandlers(self) -> HandlerList:
        return self.handlers

        @staticmethod
    def getHandlerList() -> HandlerList:
        return InventoryMoveItemEvent.handlers
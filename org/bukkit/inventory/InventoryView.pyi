from org.bukkit.entity import HumanEntity
from org.bukkit.inventory import Inventory
from org.bukkit.event.inventory import InventoryType
from typing import Optional

"""
Represents a view linking two inventories and a single player (whose
inventory may or may not be one of the two).
"""
class InventoryView:
    OUTSIDE: int = -999

    class Property:
        """
        Represents various extra properties of certain inventory windows.
        @deprecated use {@link InventoryView} and its children
        """
        BREW_TIME: 'Property'
        FUEL_TIME: 'Property'
        BURN_TIME: 'Property'
        TICKS_FOR_CURRENT_FUEL: 'Property'
        COOK_TIME: 'Property'
        TICKS_FOR_CURRENT_SMELTING: 'Property'
        ENCHANT_BUTTON1: 'Property'
        ENCHANT_BUTTON2: 'Property'
        ENCHANT_BUTTON3: 'Property'
        ENCHANT_XP_SEED: 'Property'
        ENCHANT_ID1: 'Property'
        ENCHANT_ID2: 'Property'
        ENCHANT_ID3: 'Property'
        ENCHANT_LEVEL1: 'Property'
        ENCHANT_LEVEL2: 'Property'
        ENCHANT_LEVEL3: 'Property'
        LEVELS: 'Property'
        PRIMARY_EFFECT: 'Property'
        SECONDARY_EFFECT: 'Property'
        REPAIR_COST: 'Property'
        BOOK_PAGE: 'Property'

        def __init__(self, id: int, applies_to: InventoryType):
            self.id: int = id
            self.style: InventoryType = applies_to

        def get_type(self) -> InventoryType:
            """
            @return: the type of this property
            """
            pass

        def get_id(self) -> int:
            """
            Gets the id of this view.
            @return: the id of this view
            @deprecated Magic value
            """
            pass

    def get_top_inventory(self) -> Inventory:
        """
        Get the upper inventory involved in this transaction.
        @return: the inventory
        """
        pass

    def get_bottom_inventory(self) -> Inventory:
        """
        Get the lower inventory involved in this transaction.
        @return: the inventory
        """
        pass

    def get_player(self) -> HumanEntity:
        """
        Get the player viewing.
        @return: the player
        """
        pass

    def get_type(self) -> InventoryType:
        """
        Determine the type of inventory involved in the transaction. This
        indicates the window style being shown. It will never return PLAYER,
        since that is common to all windows.
        @return: the inventory type
        """
        pass

    def set_item(self, slot: int, item: Optional['ItemStack']) -> None:
        """
        Sets one item in this inventory view by its raw slot ID.
        Note: If slot ID -999 is chosen, it may be expected that the item is
        dropped on the ground. This is not required behaviour, however.
        @param slot: The ID as returned by InventoryClickEvent.getRawSlot()
        @param item: The new item to put in the slot, or null to clear it.
        """
        pass

    def get_item(self, slot: int) -> Optional['ItemStack']:
        """
        Gets one item in this inventory view by its raw slot ID.
        @param slot: The ID as returned by InventoryClickEvent.getRawSlot()
        @return: The item currently in the slot.
        """
        pass

    def set_cursor(self, item: Optional['ItemStack']) -> None:
        """
        Sets the item on the cursor of one of the viewing players.
        @param item: The item to put on the cursor, or null to remove the item
        on their cursor.
        """
        pass

    def get_cursor(self) -> Optional['ItemStack']:
        """
        Get the item on the cursor of one of the viewing players.
        @return: The item on the player's cursor, or null if they aren't holding
        one.
        """
        pass

    def get_inventory(self, raw_slot: int) -> Optional[Inventory]:
        """
        Gets the inventory corresponding to the given raw slot ID.
        If the slot ID is {@link #OUTSIDE} null will be returned, otherwise
        behaviour for illegal and negative slot IDs is undefined.
        May be used with {@link #convertSlot(int)} to directly index an
        underlying inventory.
        @param raw_slot: The raw slot ID.
        @return: corresponding inventory, or null
        """
        pass

    def convert_slot(self, raw_slot: int) -> int:
        """
        Converts a raw slot ID into its local slot ID into whichever of the two
        inventories the slot points to.
        If the raw slot refers to the upper inventory, it will be returned
        unchanged and thus be suitable for getTopInventory().getItem(); if it
        refers to the lower inventory, the output will differ from the input
        and be suitable for getBottomInventory().getItem().
        @param raw_slot: The raw slot ID.
        @return: The converted slot ID.
        """
        pass

    def get_slot_type(self, slot: int) -> InventoryType.SlotType:
        """
        Determine the type of the slot by its raw slot ID.
        If the type of the slot is unknown, then
        {@link InventoryType.SlotType#CONTAINER} will be returned.
        @param slot: The raw slot ID
        @return: the slot type
        """
        pass

    def close(self) -> None:
        """
        Closes the inventory view.
        """
        pass

    def count_slots(self) -> int:
        """
        Check the total number of slots in this view, combining the upper and
        lower inventories.
        Note though that it's possible for this to be greater than the sum of
        the two inventories if for example some slots are not being used.
        @return: The total size
        """
        pass

    def set_property(self, prop: Property, value: int) -> bool:
        """
        Sets an extra property of this inventory if supported by that
        inventory, for example the state of a progress bar.
        @param prop: the window property to update
        @param value: the new value for the window property
        @return: true if the property was updated successfully, false if the
        property is not supported by that inventory
        """
        pass

    def get_title(self) -> str:
        """
        Get the title of this inventory window.
        @return: The title.
        """
        pass

    def get_original_title(self) -> str:
        """
        Get the original title of this inventory window, before any changes were
        made using {@link #setTitle(String)}.
        @return: the original title
        """
        pass

    def set_title(self, title: str) -> None:
        """
        Sets the title of this inventory window to the specified title if the
        inventory window supports it.
        Note if the inventory does not support titles that can be changed (ie, it
        is not creatable or viewed by a player), then this method will throw an
        exception.
        @param title: The new title.
        """
        pass
from enum import Enum

class InventoryAction(Enum):
    """
    An estimation of what the result will be.
    """
    NOTHING = ...
    """
    Nothing will happen from the click.
    There may be cases where nothing will happen and this value is not
    provided, but it is guaranteed that this value is accurate when given.
    """
    
    PICKUP_ALL = ...
    """
    All of the items on the clicked slot are moved to the cursor.
    """
    
    PICKUP_SOME = ...
    """
    Some of the items on the clicked slot are moved to the cursor.
    """
    
    PICKUP_HALF = ...
    """
    Half of the items on the clicked slot are moved to the cursor.
    """
    
    PICKUP_ONE = ...
    """
    One of the items on the clicked slot are moved to the cursor.
    """
    
    PLACE_ALL = ...
    """
    All of the items on the cursor are moved to the clicked slot.
    """
    
    PLACE_SOME = ...
    """
    Some of the items from the cursor are moved to the clicked slot
    (usually up to the max stack size).
    """
    
    PLACE_ONE = ...
    """
    A single item from the cursor is moved to the clicked slot.
    """
    
    SWAP_WITH_CURSOR = ...
    """
    The clicked item and the cursor are exchanged.
    """
    
    DROP_ALL_CURSOR = ...
    """
    The entire cursor item is dropped.
    """
    
    DROP_ONE_CURSOR = ...
    """
    One item is dropped from the cursor.
    """
    
    DROP_ALL_SLOT = ...
    """
    The entire clicked slot is dropped.
    """
    
    DROP_ONE_SLOT = ...
    """
    One item is dropped from the clicked slot.
    """
    
    MOVE_TO_OTHER_INVENTORY = ...
    """
    The item is moved to the opposite inventory if a space is found.
    """
    
    HOTBAR_MOVE_AND_READD = ...
    """
    The clicked item is moved to the hotbar, and the item currently there
    is re-added to the player's inventory.
    
    The hotbar includes the player's off hand.
    """
    
    HOTBAR_SWAP = ...
    """
    The clicked slot and the picked hotbar slot are swapped.
    
    The hotbar includes the player's off hand.
    """
    
    CLONE_STACK = ...
    """
    A max-size stack of the clicked item is put on the cursor.
    """
    
    COLLECT_TO_CURSOR = ...
    """
    The inventory is searched for the same material, and they are put on
    the cursor up to {@link org.bukkit.Material#getMaxStackSize()}.
    """
    
    UNKNOWN = ...
    """
    An unrecognized ClickType.
    """
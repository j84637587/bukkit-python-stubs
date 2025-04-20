# org/bukkit/event/inventory/DragType.pyi

from enum import Enum

class DragType(Enum):
    """Represents the effect of a drag that will be applied to an Inventory in an InventoryDragEvent."""
    
    SINGLE = ...  # One item from the cursor is placed in each selected slot.
    EVEN = ...    # The cursor is split evenly across all selected slots, not to exceed the Material's max stack size, with the remainder going to the cursor.
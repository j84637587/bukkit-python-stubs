from typing import List
from org.bukkit.block.banner import PatternType
from org.bukkit.inventory import InventoryView, LoomInventory
from org.jetbrains.annotations import NotNull

class LoomView(InventoryView):
    """
    An instance of {@link InventoryView} which provides extra methods related to
    loom view data.
    """

        def get_top_inventory(self) -> LoomInventory:
        ...

        def get_selectable_patterns(self) -> List[PatternType]:
        """
        Gets a list of all selectable to the player.

        @return A copy of the {@link PatternType}'s currently selectable by the
        player
        """
        ...

    def get_selected_pattern_index(self) -> int:
        """
        Gets an index of the selected pattern.

        @return Index of the selected pattern
        """
        ...
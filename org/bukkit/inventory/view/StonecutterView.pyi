from typing import List
from org.bukkit.inventory import InventoryView
from org.bukkit.inventory import StonecutterInventory
from org.bukkit.inventory import StonecuttingRecipe
from org.jetbrains.annotations import NotNull

"""
An instance of {@link InventoryView} which provides extra methods related to
stonecutter view data.
"""
class StonecutterView(InventoryView):

        def get_top_inventory(self) -> StonecutterInventory:
        ...

    """
    Gets the current index of the selected recipe.

    @return The index of the selected recipe in the stonecutter or -1 if null
    """
    def get_selected_recipe_index(self) -> int:
        ...

    """
    Gets a copy of all recipes currently available to the player.

    @return A copy of the {@link StonecuttingRecipe}'s currently available
    for the player
    """
        def get_recipes(self) -> List[StonecuttingRecipe]:
        ...

    """
    Gets the amount of recipes currently available.

    @return The amount of recipes currently available for the player
    """
    def get_recipe_amount(self) -> int:
        ...
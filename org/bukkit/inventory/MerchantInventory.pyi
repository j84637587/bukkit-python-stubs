from typing import Optional
from org.bukkit.inventory import Inventory
from org.jetbrains.annotations import NotNull, Nullable

class MerchantRecipe:
    pass

class Merchant:
    pass

class MerchantInventory(Inventory):
    """
    Represents a trading inventory between a player and a merchant.
    <br>
    The holder of this Inventory is the owning Villager, or null if the player is
    trading with a merchant created by a plugin.
    """

    def get_selected_recipe_index(self) -> int:
        """
        Get the index of the currently selected recipe.

        @return: the index of the currently selected recipe
        """
        ...

    def get_selected_recipe(self) -> Optional[MerchantRecipe]:
        """
        Get the currently active recipe.
        <p>
        This will be <code>null</code> if the items provided by the player do
        not match the ingredients of the selected recipe. This does not
        necessarily match the recipe selected by the player: If the player has
        selected the first recipe, the merchant will search all of its offers
        for a matching recipe to activate.

        @return: the currently active recipe
        """
        ...

        def get_merchant(self) -> Merchant:
        """
        Gets the Merchant associated with this inventory.

        @return: merchant
        """
        ...
from org.bukkit.inventory import Recipe
from org.bukkit import Keyed

class ComplexRecipe(Recipe, Keyed):
    """Represents a complex recipe which has imperative server-defined behavior, eg
    armor dyeing.

    Note: Since a complex recipe has dynamic outputs, `get_result()` will
    sometimes return an AIR ItemStack.
    """
    pass
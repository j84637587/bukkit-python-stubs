from typing import TypeVar
from org.bukkit import Material
from org.bukkit import NamespacedKey
from org.bukkit.inventory import CookingRecipe
from org.bukkit.inventory import ItemStack
from org.bukkit.material import MaterialData
from org.bukkit.inventory import RecipeChoice
from typing import List

FurnaceRecipeType = TypeVar('FurnaceRecipeType', bound='FurnaceRecipe')

class FurnaceRecipe(CookingRecipe[FurnaceRecipeType]):
    """
    Represents a furnace recipe.
    """

    def __init__(self, result: ItemStack, source: Material) -> None:
        """
        @deprecated since: "1.13"
        """
        ...

    def __init__(self, result: ItemStack, source: MaterialData) -> None:
        """
        @deprecated since: "1.13"
        """
        ...

    def __init__(self, result: ItemStack, source: MaterialData, experience: float) -> None:
        """
        @deprecated since: "1.13"
        """
        ...

    def __init__(self, result: ItemStack, source: Material, data: int) -> None:
        """
        @deprecated since: "1.6.2"
        """
        ...

    def __init__(self, key: NamespacedKey, result: ItemStack, source: Material, experience: float, cooking_time: int) -> None:
        """
        Create a furnace recipe to craft the specified ItemStack.

        @param key The unique recipe key
        @param result The item you want the recipe to create.
        @param source The input material.
        @param experience The experience given by this recipe
        @param cooking_time The cooking time (in ticks)
        """
        ...

    def __init__(self, key: NamespacedKey, result: ItemStack, source: Material, data: int, experience: float, cooking_time: int) -> None:
        """
        @deprecated since: "1.9"
        """
        ...

    def __init__(self, key: NamespacedKey, result: ItemStack, input: RecipeChoice, experience: float, cooking_time: int) -> None:
        """
        Create a furnace recipe to craft the specified ItemStack.

        @param key The unique recipe key
        @param result The item you want the recipe to create.
        @param input The input choices.
        @param experience The experience given by this recipe
        @param cooking_time The cooking time (in ticks)
        """
        ...

    def setInput(self, input: MaterialData) -> FurnaceRecipeType:
        """
        Sets the input of this furnace recipe.

        @param input The input material.
        @return The changed recipe, so you can chain calls.
        """
        ...

    def setInput(self, input: Material) -> FurnaceRecipeType:
        ...
    
    def setInput(self, input: Material, data: int) -> FurnaceRecipeType:
        """
        Sets the input of this furnace recipe.

        @param input The input material.
        @param data The data value. (Note: This is currently ignored by the
            CraftBukkit server.)
        @return The changed recipe, so you can chain calls.
        @deprecated Magic value
        """
        ...

    def setInputChoice(self, input: RecipeChoice) -> FurnaceRecipeType:
        ...
from typing import TypeVar, Generic
from org.bukkit.inventory import Recipe
from org.bukkit import Keyed, NamespacedKey, Material
from org.bukkit.inventory.recipe import CookingBookCategory
from org.bukkit.inventory import ItemStack, RecipeChoice
from collections.abc import Iterable

T = TypeVar('T', bound='CookingRecipe')

class CookingRecipe(Generic[T], Recipe, Keyed):
    """
    Represents a cooking recipe.
    @param <T> type of recipe
    """

    def __init__(self, key: NamespacedKey, result: ItemStack, source: Material, experience: float, cookingTime: int) -> None:
        """
        Create a cooking recipe to craft the specified ItemStack.

        @param key The unique recipe key
        @param result The item you want the recipe to create.
        @param source The input material.
        @param experience The experience given by this recipe
        @param cookingTime The cooking time (in ticks)
        """
        ...

    def __init__(self, key: NamespacedKey, result: ItemStack, input: RecipeChoice, experience: float, cookingTime: int) -> None:
        """
        Create a cooking recipe to craft the specified ItemStack.

        @param key The unique recipe key
        @param result The item you want the recipe to create.
        @param input The input choices.
        @param experience The experience given by this recipe
        @param cookingTime The cooking time (in ticks)
        """
        ...

    def setInput(self, input: Material) -> 'CookingRecipe':
        """
        Sets the input of this cooking recipe.

        @param input The input material.
        @return The changed recipe, so you can chain calls.
        """
        ...

    def getInput(self) -> ItemStack:
        """
        Get the input material.

        @return The input material.
        """
        ...

    def setInputChoice(self, input: RecipeChoice) -> T:
        """
        Sets the input of this cooking recipe.

        @param input The input choice.
        @return The changed recipe, so you can chain calls.
        """
        ...

    def getInputChoice(self) -> RecipeChoice:
        """
        Get the input choice.

        @return The input choice.
        """
        ...

    def getResult(self) -> ItemStack:
        """
        Get the result of this recipe.

        @return The resulting stack.
        """
        ...

    def setExperience(self, experience: float) -> None:
        """
        Sets the experience given by this recipe.

        @param experience the experience level
        """
        ...

    def getExperience(self) -> float:
        """
        Get the experience given by this recipe.

        @return experience level
        """
        ...

    def setCookingTime(self, cookingTime: int) -> None:
        """
        Set the cooking time for this recipe in ticks.

        @param cookingTime new cooking time
        """
        ...

    def getCookingTime(self) -> int:
        """
        Get the cooking time for this recipe in ticks.

        @return cooking time
        """
        ...

    def getKey(self) -> NamespacedKey:
        """
        @return The unique key for this recipe.
        """
        ...

    def getGroup(self) -> str:
        """
        Get the group of this recipe. Recipes with the same group may be grouped
        together when displayed in the client.

        @return recipe group. An empty string denotes no group. May not be null.
        """
        ...

    def setGroup(self, group: str) -> None:
        """
        Set the group of this recipe. Recipes with the same group may be grouped
        together when displayed in the client.

        @param group recipe group. An empty string denotes no group. May not be
        null.
        """
        ...

    def getCategory(self) -> CookingBookCategory:
        """
        Gets the category which this recipe will appear in the recipe book under.

        Defaults to {@link CookingBookCategory#MISC} if not set.

        @return recipe book category
        """
        ...

    def setCategory(self, category: CookingBookCategory) -> None:
        """
        Sets the category which this recipe will appear in the recipe book under.

        Defaults to {@link CookingBookCategory#MISC} if not set.

        @param category recipe book category
        """
        ...
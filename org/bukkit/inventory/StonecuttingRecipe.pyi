from collections.abc import Iterable
from typing import List, Optional

from org.bukkit import Keyed, Material, NamespacedKey
from org.bukkit.inventory import ItemStack, Recipe, RecipeChoice
from com.google.common.base import Preconditions


class StonecuttingRecipe(Recipe, Keyed):
    """
    Represents a Stonecutting recipe.
    """

    def __init__(self, key: NamespacedKey, result: ItemStack, source: Material) -> None:
        """
        Create a Stonecutting recipe to craft the specified ItemStack.

        :param key: The unique recipe key
        :param result: The item you want the recipe to create.
        :param source: The input material.
        """
        ...

    def __init__(self, key: NamespacedKey, result: ItemStack, input: RecipeChoice) -> None:
        """
        Create a cooking recipe to craft the specified ItemStack.

        :param key: The unique recipe key
        :param result: The item you want the recipe to create.
        :param input: The input choices.
        """
        ...

    def set_input(self, input: Material) -> 'StonecuttingRecipe':
        """
        Sets the input of this cooking recipe.

        :param input: The input material.
        :return: The changed recipe, so you can chain calls.
        """
        ...

    def get_input(self) -> ItemStack:
        """
        Get the input material.

        :return: The input material.
        """
        ...

    def set_input_choice(self, input: RecipeChoice) -> 'StonecuttingRecipe':
        """
        Sets the input of this cooking recipe.

        :param input: The input choice.
        :return: The changed recipe, so you can chain calls.
        """
        ...

    def get_input_choice(self) -> RecipeChoice:
        """
        Get the input choice.

        :return: The input choice.
        """
        ...

    def get_result(self) -> ItemStack:
        """
        Get the result of this recipe.

        :return: The resulting stack.
        """
        ...

    def get_key(self) -> NamespacedKey:
        """
        Get the key for this recipe.

        :return: The key for this recipe.
        """
        ...

    def get_group(self) -> str:
        """
        Get the group of this recipe. Recipes with the same group may be grouped
        together when displayed in the client.

        :return: recipe group. An empty string denotes no group. May not be null.
        """
        ...

    def set_group(self, group: str) -> None:
        """
        Set the group of this recipe. Recipes with the same group may be grouped
        together when displayed in the client.

        :param group: recipe group. An empty string denotes no group. May not be
        null.
        """
        ...
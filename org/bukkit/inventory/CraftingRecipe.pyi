from typing import Any
from org.bukkit import Keyed
from org.bukkit import Material
from org.bukkit import NamespacedKey
from org.bukkit.inventory import ItemStack
from org.bukkit.inventory.recipe import CraftingBookCategory
from com.google.common.base import Preconditions
from org.jetbrains.annotations import ApiStatus
from org.jetbrains.annotations import NotNull

"""
Represents a shaped or shapeless crafting recipe.
"""
class CraftingRecipe(Keyed):
    key: NamespacedKey
    output: ItemStack
    group: str = ""
    category: CraftingBookCategory = CraftingBookCategory.MISC

    def __init__(self, key: NamespacedKey, result: ItemStack) -> None:
        """
        Initializes a new crafting recipe.

        :param key: The namespaced key for this recipe.
        :param result: The result item stack of this recipe.
        """
        ...

        def getKey(self) -> NamespacedKey:
        """
        Get the key of this recipe.

        :return: The namespaced key.
        """
        ...

    """
    Get the result of this recipe.

    :return: The result stack.
    """
        def getResult(self) -> ItemStack:
        ...

    """
    Get the group of this recipe. Recipes with the same group may be grouped
    together when displayed in the client.

    :return: recipe group. An empty string denotes no group. May not be null.
    """
        def getGroup(self) -> str:
        ...

    """
    Set the group of this recipe. Recipes with the same group may be grouped
    together when displayed in the client.

    :param group: recipe group. An empty string denotes no group. May not be
    null.
    """
    def setGroup(self, group: str) -> None:
        ...

    """
    Gets the category which this recipe will appear in the recipe book under.
    <br>
    Defaults to {@link CraftingBookCategory#MISC} if not set.

    :return: recipe book category
    """
        def getCategory(self) -> CraftingBookCategory:
        ...

    """
    Sets the category which this recipe will appear in the recipe book under.
    <br>
    Defaults to {@link CraftingBookCategory#MISC} if not set.

    :param category: recipe book category
    """
    def setCategory(self, category: CraftingBookCategory) -> None:
        ...

    """
    Checks an ItemStack to be used in constructors related to CraftingRecipe
    is not empty.

    :param result: an ItemStack
    :return: the same result ItemStack
    :raises IllegalArgumentException: if the {@code result} is an empty item
    (AIR)
    """
            @staticmethod
    def checkResult(result: ItemStack) -> ItemStack:
        ...
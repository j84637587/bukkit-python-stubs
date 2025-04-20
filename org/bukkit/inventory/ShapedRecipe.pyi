from collections import HashMap
from typing import Dict, List, Optional

from org.bukkit.Material import Material
from org.bukkit.NamespacedKey import NamespacedKey
from org.bukkit.inventory.CraftingRecipe import CraftingRecipe
from org.bukkit.inventory.ItemStack import ItemStack
from org.bukkit.material.MaterialData import MaterialData
from org.bukkit.inventory.RecipeChoice import RecipeChoice
from com.google.common.base import Preconditions
from org.jetbrains.annotations import NotNull

"""
Represents a shaped (ie normal) crafting recipe.
"""
class ShapedRecipe(CraftingRecipe):
    def __init__(self, result: ItemStack) -> None:
        """
        Create a shaped recipe to craft the specified ItemStack. The
        constructor merely determines the result and type; to set the actual
        recipe, you'll need to call the appropriate methods.

        @param result The item you want the recipe to create.
        @see ShapedRecipe#shape(String...)
        @see ShapedRecipe#setIngredient(char, Material)
        @see ShapedRecipe#setIngredient(char, Material, int)
        @see ShapedRecipe#setIngredient(char, MaterialData)
        @see ShapedRecipe#setIngredient(char, RecipeChoice)
        @deprecated Recipes must have keys. Use {@link #ShapedRecipe(NamespacedKey, ItemStack)}
        instead.
        """
        ...

    def __init__(self, key: NamespacedKey, result: ItemStack) -> None:
        """
        Create a shaped recipe to craft the specified ItemStack. The
        constructor merely determines the result and type; to set the actual
        recipe, you'll need to call the appropriate methods.

        @param key the unique recipe key
        @param result The item you want the recipe to create.
        @exception IllegalArgumentException if the {@code result} is an empty item (AIR)
        @see ShapedRecipe#shape(String...)
        @see ShapedRecipe#setIngredient(char, Material)
        @see ShapedRecipe#setIngredient(char, Material, int)
        @see ShapedRecipe#setIngredient(char, MaterialData)
        @see ShapedRecipe#setIngredient(char, RecipeChoice)
        """
        ...

        def shape(self, shape: List[str]) -> 'ShapedRecipe':
        """
        Set the shape of this recipe to the specified rows. Each character
        represents a different ingredient; excluding space characters, which
        must be empty, exactly what each character represents is set separately.
        The first row supplied corresponds with the upper most part of the recipe
        on the workbench e.g. if all three rows are supplies the first string
        represents the top row on the workbench.

        @param shape The rows of the recipe (up to 3 rows).
        @return The changed recipe, so you can chain calls.
        """
        ...

        def setIngredient(self, key: str, ingredient: MaterialData) -> 'ShapedRecipe':
        """
        Sets the material that a character in the recipe shape refers to.
        <p>
        Note that before an ingredient can be set, the recipe's shape must be defined
        with {@link #shape(String...)}.

        @param key The character that represents the ingredient in the shape.
        @param ingredient The ingredient.
        @return The changed recipe, so you can chain calls.
        @throws IllegalArgumentException if the {@code key} is a space character
        @throws IllegalArgumentException if the {@code key} does not appear in the shape.
        """
        ...

        def setIngredient(self, key: str, ingredient: Material) -> 'ShapedRecipe':
        """
        Sets the material that a character in the recipe shape refers to.
        <p>
        Note that before an ingredient can be set, the recipe's shape must be defined
        with {@link #shape(String...)}.

        @param key The character that represents the ingredient in the shape.
        @param ingredient The ingredient.
        @return The changed recipe, so you can chain calls.
        @throws IllegalArgumentException if the {@code key} is a space character
        @throws IllegalArgumentException if the {@code key} does not appear in the shape.
        """
        ...

        def setIngredient(self, key: str, ingredient: Material, raw: int) -> 'ShapedRecipe':
        """
        Sets the material that a character in the recipe shape refers to.
        <p>
        Note that before an ingredient can be set, the recipe's shape must be defined
        with {@link #shape(String...)}.

        @param key The character that represents the ingredient in the shape.
        @param ingredient The ingredient.
        @param raw The raw material data as an integer.
        @return The changed recipe, so you can chain calls.
        @throws IllegalArgumentException if the {@code key} is a space character
        @throws IllegalArgumentException if the {@code key} does not appear in the shape.
        @deprecated Magic value
        """
        ...

        def setIngredient(self, key: str, ingredient: RecipeChoice) -> 'ShapedRecipe':
        """
        Sets the {@link RecipeChoice} that a character in the recipe shape refers to.
        <p>
        Note that before an ingredient can be set, the recipe's shape must be defined
        with {@link #shape(String...)}.

        @param key The character that represents the ingredient in the shape.
        @param ingredient The ingredient.
        @return The changed recipe, so you can chain calls.
        @throws IllegalArgumentException if the {@code key} is a space character
        @throws IllegalArgumentException if the {@code key} does not appear in the shape.
        """
        ...

        def getIngredientMap(self) -> Dict[str, ItemStack]:
        """
        Get a copy of the ingredients map.

        @return The mapping of character to ingredients.
        """
        ...

        def getChoiceMap(self) -> Dict[str, RecipeChoice]:
        """
        Get a copy of the choice map.

        @return The mapping of character to ingredients.
        """
        ...

        def getShape(self) -> List[str]:
        """
        Get the shape.

        @return The recipe's shape.
        @throws NullPointerException when not set yet
        """
        ...
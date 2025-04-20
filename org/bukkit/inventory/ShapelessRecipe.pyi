from typing import List
from org.bukkit import Material, NamespacedKey
from org.bukkit.inventory import CraftingRecipe
from org.bukkit.inventory import ItemStack
from org.bukkit.material import MaterialData
from org.bukkit.inventory import RecipeChoice
from com.google.common.base import Preconditions
from java.util import ArrayList, Collections, Iterator

class ShapelessRecipe(CraftingRecipe):
    """
    Represents a shapeless recipe, where the arrangement of the ingredients on
    the crafting grid does not matter.
    """
    
    def __init__(self, result: ItemStack) -> None:
        """
        @deprecated(since = "1.12")
        """
        ...

    def __init__(self, key: NamespacedKey, result: ItemStack) -> None:
        """
        Create a shapeless recipe to craft the specified ItemStack. The
        constructor merely determines the result and type; to set the actual
        recipe, you'll need to call the appropriate methods.

        @param key the unique recipe key
        @param result The item you want the recipe to create.
        @exception IllegalArgumentException if the {@code result} is an empty item (AIR)
        @see ShapelessRecipe#addIngredient(Material)
        @see ShapelessRecipe#addIngredient(MaterialData)
        @see ShapelessRecipe#addIngredient(Material,int)
        @see ShapelessRecipe#addIngredient(int,Material)
        @see ShapelessRecipe#addIngredient(int,MaterialData)
        @see ShapelessRecipe#addIngredient(int,Material,int)
        """
        ...

    def addIngredient(self, ingredient: MaterialData) -> 'ShapelessRecipe':
        """
        Adds the specified ingredient.

        @param ingredient The ingredient to add.
        @return The changed recipe, so you can chain calls.
        """
        ...

    def addIngredient(self, ingredient: Material) -> 'ShapelessRecipe':
        """
        Adds the specified ingredient.

        @param ingredient The ingredient to add.
        @return The changed recipe, so you can chain calls.
        """
        ...

    def addIngredient(self, ingredient: Material, rawdata: int) -> 'ShapelessRecipe':
        """
        Adds the specified ingredient.

        @param ingredient The ingredient to add.
        @param rawdata The data value, or -1 to allow any data value.
        @return The changed recipe, so you can chain calls.
        @deprecated Magic value
        """
        ...

    def addIngredient(self, count: int, ingredient: MaterialData) -> 'ShapelessRecipe':
        """
        Adds multiples of the specified ingredient.

        @param count How many to add (can't be more than 9!)
        @param ingredient The ingredient to add.
        @return The changed recipe, so you can chain calls.
        """
        ...

    def addIngredient(self, count: int, ingredient: Material) -> 'ShapelessRecipe':
        """
        Adds multiples of the specified ingredient.

        @param count How many to add (can't be more than 9!)
        @param ingredient The ingredient to add.
        @return The changed recipe, so you can chain calls.
        """
        ...

    def addIngredient(self, count: int, ingredient: Material, rawdata: int) -> 'ShapelessRecipe':
        """
        Adds multiples of the specified ingredient.

        @param count How many to add (can't be more than 9!)
        @param ingredient The ingredient to add.
        @param rawdata The data value, or -1 to allow any data value.
        @return The changed recipe, so you can chain calls.
        @deprecated Magic value
        """
        ...

    def addIngredient(self, ingredient: RecipeChoice) -> 'ShapelessRecipe':
        """
        Adds the specified ingredient.

        @param ingredient The ingredient to add.
        @return The changed recipe, so you can chain calls.
        """
        ...

    def removeIngredient(self, ingredient: RecipeChoice) -> 'ShapelessRecipe':
        """
        Removes an ingredient from the list.

        @param ingredient The ingredient to remove
        @return The changed recipe.
        """
        ...

    def removeIngredient(self, ingredient: Material) -> 'ShapelessRecipe':
        """
        Removes an ingredient from the list. If the ingredient occurs multiple
        times, only one instance of it is removed. Only removes exact matches,
        with a data value of 0.

        @param ingredient The ingredient to remove
        @return The changed recipe.
        """
        ...

    def removeIngredient(self, ingredient: MaterialData) -> 'ShapelessRecipe':
        """
        Removes an ingredient from the list. If the ingredient occurs multiple
        times, only one instance of it is removed. If the data value is -1,
        only ingredients with a -1 data value will be removed.

        @param ingredient The ingredient to remove
        @return The changed recipe.
        """
        ...

    def removeIngredient(self, count: int, ingredient: Material) -> 'ShapelessRecipe':
        """
        Removes multiple instances of an ingredient from the list. If there are
        less instances than specified, all will be removed. Only removes exact
        matches, with a data value of 0.

        @param count The number of copies to remove.
        @param ingredient The ingredient to remove
        @return The changed recipe.
        """
        ...

    def removeIngredient(self, count: int, ingredient: MaterialData) -> 'ShapelessRecipe':
        """
        Removes multiple instances of an ingredient from the list. If there are
        less instances than specified, all will be removed. If the data value
        is -1, only ingredients with a -1 data value will be removed.

        @param count The number of copies to remove.
        @param ingredient The ingredient to remove.
        @return The changed recipe.
        """
        ...

    def removeIngredient(self, ingredient: Material, rawdata: int) -> 'ShapelessRecipe':
        """
        Removes an ingredient from the list. If the ingredient occurs multiple
        times, only one instance of it is removed. If the data value is -1,
        only ingredients with a -1 data value will be removed.

        @param ingredient The ingredient to remove
        @param rawdata The data value;
        @return The changed recipe.
        @deprecated Magic value
        """
        ...

    def removeIngredient(self, count: int, ingredient: Material, rawdata: int) -> 'ShapelessRecipe':
        """
        Removes multiple instances of an ingredient from the list. If there are
        less instances than specified, all will be removed. If the data value
        is -1, only ingredients with a -1 data value will be removed.

        @param count The number of copies to remove.
        @param ingredient The ingredient to remove.
        @param rawdata The data value.
        @return The changed recipe.
        @deprecated Magic value
        """
        ...

    def getIngredientList(self) -> List[ItemStack]:
        """
        Get the list of ingredients used for this recipe.

        @return The input list
        """
        ...

    def getChoiceList(self) -> List[RecipeChoice]:
        """
        @return The choice list
        """
        ...
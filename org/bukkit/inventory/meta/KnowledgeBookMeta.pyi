from typing import List
from org.bukkit import NamespacedKey
from org.bukkit.inventory.meta import ItemMeta

class KnowledgeBookMeta(ItemMeta):
    """
    Checks for the existence of recipes in the book.
    
    @return true if the book has recipes
    """
    def has_recipes(self) -> bool: ...

    """
    Gets all the recipes in the book.
    
    @return list of all the recipes in the book
    """
    def get_recipes(self) -> List[NamespacedKey]: ...

    """
    Clears the existing book recipes, and sets the book to use the provided
    recipes.
    
    @param recipes A list of recipes to set the book to use
    """
    def set_recipes(self, recipes: List[NamespacedKey]) -> None: ...

    """
    Adds new recipe to the end of the book.
    
    @param recipes A list of recipe keys
    """
    def add_recipe(self, *recipes: NamespacedKey) -> None: ...

    """
    @return a clone of the KnowledgeBookMeta
    """
    def clone(self) -> 'KnowledgeBookMeta': ...
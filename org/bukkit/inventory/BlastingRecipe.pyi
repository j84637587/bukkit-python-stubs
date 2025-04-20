from org.bukkit import Material
from org.bukkit import NamespacedKey
from org.jetbrains.annotations import NotNull
from org.bukkit.inventory import CookingRecipe
from org.bukkit.inventory import ItemStack
from org.bukkit.inventory import RecipeChoice

"""
Represents a campfire recipe.
"""
class BlastingRecipe(CookingRecipe['BlastingRecipe']):
    
    def __init__(self, key: NotNull[NamespacedKey], result: NotNull[ItemStack], source: NotNull[Material], experience: float, cooking_time: int) -> None:
        ...

    def __init__(self, key: NotNull[NamespacedKey], result: NotNull[ItemStack], input: NotNull[RecipeChoice], experience: float, cooking_time: int) -> None:
        ...
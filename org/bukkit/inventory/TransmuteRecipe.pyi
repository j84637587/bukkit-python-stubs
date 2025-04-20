from org.bukkit.Material import Material
from org.bukkit.NamespacedKey import NamespacedKey
from org.jetbrains.annotations import NotNull
from org.bukkit.inventory import CraftingRecipe, ComplexRecipe, RecipeChoice, ItemStack

"""
Represents a recipe which will change the type of the input material when
combined with an additional material, but preserve all custom data. Only the
item type of the result stack will be used.
<br>
Used for dyeing shulker boxes in Vanilla.
"""
class TransmuteRecipe(CraftingRecipe, ComplexRecipe):
    input: RecipeChoice
    material: RecipeChoice

    """
    Create a transmute recipe to produce a result of the specified type.

    @param key the unique recipe key
    @param result the transmuted result item
    @param input the input ingredient
    @param material the additional ingredient
    """
    def __init__(self, key: NotNull[NamespacedKey], result: NotNull[ItemStack], input: NotNull[RecipeChoice], material: NotNull[RecipeChoice]) -> None:
        ...

    """
    Create a transmute recipe to produce a result of the specified type.

    @param key the unique recipe key
    @param result the transmuted result material
    @param input the input ingredient
    @param material the additional ingredient
    """
    def __init__(self, key: NotNull[NamespacedKey], result: NotNull[Material], input: NotNull[RecipeChoice], material: NotNull[RecipeChoice]) -> None:
        ...

    """
    Gets the input material, which will be transmuted.

    @return the input from transmutation
    """
        def getInput(self) -> RecipeChoice:
        ...

    """
    Gets the additional material required to cause the transmutation.

    @return the ingredient material
    """
        def getMaterial(self) -> RecipeChoice:
        ...
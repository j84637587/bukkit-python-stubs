from org.bukkit.inventory import Recipe
from org.bukkit import Keyed
from org.bukkit import NamespacedKey
from org.jetbrains.annotations import NotNull, Nullable

"""
Represents a smithing recipe.
"""
class SmithingRecipe(Recipe, Keyed):
    key: NamespacedKey
    result: ItemStack
    base: RecipeChoice
    addition: RecipeChoice

    """
    Create a smithing recipe to produce the specified result ItemStack.

    @param key The unique recipe key
    @param result The item you want the recipe to create.
    @param base The base ingredient
    @param addition The addition ingredient
    @deprecated as of Minecraft 1.20, smithing recipes are now separated into two
    distinct recipe types, {@link SmithingTransformRecipe} and {@link SmithingTrimRecipe}.
    This class now acts as a base class to these two classes and will do nothing when
    added to the server.
    """
    @Deprecated(since="1.20.1")
    def __init__(self, key: NotNull[NamespacedKey], result: NotNull[ItemStack], base: Nullable[RecipeChoice], addition: Nullable[RecipeChoice]) -> None:
        ...

    """
    Get the base recipe item.

    @return base choice
    """
    def getBase(self) -> Nullable[RecipeChoice]:
        ...

    """
    Get the addition recipe item.

    @return addition choice
    """
    def getAddition(self) -> Nullable[RecipeChoice]:
        ...

        def getResult(self) -> ItemStack:
        ...

        def getKey(self) -> NamespacedKey:
        ...
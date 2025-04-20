from org.bukkit import Material
from org.bukkit import NamespacedKey
from org.bukkit.inventory import RecipeChoice
from org.bukkit.inventory import SmithingRecipe
from org.bukkit.inventory import ItemStack
from org.bukkit.inventory.meta.trim import TrimPattern
from typing import Optional

class SmithingTrimRecipe(SmithingRecipe):
    """
    Represents a smithing trim recipe.
    """

    def __init__(self, key: NamespacedKey, template: Optional[RecipeChoice], base: Optional[RecipeChoice], addition: Optional[RecipeChoice]) -> None:
        ...

    def __init__(self, key: NamespacedKey, template: Optional[RecipeChoice], base: Optional[RecipeChoice], addition: Optional[RecipeChoice], trim_pattern: TrimPattern) -> None:
        ...

    @staticmethod
    @Deprecated(since="1.21.5")
    def get_trim_pattern(template: Optional[RecipeChoice]) -> TrimPattern:
        """
        Get the trim pattern based on the template choice.

        :param template: The template item choice.
        :return: The corresponding trim pattern.
        """
        ...

    def get_template(self) -> Optional[RecipeChoice]:
        """
        Get the template recipe item.

        :return: template choice
        """
        ...

    def get_trim_pattern(self) -> TrimPattern:
        """
        Get the trim pattern.

        :return: trim pattern
        """
        ...
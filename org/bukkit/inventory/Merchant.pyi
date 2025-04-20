from typing import List, Optional
from org.bukkit.entity import HumanEntity

class Merchant:
    """
    Represents a merchant. A merchant is a special type of inventory which can
    facilitate custom trades between items.
    """

    def get_recipes(self) -> List['MerchantRecipe']:
        """
        Get a list of trades currently available from this merchant.

        :return: an immutable list of trades
        """
        ...

    def set_recipes(self, recipes: List['MerchantRecipe']) -> None:
        """
        Set the list of trades currently available from this merchant.
        This will not change the selected trades of players currently trading
        with this merchant.

        :param recipes: a list of recipes
        """
        ...

    def get_recipe(self, i: int) -> 'MerchantRecipe':
        """
        Get the recipe at a certain index of this merchant's trade list.

        :param i: the index
        :return: the recipe
        :raises IndexError: if recipe index out of bounds
        """
        ...

    def set_recipe(self, i: int, recipe: 'MerchantRecipe') -> None:
        """
        Set the recipe at a certain index of this merchant's trade list.

        :param i: the index
        :param recipe: the recipe
        :raises IndexError: if recipe index out of bounds
        """
        ...

    def get_recipe_count(self) -> int:
        """
        Get the number of trades this merchant currently has available.

        :return: the recipe count
        """
        ...

    def is_trading(self) -> bool:
        """
        Gets whether this merchant is currently trading.

        :return: whether the merchant is trading
        """
        ...

    def get_trader(self) -> Optional[HumanEntity]:
        """
        Gets the player this merchant is trading with, or None if it is not
        currently trading.

        :return: the trader, or None
        """
        ...
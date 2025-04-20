from typing import Any
from org.bukkit.enchantments import Enchantment

class EnchantmentOffer:
    """
    A class for the available enchantment offers in the enchantment table.
    """

    def __init__(self, enchantment: Enchantment, enchantment_level: int, cost: int) -> None:
        """
        Initialize an EnchantmentOffer.

        :param enchantment: type of the enchantment
        :param enchantment_level: level of the enchantment
        :param cost: cost for this enchantment
        """
        ...

    def get_enchantment(self) -> Enchantment:
        """
        Get the type of the enchantment.

        :return: type of enchantment
        """
        ...

    def set_enchantment(self, enchantment: Enchantment) -> None:
        """
        Sets the type of the enchantment.

        :param enchantment: type of the enchantment
        """
        ...

    def get_enchantment_level(self) -> int:
        """
        Gets the level of the enchantment.

        :return: level of the enchantment
        """
        ...

    def set_enchantment_level(self, enchantment_level: int) -> None:
        """
        Sets the level of the enchantment.

        :param enchantment_level: level of the enchantment
        """
        ...

    def get_cost(self) -> int:
        """
        Gets the cost (minimum level) which is displayed as a number on the right
        hand side of the enchantment offer.

        :return: cost for this enchantment
        """
        ...

    def set_cost(self, cost: int) -> None:
        """
        Sets the cost (minimum level) which is displayed as a number on the right
        hand side of the enchantment offer.

        :param cost: cost for this enchantment
        """
        ...
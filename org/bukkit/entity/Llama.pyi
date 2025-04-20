from org.bukkit.entity import ChestedHorse
from org.bukkit.inventory import LlamaInventory
from typing import Literal

class Llama(ChestedHorse):
    """
    Represents a Llama.
    """

    class Color:
        """
        Represents the base color that the llama has.
        """
        CREAMY: Literal['CREAMY']
        WHITE: Literal['WHITE']
        BROWN: Literal['BROWN']
        GRAY: Literal['GRAY']

    def get_color(self) -> Color:
        """
        Gets the llama's color.

        Returns:
            Color: a Color representing the llama's color
        """
        ...

    def set_color(self, color: Color) -> None:
        """
        Sets the llama's color.

        Args:
            color (Color): a Color for this llama
        """
        ...

    def get_strength(self) -> int:
        """
        Gets the llama's strength. A higher strength llama will have more
        inventory slots and be more threatening to entities.

        Returns:
            int: llama strength [1,5]
        """
        ...

    def set_strength(self, strength: int) -> None:
        """
        Sets the llama's strength. A higher strength llama will have more
        inventory slots and be more threatening to entities. Inventory slots are
        equal to strength * 3.

        Args:
            strength (int): llama strength [1,5]
        """
        ...

    def get_inventory(self) -> LlamaInventory:
        """
        Overrides the method from ChestedHorse to get the llama's inventory.

        Returns:
            LlamaInventory: the llama's inventory
        """
        ...
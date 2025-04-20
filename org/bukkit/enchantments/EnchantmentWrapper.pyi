from typing import Type
from org.bukkit.enchantments import Enchantment

class EnchantmentWrapper(Enchantment):
    """
    A simple wrapper for ease of selecting {@link Enchantment}s
    @deprecated only for backwards compatibility, EnchantmentWrapper is no longer used.
    """
    
    def __init__(self) -> None:
        """Initializes the EnchantmentWrapper."""
        ...

    def get_enchantment(self) -> Type[Enchantment]:
        """
        Gets the enchantment bound to this wrapper

        @return Enchantment
        """
        ...
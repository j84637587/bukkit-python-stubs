from org.bukkit.inventory.meta import ItemMeta
from typing import Protocol

class OminousBottleMeta(ItemMeta, Protocol):
    """
    Represents a map that can be scalable.
    """

    def has_amplifier(self) -> bool:
        """
        Checks for the presence of an amplifier.

        :return: true if a customer amplifier is applied
        """
        ...

    def get_amplifier(self) -> int:
        """
        Gets the amplifier amount for an Ominous Bottle's bad omen effect.
        Plugins should check that has_amplifier() returns true before calling this
        method.

        :return: amplifier
        """
        ...

    def set_amplifier(self, amplifier: int) -> None:
        """
        Sets the amplifier amount for an Ominous Bottle's bad omen effect.

        :param amplifier: between 0 and 4
        """
        ...

    def clone(self) -> 'OminousBottleMeta':
        ...
from org.bukkit.DyeColor import DyeColor
from org.bukkit.Keyed import Keyed
from org.bukkit.NamespacedKey import NamespacedKey
from org.bukkit.Registry import Registry
from org.bukkit.registry.RegistryAware import RegistryAware
from typing import Protocol

class Wolf(Protocol):
    """
    Represents a Wolf
    """

    def is_angry(self) -> bool:
        """
        Checks if this wolf is angry

        :return: Anger true if angry
        """
        ...

    def set_angry(self, angry: bool) -> None:
        """
        Sets the anger of this wolf.
        An angry wolf can not be fed or tamed.

        :param angry: true if angry
        :see: set_target(org.bukkit.entity.LivingEntity)
        """
        ...

    def get_collar_color(self) -> DyeColor:
        """
        Get the collar color of this wolf

        :return: the color of the collar
        """
        ...

    def set_collar_color(self, color: DyeColor) -> None:
        """
        Set the collar color of this wolf

        :param color: the color to apply
        """
        ...

    def is_wet(self) -> bool:
        """
        Gets whether the wolf is wet

        :return: Whether the wolf is wet
        """
        ...

    def get_tail_angle(self) -> float:
        """
        Gets the wolf's tail angle in radians

        :return: The angle of the wolf's tail in radians
        """
        ...

    def is_interested(self) -> bool:
        """
        Gets if the wolf is interested

        :return: Whether the wolf is interested
        """
        ...

    def set_interested(self, interested: bool) -> None:
        """
        Set wolf to be interested

        :param interested: Whether the wolf is interested
        """
        ...

    def get_variant(self) -> 'Wolf.Variant':
        """
        Get the variant of this wolf.

        :return: wolf variant
        """
        ...

    def set_variant(self, variant: 'Wolf.Variant') -> None:
        """
        Set the variant of this wolf.

        :param variant: wolf variant
        """
        ...


class Variant(Protocol, Keyed, RegistryAware):
    """
    Represents the variant of a wolf.
    """

    PALE: 'Variant'
    SPOTTED: 'Variant'
    SNOWY: 'Variant'
    BLACK: 'Variant'
    ASHEN: 'Variant'
    RUSTY: 'Variant'
    WOODS: 'Variant'
    CHESTNUT: 'Variant'
    STRIPED: 'Variant'

    @staticmethod
    def get_variant(key: str) -> 'Variant':
        """
        :param key: the key to get the variant
        :return: Variant
        """
        ...

    def get_key(self) -> NamespacedKey:
        """
        :return: the key of the variant
        :see: get_key_or_throw()
        :see: is_registered()
        :deprecated: A key might not always be present, use get_key_or_throw() instead.
        """
        ...
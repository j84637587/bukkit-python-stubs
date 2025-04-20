from typing import Protocol, TypeVar, List
from org.bukkit import DyeColor
from org.bukkit import Keyed
from org.bukkit import NamespacedKey
from org.bukkit import Registry
from org.bukkit.registry import RegistryAware
from org.bukkit.util import OldEnum
from google.common.base import Preconditions
import locale

T = TypeVar('T', bound='Cat.Type')

class Cat(Protocol):
    """
    Meow.
    """

    def get_cat_type(self) -> T:
        """
        Gets the current type of this cat.

        Returns:
            Type of the cat.
        """
        ...

    def set_cat_type(self, type: T) -> None:
        """
        Sets the current type of this cat.

        Args:
            type: New type of this cat.
        """
        ...

    def get_collar_color(self) -> DyeColor:
        """
        Get the collar color of this cat.

        Returns:
            the color of the collar.
        """
        ...

    def set_collar_color(self, color: DyeColor) -> None:
        """
        Set the collar color of this cat.

        Args:
            color: the color to apply.
        """
        ...

class Type(OldEnum[T], Keyed, RegistryAware, Protocol):
    """
    Represents the various different cat types there are.
    """

    TABBY: T
    BLACK: T
    RED: T
    SIAMESE: T
    BRITISH_SHORTHAIR: T
    CALICO: T
    PERSIAN: T
    RAGDOLL: T
    WHITE: T
    JELLIE: T
    ALL_BLACK: T

    @staticmethod
    def get_type(key: str) -> T:
        """
        Get the type by key.

        Args:
            key: The key of the cat type.

        Returns:
            The cat type.
        """
        return Registry.CAT_VARIANT.get_or_throw(NamespacedKey.minecraft(key))

    def get_key(self) -> NamespacedKey:
        """
        {@inheritDoc}

        Returns:
            The key of the cat type.
        """
        ...

    @staticmethod
    def value_of(name: str) -> T:
        """
        Get the cat type with the given name.

        Args:
            name: Name of the cat type.

        Returns:
            The cat type with the given name.
        """
        ...

    @staticmethod
    def values() -> List[T]:
        """
        Get an array of all known cat types.

        Returns:
            An array of all known cat types.
        """
        ...
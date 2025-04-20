from typing import Optional, Protocol, runtime_checkable
from org.bukkit.entity import Animals
from org.bukkit import Keyed, NamespacedKey, Registry
from org.bukkit.registry import RegistryAware
from org.bukkit.util import OldEnum
import locale

"""
A Frog.
"""
@runtime_checkable
class Frog(Animals, Protocol):
    """
    Gets the tongue target of this frog.

    @return tongue target or None if not set
    """
    def get_tongue_target(self) -> Optional['Entity']:
        ...

    """
    Sets the tongue target of this frog.

    @param target tongue target or None to clear
    """
    def set_tongue_target(self, target: Optional['Entity']) -> None:
        ...

    """
    Get the variant of this frog.

    @return frog variant
    """
    def get_variant(self) -> 'Frog.Variant':
        ...

    """
    Set the variant of this frog.

    @param variant frog variant
    """
    def set_variant(self, variant: 'Frog.Variant') -> None:
        ...


class Variant(OldEnum['Variant'], Keyed, RegistryAware, Protocol):
    """
    Temperate (brown-orange) frog.
    """
    TEMPERATE: 'Variant'
    """
    Warm (gray) frog.
    """
    WARM: 'Variant'
    """
    Cold (green) frog.
    """
    COLD: 'Variant'

    @staticmethod
    def get_variant(key: str) -> 'Variant':
        ...

    """
    {@inheritDoc}

    @see #get_key_or_throw()
    @see #is_registered()
    @deprecated A key might not always be present, use {@link #get_key_or_throw()} instead.
    """
    def get_key(self) -> NamespacedKey:
        ...

    """
    @param name of the frog variant.
    @return the frog variant with the given name.
    @deprecated only for backwards compatibility, use {@link Registry#get(NamespacedKey)} instead.
    """
    @staticmethod
    def value_of(name: str) -> 'Variant':
        ...

    """
    @return an array of all known frog variants.
    @deprecated use {@link Registry#iterator()}.
    """
    @staticmethod
    def values() -> list['Variant']:
        ...
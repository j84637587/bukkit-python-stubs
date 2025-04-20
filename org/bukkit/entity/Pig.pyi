from org.bukkit import Keyed
from org.bukkit import NamespacedKey
from org.bukkit import Registry
from org.bukkit.registry import RegistryAware
from typing import Protocol

class Pig(Protocol):
    """
    Represents a Pig.
    """

    def get_variant(self) -> Variant:
        """
        Get the variant of this pig.

        Returns:
            pig variant
        """
        ...

    def set_variant(self, variant: Variant) -> None:
        """
        Set the variant of this pig.

        Args:
            variant: pig variant
        """
        ...

class Variant(Protocol, Keyed, RegistryAware):
    TEMPERATE: Variant
    WARM: Variant
    COLD: Variant

    def get_key(self) -> NamespacedKey:
        """
        {@inheritDoc}

        @see #getKeyOrThrow()
        @see #isRegistered()
        @deprecated A key might not always be present, use {@link #getKeyOrThrow()} instead.
        """
        ...

    @staticmethod
    def get_type(key: str) -> Variant:
        """
        Get the variant type by key.

        Args:
            key: The key of the variant.

        Returns:
            The variant associated with the key.
        """
        ...
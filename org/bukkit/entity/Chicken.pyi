from org.bukkit import Keyed
from org.bukkit import NamespacedKey
from org.bukkit import Registry
from org.bukkit.registry import RegistryAware
from typing import Protocol

class Chicken(Protocol):
    """Represents a Chicken."""

    def get_variant(self) -> Variant:
        """Get the variant of this chicken.

        Returns:
            chicken variant
        """
        ...

    def set_variant(self, variant: Variant) -> None:
        """Set the variant of this chicken.

        Args:
            variant: chicken variant
        """
        ...

class Variant(Keyed, RegistryAware, Protocol):
    """Represents the variant of a chicken."""

    TEMPERATE: Variant
    WARM: Variant
    COLD: Variant

    def get_key(self) -> NamespacedKey:
        """{@inheritDoc}

        @see #getKeyOrThrow()
        @see #isRegistered()
        @deprecated A key might not always be present, use {@link #getKeyOrThrow()} instead.
        """
        ...

    @staticmethod
    def get_type(key: str) -> Variant:
        """Get the variant type by key.

        Args:
            key: The key of the variant.

        Returns:
            The variant corresponding to the key.
        """
        ...
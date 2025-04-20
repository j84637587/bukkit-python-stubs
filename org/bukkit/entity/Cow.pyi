from org.bukkit import Keyed
from org.bukkit import NamespacedKey
from org.bukkit import Registry
from org.bukkit.registry import RegistryAware
from typing import Protocol

class Cow(Protocol):
    """Represents a regular Cow."""

    def get_variant(self) -> Variant:
        """Get the variant of this cow.

        Returns:
            cow variant
        """
        ...

    def set_variant(self, variant: Variant) -> None:
        """Set the variant of this cow.

        Args:
            variant: cow variant
        """
        ...

class Variant(Keyed, RegistryAware, Protocol):
    """Represents the variant of a cow."""

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
        """Get the variant type by key."""
        ...
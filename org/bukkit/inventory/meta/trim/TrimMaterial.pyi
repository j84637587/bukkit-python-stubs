from org.bukkit import Keyed
from org.bukkit import Material
from org.bukkit import NamespacedKey
from org.bukkit import Registry
from org.bukkit import Translatable
from org.bukkit.registry import RegistryAware
from typing import Protocol, runtime_checkable

@runtime_checkable
class TrimMaterial(Protocol, Keyed, Translatable, RegistryAware):
    """
    Represents a material that may be used in an {@link ArmorTrim}.
    """

    QUARTZ: 'TrimMaterial'
    IRON: 'TrimMaterial'
    NETHERITE: 'TrimMaterial'
    REDSTONE: 'TrimMaterial'
    COPPER: 'TrimMaterial'
    GOLD: 'TrimMaterial'
    EMERALD: 'TrimMaterial'
    DIAMOND: 'TrimMaterial'
    LAPIS: 'TrimMaterial'
    AMETHYST: 'TrimMaterial'
    RESIN: 'TrimMaterial'

    @staticmethod
    def get_trim_material(key: str) -> 'TrimMaterial':
        """
        Retrieves a TrimMaterial by its key.

        @param key: The key of the TrimMaterial.
        @return: The corresponding TrimMaterial.
        """
        ...

    @Deprecated(since="1.21.4")
    def get_key(self) -> NamespacedKey:
        """
        {@inheritDoc}

        @see #getKeyOrThrow()
        @see #isRegistered()
        @deprecated A key might not always be present, use {@link #getKeyOrThrow()} instead.
        """
        ...
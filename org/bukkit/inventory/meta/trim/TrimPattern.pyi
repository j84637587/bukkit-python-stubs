from org.bukkit import Keyed
from org.bukkit import Material
from org.bukkit import NamespacedKey
from org.bukkit import Registry
from org.bukkit import Translatable
from org.bukkit.registry import RegistryAware
from typing import Protocol

class TrimPattern(Protocol, Keyed, Translatable, RegistryAware):
    """
    Represents a pattern that may be used in an {@link ArmorTrim}.
    """

    SENTRY: 'TrimPattern'
    DUNE: 'TrimPattern'
    COAST: 'TrimPattern'
    WILD: 'TrimPattern'
    WARD: 'TrimPattern'
    EYE: 'TrimPattern'
    VEX: 'TrimPattern'
    TIDE: 'TrimPattern'
    SNOUT: 'TrimPattern'
    RIB: 'TrimPattern'
    SPIRE: 'TrimPattern'
    WAYFINDER: 'TrimPattern'
    SHAPER: 'TrimPattern'
    SILENCE: 'TrimPattern'
    RAISER: 'TrimPattern'
    HOST: 'TrimPattern'
    FLOW: 'TrimPattern'
    BOLT: 'TrimPattern'

    @staticmethod
    def get_trim_pattern(key: str) -> 'TrimPattern':
        """
        {@link Material#SENTRY_ARMOR_TRIM_SMITHING_TEMPLATE}.
        """
        ...

    def get_key(self) -> NamespacedKey:
        """
        {@inheritDoc}
        
        @see #getKeyOrThrow()
        @see #isRegistered()
        @deprecated A key might not always be present, use {@link #getKeyOrThrow()} instead.
        """
        ...
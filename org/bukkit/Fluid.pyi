from typing import List
from org.bukkit import NamespacedKey, Registry
from org.bukkit.util import OldEnum
from org.bukkit.registry import RegistryAware

class Fluid(OldEnum, RegistryAware):
    """
    Represents a fluid type.
    """
    EMPTY: 'Fluid'
    WATER: 'Fluid'
    FLOWING_WATER: 'Fluid'
    LAVA: 'Fluid'
    FLOWING_LAVA: 'Fluid'

    @staticmethod
    def getFluid(key: str) -> 'Fluid':
        """
        Private method to get fluid.
        """
        pass

    def getKey(self) -> NamespacedKey:
        """
        {@inheritDoc}

        @see #getKeyOrThrow()
        @see #isRegistered()
        @deprecated A key might not always be present, use {@link #getKeyOrThrow()} instead.
        """
        pass

    @staticmethod
    def valueOf(name: str) -> 'Fluid':
        """
        @param name of the fluid.
        @return the fluid with the given name.
        @deprecated only for backwards compatibility, use {@link Registry#get(NamespacedKey)} instead.
        """
        pass

    @staticmethod
    def values() -> List['Fluid']:
        """
        @return an array of all known fluids.
        @deprecated use {@link Registry#iterator()}.
        """
        pass
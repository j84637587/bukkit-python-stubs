from typing import List, Protocol
from org.bukkit import Bukkit, FeatureFlag, NamespacedKey, Registry
from org.bukkit.util import OldEnum

class Biome(OldEnum, Protocol):
    """
    Holds all accepted Biomes in the server.
    The Biomes listed in this interface are present in the default server
    or can be enabled via a {@link FeatureFlag}.
    There may be additional biomes present in the server, for example from a {@link DataPack}
    which can be accessed via {@link Registry#BIOME}.
    """
    
    OCEAN: 'Biome'
    PLAINS: 'Biome'
    DESERT: 'Biome'
    WINDSWEPT_HILLS: 'Biome'
    FOREST: 'Biome'
    TAIGA: 'Biome'
    SWAMP: 'Biome'
    MANGROVE_SWAMP: 'Biome'
    RIVER: 'Biome'
    NETHER_WASTES: 'Biome'
    THE_END: 'Biome'
    FROZEN_OCEAN: 'Biome'
    FROZEN_RIVER: 'Biome'
    SNOWY_PLAINS: 'Biome'
    MUSHROOM_FIELDS: 'Biome'
    BEACH: 'Biome'
    JUNGLE: 'Biome'
    SPARSE_JUNGLE: 'Biome'
    DEEP_OCEAN: 'Biome'
    STONY_SHORE: 'Biome'
    SNOWY_BEACH: 'Biome'
    BIRCH_FOREST: 'Biome'
    DARK_FOREST: 'Biome'
    PALE_GARDEN: 'Biome'
    SNOWY_TAIGA: 'Biome'
    OLD_GROWTH_PINE_TAIGA: 'Biome'
    WINDSWEPT_FOREST: 'Biome'
    SAVANNA: 'Biome'
    SAVANNA_PLATEAU: 'Biome'
    BADLANDS: 'Biome'
    WOODED_BADLANDS: 'Biome'
    SMALL_END_ISLANDS: 'Biome'
    END_MIDLANDS: 'Biome'
    END_HIGHLANDS: 'Biome'
    END_BARRENS: 'Biome'
    WARM_OCEAN: 'Biome'
    LUKEWARM_OCEAN: 'Biome'
    COLD_OCEAN: 'Biome'
    DEEP_LUKEWARM_OCEAN: 'Biome'
    DEEP_COLD_OCEAN: 'Biome'
    DEEP_FROZEN_OCEAN: 'Biome'
    THE_VOID: 'Biome'
    SUNFLOWER_PLAINS: 'Biome'
    WINDSWEPT_GRAVELLY_HILLS: 'Biome'
    FLOWER_FOREST: 'Biome'
    ICE_SPIKES: 'Biome'
    OLD_GROWTH_BIRCH_FOREST: 'Biome'
    OLD_GROWTH_SPRUCE_TAIGA: 'Biome'
    WINDSWEPT_SAVANNA: 'Biome'
    ERODED_BADLANDS: 'Biome'
    BAMBOO_JUNGLE: 'Biome'
    SOUL_SAND_VALLEY: 'Biome'
    CRIMSON_FOREST: 'Biome'
    WARPED_FOREST: 'Biome'
    BASALT_DELTAS: 'Biome'
    DRIPSTONE_CAVES: 'Biome'
    LUSH_CAVES: 'Biome'
    DEEP_DARK: 'Biome'
    MEADOW: 'Biome'
    GROVE: 'Biome'
    SNOWY_SLOPES: 'Biome'
    FROZEN_PEAKS: 'Biome'
    JAGGED_PEAKS: 'Biome'
    STONY_PEAKS: 'Biome'
    CHERRY_GROVE: 'Biome'

    CUSTOM: 'Biome'

    @staticmethod
    def get_biome(key: str) -> 'Biome':
        """
        Retrieves a biome by its key.
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

    @staticmethod
    def value_of(name: str) -> 'Biome':
        """
        @param name of the biome.
        @return the biome with the given name.
        @deprecated only for backwards compatibility, use {@link Registry#get(NamespacedKey)} instead.
        """
        ...

    @staticmethod
    def values() -> List['Biome']:
        """
        @return an array of all known biomes.
        @deprecated use {@link Registry#iterator()}.
        """
        ...
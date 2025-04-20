from org.bukkit import Keyed
from org.bukkit import NamespacedKey
from org.bukkit import Registry
from org.bukkit.registry import RegistryAware
from typing import Any

class Structure(Keyed, RegistryAware):
    """
    Represent a Structure from the world.

    Listed structures are present in the default server. Depending on the server
    there might be additional structures present (for example structures added by
    data packs), which can be received via {@link Registry#STRUCTURE}.
    """

    PILLAGER_OUTPOST: "Structure"
    MINESHAFT: "Structure"
    MINESHAFT_MESA: "Structure"
    MANSION: "Structure"
    JUNGLE_PYRAMID: "Structure"
    DESERT_PYRAMID: "Structure"
    IGLOO: "Structure"
    SHIPWRECK: "Structure"
    SHIPWRECK_BEACHED: "Structure"
    SWAMP_HUT: "Structure"
    STRONGHOLD: "Structure"
    MONUMENT: "Structure"
    OCEAN_RUIN_COLD: "Structure"
    OCEAN_RUIN_WARM: "Structure"
    FORTRESS: "Structure"
    NETHER_FOSSIL: "Structure"
    END_CITY: "Structure"
    BURIED_TREASURE: "Structure"
    BASTION_REMNANT: "Structure"
    VILLAGE_PLAINS: "Structure"
    VILLAGE_DESERT: "Structure"
    VILLAGE_SAVANNA: "Structure"
    VILLAGE_SNOWY: "Structure"
    VILLAGE_TAIGA: "Structure"
    RUINED_PORTAL: "Structure"
    RUINED_PORTAL_DESERT: "Structure"
    RUINED_PORTAL_JUNGLE: "Structure"
    RUINED_PORTAL_SWAMP: "Structure"
    RUINED_PORTAL_MOUNTAIN: "Structure"
    RUINED_PORTAL_OCEAN: "Structure"
    RUINED_PORTAL_NETHER: "Structure"
    ANCIENT_CITY: "Structure"
    TRAIL_RUINS: "Structure"
    TRIAL_CHAMBERS: "Structure"

    @staticmethod
    def get_structure(name: str) -> "Structure":
        """
        Retrieves a structure by its name.

        :param name: The name of the structure.
        :return: The structure associated with the given name.
        """
        ...

    def get_structure_type(self) -> "StructureType":
        """
        Returns the type of the structure.

        :return: the type of structure
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
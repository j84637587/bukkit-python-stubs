from org.bukkit import Keyed
from org.bukkit import NamespacedKey
from org.bukkit import Registry
from org.bukkit.registry import RegistryAware
from typing import Final

class StructureType(Keyed, RegistryAware):
    """
    Represent a StructureType of a {@link Structure}.

    Listed structure types are present in the default server. Depending on the
    server there might be additional structure types present (for example
    structure types added by data packs), which can be received via
    {@link Registry#STRUCTURE_TYPE}.
    """

    BURIED_TREASURE: Final[StructureType]
    DESERT_PYRAMID: Final[StructureType]
    END_CITY: Final[StructureType]
    FORTRESS: Final[StructureType]
    IGLOO: Final[StructureType]
    JIGSAW: Final[StructureType]
    JUNGLE_TEMPLE: Final[StructureType]
    MINESHAFT: Final[StructureType]
    NETHER_FOSSIL: Final[StructureType]
    OCEAN_MONUMENT: Final[StructureType]
    OCEAN_RUIN: Final[StructureType]
    RUINED_PORTAL: Final[StructureType]
    SHIPWRECK: Final[StructureType]
    STRONGHOLD: Final[StructureType]
    SWAMP_HUT: Final[StructureType]
    WOODLAND_MANSION: Final[StructureType]

    @staticmethod
    def get_structure_type(name: str) -> StructureType:
        """
        Retrieve a StructureType by its name.

        :param name: The name of the structure type.
        :return: The StructureType associated with the given name.
        """
        return Registry.STRUCTURE_TYPE.getOrThrow(NamespacedKey.minecraft(name))

    @Deprecated(since="1.21.4")
    def get_key(self) -> NamespacedKey:
        """
        {@inheritDoc}

        @see #getKeyOrThrow()
        @see #isRegistered()
        @deprecated A key might not always be present, use {@link #getKeyOrThrow()} instead.
        """
        ...
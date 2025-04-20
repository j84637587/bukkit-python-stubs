from typing import Dict, Optional, Type, TypeVar
from org.bukkit.map import MapCursor
from org.bukkit import NamespacedKey

T = TypeVar('T', bound='StructureType')

class StructureType:
    """
    This class handles the creation and storage of all structure types for
    Bukkit. Structure Types are the different kinds of structures that can be
    generated during world/chunk generation. These include Villages, Mineshafts,
    Mansions, etc.
    The registration of new StructureTypes is case-sensitive.

    @deprecated This class does not represent the structures of a world well. Use
    org.bukkit.generator.structure.Structure or
    org.bukkit.generator.structure.StructureType instead.
    """
    structureTypeMap: Dict[str, 'StructureType'] = {}

    MINESHAFT: 'StructureType'
    VILLAGE: 'StructureType'
    NETHER_FORTRESS: 'StructureType'
    STRONGHOLD: 'StructureType'
    JUNGLE_PYRAMID: 'StructureType'
    OCEAN_RUIN: 'StructureType'
    DESERT_PYRAMID: 'StructureType'
    IGLOO: 'StructureType'
    SWAMP_HUT: 'StructureType'
    OCEAN_MONUMENT: 'StructureType'
    END_CITY: 'StructureType'
    WOODLAND_MANSION: 'StructureType'
    BURIED_TREASURE: 'StructureType'
    SHIPWRECK: 'StructureType'
    PILLAGER_OUTPOST: 'StructureType'
    NETHER_FOSSIL: 'StructureType'
    RUINED_PORTAL: 'StructureType'
    BASTION_REMNANT: 'StructureType'

    key: NamespacedKey
    mapCursor: Optional[MapCursor.Type]

    def __init__(self, name: str, mapIcon: Optional[MapCursor.Type]) -> None:
        """
        Create a new StructureType with a given name and map cursor. To indicate
        this structure should not be compatible with explorer maps, use None for
        mapIcon.
        """
        pass

    def getName(self) -> str:
        """
        Get the name of this structure. This is case-sensitive when used in
        commands.
        """
        pass

    def getMapIcon(self) -> Optional[MapCursor.Type]:
        """
        Get the MapCursor.Type that this structure can use on maps. If
        this is None, this structure will not appear on explorer maps.
        """
        pass

    def equals(self, other: object) -> bool:
        pass

    def hashCode(self) -> int:
        pass

    def toString(self) -> str:
        pass

    @staticmethod
    def register(type: T) -> T:
        pass

    @staticmethod
    def getStructureTypes() -> Dict[str, 'StructureType']:
        """
        Get all registered StructureTypes.
        """
        pass

    def getKey(self) -> NamespacedKey:
        pass
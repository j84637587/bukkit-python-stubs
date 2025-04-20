from typing import List, Map, Set, Optional, Any

from org.bukkit.configuration import ConfigurationSection
from org.bukkit.configuration import Configuration
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.bukkit.inventory import ItemStack
from org.bukkit import Color
from org.bukkit import Location
from org.bukkit import OfflinePlayer
from org.bukkit.util import Vector
from com.google.common.base import Preconditions
from com.google.common.base import Strings

class MemorySection(ConfigurationSection):
    """
    A type of {@link ConfigurationSection} that is stored in memory.
    """

    def __init__(self) -> None:
        """
        Creates an empty MemorySection for use as a root {@link Configuration}
        section.
        <p>
        Note that calling this without being yourself a {@link Configuration}
        will throw an exception!
        """
        ...

    def __init__(self, parent: ConfigurationSection, path: str) -> None:
        """
        Creates an empty MemorySection with the specified parent and path.

        @param parent Parent section that contains this own section.
        @param path Path that you may access this section from via the root
            {@link Configuration}.
        @throws IllegalArgumentException Thrown is parent or path is null, or
            if parent contains no root Configuration.
        """
        ...

    def getKeys(self, deep: bool) -> Set[str]:
        ...

    def getValues(self, deep: bool) -> Map[str, Any]:
        ...

    def contains(self, path: str) -> bool:
        ...

    def contains(self, path: str, ignoreDefault: bool) -> bool:
        ...

    def isSet(self, path: str) -> bool:
        ...

    def getCurrentPath(self) -> str:
        ...

    def getName(self) -> str:
        ...

    def getRoot(self) -> Optional[Configuration]:
        ...

    def getParent(self) -> Optional[ConfigurationSection]:
        ...

    def addDefault(self, path: str, value: Optional[Any]) -> None:
        ...

    def getDefaultSection(self) -> Optional[ConfigurationSection]:
        ...

    def set(self, path: str, value: Optional[Any]) -> None:
        ...

    def get(self, path: str) -> Optional[Any]:
        ...

    def get(self, path: str, def: Optional[Any]) -> Optional[Any]:
        ...

    def createSection(self, path: str) -> ConfigurationSection:
        ...

    def createSection(self, path: str, map: Map[Any, Any]) -> ConfigurationSection:
        ...

    def getString(self, path: str) -> Optional[str]:
        ...

    def getString(self, path: str, def: Optional[str]) -> Optional[str]:
        ...

    def isString(self, path: str) -> bool:
        ...

    def getInt(self, path: str) -> int:
        ...

    def getInt(self, path: str, def: int) -> int:
        ...

    def isInt(self, path: str) -> bool:
        ...

    def getBoolean(self, path: str) -> bool:
        ...

    def getBoolean(self, path: str, def: bool) -> bool:
        ...

    def isBoolean(self, path: str) -> bool:
        ...

    def getDouble(self, path: str) -> float:
        ...

    def getDouble(self, path: str, def: float) -> float:
        ...

    def isDouble(self, path: str) -> bool:
        ...

    def getLong(self, path: str) -> int:
        ...

    def getLong(self, path: str, def: int) -> int:
        ...

    def isLong(self, path: str) -> bool:
        ...

    def getList(self, path: str) -> Optional[List[Any]]:
        ...

    def getList(self, path: str, def: Optional[List[Any]]) -> Optional[List[Any]]:
        ...

    def isList(self, path: str) -> bool:
        ...

    def getStringList(self, path: str) -> List[str]:
        ...

    def getIntegerList(self, path: str) -> List[int]:
        ...

    def getBooleanList(self, path: str) -> List[bool]:
        ...

    def getDoubleList(self, path: str) -> List[float]:
        ...

    def getFloatList(self, path: str) -> List[float]:
        ...

    def getLongList(self, path: str) -> List[int]:
        ...

    def getByteList(self, path: str) -> List[int]:
        ...

    def getCharacterList(self, path: str) -> List[str]:
        ...

    def getShortList(self, path: str) -> List[int]:
        ...

    def getMapList(self, path: str) -> List[Map[Any, Any]]:
        ...

    def getObject(self, path: str, clazz: type) -> Optional[Any]:
        ...

    def getObject(self, path: str, clazz: type, def: Optional[Any]) -> Optional[Any]:
        ...

    def getSerializable(self, path: str, clazz: type) -> Optional[ConfigurationSerializable]:
        ...

    def getSerializable(self, path: str, clazz: type, def: Optional[ConfigurationSerializable]) -> Optional[ConfigurationSerializable]:
        ...

    def getVector(self, path: str) -> Optional[Vector]:
        ...

    def getVector(self, path: str, def: Optional[Vector]) -> Optional[Vector]:
        ...

    def isVector(self, path: str) -> bool:
        ...

    def getOfflinePlayer(self, path: str) -> Optional[OfflinePlayer]:
        ...

    def getOfflinePlayer(self, path: str, def: Optional[OfflinePlayer]) -> Optional[OfflinePlayer]:
        ...

    def isOfflinePlayer(self, path: str) -> bool:
        ...

    def getItemStack(self, path: str) -> Optional[ItemStack]:
        ...

    def getItemStack(self, path: str, def: Optional[ItemStack]) -> Optional[ItemStack]:
        ...

    def isItemStack(self, path: str) -> bool:
        ...

    def getColor(self, path: str) -> Optional[Color]:
        ...

    def getColor(self, path: str, def: Optional[Color]) -> Optional[Color]:
        ...

    def isColor(self, path: str) -> bool:
        ...

    def getLocation(self, path: str) -> Optional[Location]:
        ...

    def getLocation(self, path: str, def: Optional[Location]) -> Optional[Location]:
        ...

    def isLocation(self, path: str) -> bool:
        ...

    def getConfigurationSection(self, path: str) -> Optional[ConfigurationSection]:
        ...

    def isConfigurationSection(self, path: str) -> bool:
        ...

    def isPrimitiveWrapper(self, input: Optional[Any]) -> bool:
        ...

    def getDefault(self, path: str) -> Optional[Any]:
        ...

    def mapChildrenKeys(self, output: Set[str], section: ConfigurationSection, deep: bool) -> None:
        ...

    def mapChildrenValues(self, output: Map[str, Any], section: ConfigurationSection, deep: bool) -> None:
        ...

    @staticmethod
    def createPath(section: ConfigurationSection, key: Optional[str]) -> str:
        ...

    @staticmethod
    def createPath(section: ConfigurationSection, key: Optional[str], relativeTo: Optional[ConfigurationSection]) -> str:
        ...

    def getComments(self, path: str) -> List[str]:
        ...

    def getInlineComments(self, path: str) -> List[str]:
        ...

    def setComments(self, path: str, comments: Optional[List[str]]) -> None:
        ...

    def setInlineComments(self, path: str, comments: Optional[List[str]]) -> None:
        ...

    def getSectionPathData(self, path: str) -> Optional['SectionPathData']:
        ...

    def __str__(self) -> str:
        ...
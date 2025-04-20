from typing import Any, Dict, Optional, Union
from org.bukkit import World, Chunk, Block, Vector, Bukkit
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.bukkit.util import NumberConversions

class Location(ConfigurationSerializable):
    """
    Represents a 3-dimensional position in a world.
    No constraints are placed on any angular values other than that they be
    specified in degrees. This means that negative angles or angles of greater
    magnitude than 360 are valid, but may be normalized to any other equivalent
    representation by the implementation.
    """
    world: Optional[World]
    x: float
    y: float
    z: float
    pitch: float
    yaw: float

    def __init__(self, world: Optional[World], x: float, y: float, z: float, yaw: float = 0, pitch: float = 0) -> None:
        ...

    def setWorld(self, world: Optional[World]) -> None:
        ...

    def isWorldLoaded(self) -> bool:
        ...

    def getWorld(self) -> Optional[World]:
        ...

    def getChunk(self) -> Chunk:
        ...

    def getBlock(self) -> Block:
        ...

    def setX(self, x: float) -> None:
        ...

    def getX(self) -> float:
        ...

    def getBlockX(self) -> int:
        ...

    def setY(self, y: float) -> None:
        ...

    def getY(self) -> float:
        ...

    def getBlockY(self) -> int:
        ...

    def setZ(self, z: float) -> None:
        ...

    def getZ(self) -> float:
        ...

    def getBlockZ(self) -> int:
        ...

    def setYaw(self, yaw: float) -> None:
        ...

    def getYaw(self) -> float:
        ...

    def setPitch(self, pitch: float) -> None:
        ...

    def getPitch(self) -> float:
        ...

    def getDirection(self) -> Vector:
        ...

    def setDirection(self, vector: Vector) -> 'Location':
        ...

    def add(self, vec: Union['Location', Vector]) -> 'Location':
        ...

    def add(self, x: float, y: float, z: float) -> 'Location':
        ...

    def subtract(self, vec: Union['Location', Vector]) -> 'Location':
        ...

    def subtract(self, x: float, y: float, z: float) -> 'Location':
        ...

    def length(self) -> float:
        ...

    def lengthSquared(self) -> float:
        ...

    def distance(self, o: 'Location') -> float:
        ...

    def distanceSquared(self, o: 'Location') -> float:
        ...

    def multiply(self, m: float) -> 'Location':
        ...

    def zero(self) -> 'Location':
        ...

    def equals(self, obj: Any) -> bool:
        ...

    def hashCode(self) -> int:
        ...

    def toString(self) -> str:
        ...

    def toVector(self) -> Vector:
        ...

    def clone(self) -> 'Location':
        ...

    def checkFinite(self) -> None:
        ...

    @staticmethod
    def locToBlock(loc: float) -> int:
        ...

    def serialize(self) -> Dict[str, Any]:
        ...

    @staticmethod
    def deserialize(args: Dict[str, Any]) -> 'Location':
        ...

    @staticmethod
    def normalizeYaw(yaw: float) -> float:
        ...

    @staticmethod
    def normalizePitch(pitch: float) -> float:
        ...
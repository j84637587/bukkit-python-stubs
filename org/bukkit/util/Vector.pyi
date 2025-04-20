from typing import Dict, Any
from org.bukkit.Location import Location
from org.bukkit.World import World
from org.bukkit.configuration.serialization import ConfigurationSerializable
from org.bukkit.configuration.serialization import SerializableAs
from org.joml import RoundingMode
from org.joml import Vector3d
from org.joml import Vector3dc
from org.joml import Vector3f
from org.joml import Vector3fc
from org.joml import Vector3i
from org.joml import Vector3ic
from com.google.common.base import Preconditions
from com.google.common.primitives import Doubles
import random

@SerializableAs("Vector")
class Vector(ConfigurationSerializable):
    serialVersionUID: int = -2657651106777219169
    random: random.Random = random.Random()
    epsilon: float = 0.000001

    x: float
    y: float
    z: float

    def __init__(self) -> None:
        """Construct the vector with all components as 0."""
        ...

    def __init__(self, x: int, y: int, z: int) -> None:
        """Construct the vector with provided integer components."""
        ...

    def __init__(self, x: float, y: float, z: float) -> None:
        """Construct the vector with provided double components."""
        ...

    def __init__(self, x: float, y: float, z: float) -> None:
        """Construct the vector with provided float components."""
        ...

    def add(self, vec: 'Vector') -> 'Vector':
        """Adds a vector to this one."""
        ...

    def subtract(self, vec: 'Vector') -> 'Vector':
        """Subtracts a vector from this one."""
        ...

    def multiply(self, vec: 'Vector') -> 'Vector':
        """Multiplies the vector by another."""
        ...

    def divide(self, vec: 'Vector') -> 'Vector':
        """Divides the vector by another."""
        ...

    def copy(self, vec: 'Vector') -> 'Vector':
        """Copies another vector."""
        ...

    def length(self) -> float:
        """Gets the magnitude of the vector."""
        ...

    def lengthSquared(self) -> float:
        """Gets the magnitude of the vector squared."""
        ...

    def distance(self, o: 'Vector') -> float:
        """Get the distance between this vector and another."""
        ...

    def distanceSquared(self, o: 'Vector') -> float:
        """Get the squared distance between this vector and another."""
        ...

    def angle(self, other: 'Vector') -> float:
        """Gets the angle between this vector and another in radians."""
        ...

    def midpoint(self, other: 'Vector') -> 'Vector':
        """Sets this vector to the midpoint between this vector and another."""
        ...

    def getMidpoint(self, other: 'Vector') -> 'Vector':
        """Gets a new midpoint vector between this vector and another."""
        ...

    def multiply(self, m: int) -> 'Vector':
        """Performs scalar multiplication with an integer."""
        ...

    def multiply(self, m: float) -> 'Vector':
        """Performs scalar multiplication with a float."""
        ...

    def multiply(self, m: float) -> 'Vector':
        """Performs scalar multiplication with a double."""
        ...

    def dot(self, other: 'Vector') -> float:
        """Calculates the dot product of this vector with another."""
        ...

    def crossProduct(self, o: 'Vector') -> 'Vector':
        """Calculates the cross product of this vector with another."""
        ...

    def getCrossProduct(self, o: 'Vector') -> 'Vector':
        """Calculates the cross product without mutating the original."""
        ...

    def normalize(self) -> 'Vector':
        """Converts this vector to a unit vector."""
        ...

    def zero(self) -> 'Vector':
        """Zero this vector's components."""
        ...

    def isZero(self) -> bool:
        """Check whether or not each component of this vector is equal to 0."""
        ...

    def normalizeZeros(self) -> 'Vector':
        """Converts each component of value -0.0 to 0.0."""
        ...

    def isInAABB(self, min: 'Vector', max: 'Vector') -> bool:
        """Returns whether this vector is in an axis-aligned bounding box."""
        ...

    def isInSphere(self, origin: 'Vector', radius: float) -> bool:
        """Returns whether this vector is within a sphere."""
        ...

    def isNormalized(self) -> bool:
        """Returns if a vector is normalized."""
        ...

    def rotateAroundX(self, angle: float) -> 'Vector':
        """Rotates the vector around the x axis."""
        ...

    def rotateAroundY(self, angle: float) -> 'Vector':
        """Rotates the vector around the y axis."""
        ...

    def rotateAroundZ(self, angle: float) -> 'Vector':
        """Rotates the vector around the z axis."""
        ...

    def rotateAroundAxis(self, axis: 'Vector', angle: float) -> 'Vector':
        """Rotates the vector around a given arbitrary axis."""
        ...

    def rotateAroundNonUnitAxis(self, axis: 'Vector', angle: float) -> 'Vector':
        """Rotates the vector around a given arbitrary axis."""
        ...

    def getX(self) -> float:
        """Gets the X component."""
        ...

    def getBlockX(self) -> int:
        """Gets the floored value of the X component."""
        ...

    def getY(self) -> float:
        """Gets the Y component."""
        ...

    def getBlockY(self) -> int:
        """Gets the floored value of the Y component."""
        ...

    def getZ(self) -> float:
        """Gets the Z component."""
        ...

    def getBlockZ(self) -> int:
        """Gets the floored value of the Z component."""
        ...

    def setX(self, x: int) -> 'Vector':
        """Set the X component."""
        ...

    def setX(self, x: float) -> 'Vector':
        """Set the X component."""
        ...

    def setX(self, x: float) -> 'Vector':
        """Set the X component."""
        ...

    def setY(self, y: int) -> 'Vector':
        """Set the Y component."""
        ...

    def setY(self, y: float) -> 'Vector':
        """Set the Y component."""
        ...

    def setY(self, y: float) -> 'Vector':
        """Set the Y component."""
        ...

    def setZ(self, z: int) -> 'Vector':
        """Set the Z component."""
        ...

    def setZ(self, z: float) -> 'Vector':
        """Set the Z component."""
        ...

    def setZ(self, z: float) -> 'Vector':
        """Set the Z component."""
        ...

    def equals(self, obj: Any) -> bool:
        """Checks to see if two objects are equal."""
        ...

    def hashCode(self) -> int:
        """Returns a hash code for this vector."""
        ...

    def clone(self) -> 'Vector':
        """Get a new vector."""
        ...

    def toString(self) -> str:
        """Returns this vector's components as x,y,z."""
        ...

    def toLocation(self, world: 'World') -> 'Location':
        """Gets a Location version of this vector with yaw and pitch being 0."""
        ...

    def toLocation(self, world: 'World', yaw: float, pitch: float) -> 'Location':
        """Gets a Location version of this vector."""
        ...

    def toBlockVector(self) -> 'BlockVector':
        """Get the block vector of this vector."""
        ...

    def toVector3f(self) -> 'Vector3f':
        """Get this vector as a JOML Vector3f."""
        ...

    def toVector3d(self) -> 'Vector3d':
        """Get this vector as a JOML Vector3d."""
        ...

    def toVector3i(self, roundingMode: int) -> 'Vector3i':
        """Get this vector as a JOML Vector3i."""
        ...

    def toVector3i(self) -> 'Vector3i':
        """Get this vector as a JOML Vector3i with its components floored."""
        ...

    def checkFinite(self) -> None:
        """Check if each component of this Vector is finite."""
        ...

    @staticmethod
    def getEpsilon() -> float:
        """Get the threshold used for equals()."""
        ...

    @staticmethod
    def getMinimum(v1: 'Vector', v2: 'Vector') -> 'Vector':
        """Gets the minimum components of two vectors."""
        ...

    @staticmethod
    def getMaximum(v1: 'Vector', v2: 'Vector') -> 'Vector':
        """Gets the maximum components of two vectors."""
        ...

    @staticmethod
    def getRandom() -> 'Vector':
        """Gets a random vector with components having a random value between 0 and 1."""
        ...

    @staticmethod
    def fromJOML(vector: 'Vector3f') -> 'Vector':
        """Gets a vector with components that match the provided JOML Vector3f."""
        ...

    @staticmethod
    def fromJOML(vector: 'Vector3d') -> 'Vector':
        """Gets a vector with components that match the provided JOML Vector3d."""
        ...

    @staticmethod
    def fromJOML(vector: 'Vector3i') -> 'Vector':
        """Gets a vector with components that match the provided JOML Vector3i."""
        ...

    @staticmethod
    def fromJOML(vector: 'Vector3fc') -> 'Vector':
        """Gets a vector with components that match the provided JOML Vector3fc."""
        ...

    @staticmethod
    def fromJOML(vector: 'Vector3dc') -> 'Vector':
        """Gets a vector with components that match the provided JOML Vector3dc."""
        ...

    @staticmethod
    def fromJOML(vector: 'Vector3ic') -> 'Vector':
        """Gets a vector with components that match the provided JOML Vector3ic."""
        ...

    def serialize(self) -> Dict[str, Any]:
        """Serialize the vector."""
        ...

    @staticmethod
    def deserialize(args: Dict[str, Any]) -> 'Vector':
        """Deserialize a vector from a dictionary."""
        ...
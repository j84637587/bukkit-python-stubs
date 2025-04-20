from typing import Dict, Any
from org.bukkit.configuration.serialization import SerializableAs
from org.jetbrains.annotations import NotNull
from org.bukkit.util import Vector

@SerializableAs("BlockVector")
class BlockVector(Vector):
    """
    A vector with a hash function that floors the X, Y, Z components, a la
    BlockVector in WorldEdit. BlockVectors can be used in hash sets and
    hash maps. Be aware that BlockVectors are mutable, but it is important
    that BlockVectors are never changed once put into a hash set or hash map.
    """

    def __init__(self) -> None:
        """
        Construct the vector with all components as 0.
        """
        ...

    def __init__(self, vec: NotNull[Vector]) -> None:
        """
        Construct the vector with another vector.

        :param vec: The other vector.
        """
        ...

    def __init__(self, x: int, y: int, z: int) -> None:
        """
        Construct the vector with provided integer components.

        :param x: X component
        :param y: Y component
        :param z: Z component
        """
        ...

    def __init__(self, x: float, y: float, z: float) -> None:
        """
        Construct the vector with provided double components.

        :param x: X component
        :param y: Y component
        :param z: Z component
        """
        ...

    def __init__(self, x: float, y: float, z: float) -> None:
        """
        Construct the vector with provided float components.

        :param x: X component
        :param y: Y component
        :param z: Z component
        """
        ...

    def __eq__(self, obj: Any) -> bool:
        """
        Checks if another object is equivalent.

        :param obj: The other object
        :return: whether the other object is equivalent
        """
        ...

    def __hash__(self) -> int:
        """
        Returns a hash code for this vector.

        :return: hash code
        """
        ...

    def clone(self) -> 'BlockVector':
        """
        Get a new block vector.

        :return: vector
        """
        ...

    @staticmethod
        def deserialize(args: NotNull[Dict[str, Any]]) -> 'BlockVector':
        """
        Deserialize a BlockVector from a map of arguments.

        :param args: The arguments map
        :return: A new BlockVector
        """
        ...
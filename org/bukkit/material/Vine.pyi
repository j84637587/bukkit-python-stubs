from enum import Enum
from typing import List, Union, Optional, Set
from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import MaterialData

class Vine(MaterialData):
    """
    Represents a vine

    @deprecated all usage of MaterialData is deprecated and subject to removal.
    Use {@link org.bukkit.block.data.BlockData}.
    """

    VINE_NORTH: int = 0x4
    VINE_EAST: int = 0x8
    VINE_WEST: int = 0x2
    VINE_SOUTH: int = 0x1
    possibleFaces: Set[BlockFace] = {BlockFace.WEST, BlockFace.NORTH, BlockFace.SOUTH, BlockFace.EAST}

    def __init__(self) -> None:
        super().__init__(Material.LEGACY_VINE)

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    @Deprecated(since="1.6.2")
    def __init__(self, type: Material, data: bytes) -> None:
        super().__init__(type, data)

    """
    @param data the raw data value
    @deprecated Magic value
    """
    @Deprecated(since="1.6.2")
    def __init__(self, data: bytes) -> None:
        super().__init__(Material.LEGACY_VINE, data)

    def __init__(self, *faces: BlockFace) -> None:
        self.__init__(set(faces))

    def __init__(self, faces: Set[BlockFace]) -> None:
        self.__init__(0)
        faces.intersection_update(self.possibleFaces)

        data: bytes = 0

        if BlockFace.WEST in faces:
            data |= self.VINE_WEST

        if BlockFace.NORTH in faces:
            data |= self.VINE_NORTH

        if BlockFace.SOUTH in faces:
            data |= self.VINE_SOUTH

        if BlockFace.EAST in faces:
            data |= self.VINE_EAST

        self.setData(data)

    """
    Check if the vine is attached to the specified face of an adjacent
    block. You can check two faces at once by passing e.g. {@link
    BlockFace#NORTH_EAST}.

    @param face The face to check.
    @return Whether it is attached to that face.
    """
    def isOnFace(self, face: BlockFace) -> bool:
        pass

    """
    Attach the vine to the specified face of an adjacent block.

    @param face The face to attach.
    """
    def putOnFace(self, face: BlockFace) -> None:
        pass

    """
    Detach the vine from the specified face of an adjacent block.

    @param face The face to detach.
    """
    def removeFromFace(self, face: BlockFace) -> None:
        pass

    def __str__(self) -> str:
        pass

    def clone(self) -> 'Vine':
        pass
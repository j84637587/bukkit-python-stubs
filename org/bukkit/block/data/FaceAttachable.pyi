from org.bukkit.block.data import BlockData
from typing import Literal

class FaceAttachable(BlockData):
    """
    'face' represents the face to which a lever or button is stuck.
    <br>
    This is used in conjunction with {@link Directional} to compute the
    orientation of these blocks.
    """

    def get_attached_face(self) -> 'AttachedFace':
        """
        Gets the value of the 'face' property.

        @return: the 'face' value
        """
        ...

    def set_attached_face(self, face: 'AttachedFace') -> None:
        """
        Sets the value of the 'face' property.

        @param face: the new 'face' value
        """
        ...

class AttachedFace:
    """
    The face to which a switch type block is stuck.
    """
    FLOOR: Literal['FLOOR'] = 'FLOOR'
    WALL: Literal['WALL'] = 'WALL'
    CEILING: Literal['CEILING'] = 'CEILING'
from org.bukkit.block.data import Directional
from org.bukkit.block.data import FaceAttachable
from org.bukkit.block.data import Powerable
from org.jetbrains.annotations import NotNull
from typing import Literal

class Switch(Directional, FaceAttachable, Powerable):
    """
    Interface representing a switch block.
    """

        def get_face(self) -> 'Switch.Face':
        """
        Gets the value of the 'face' property.

        Returns:
            the 'face' value

        Deprecated:
            use {@link #getAttachedFace()}
        """
        ...

    def set_face(self, face: 'Switch.Face') -> None:
        """
        Sets the value of the 'face' property.

        Args:
            face: the new 'face' value

        Deprecated:
            use {@link #getAttachedFace()}
        """
        ...

    class Face:
        """
        The face to which a switch type block is stuck.

        Deprecated:
            use {@link AttachedFace}
        """
        FLOOR: Literal['FLOOR'] = 'FLOOR'
        WALL: Literal['WALL'] = 'WALL'
        CEILING: Literal['CEILING'] = 'CEILING'
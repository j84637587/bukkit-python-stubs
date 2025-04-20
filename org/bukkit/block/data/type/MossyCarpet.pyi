from org.bukkit.block import BlockFace
from org.bukkit.block.data import BlockData
from org.jetbrains.annotations import ApiStatus, NotNull

class MossyCarpet(BlockData):
    """
    This class encompasses the 'north', 'east', 'south', 'west', height flags
    which are used to set the height of a face.

    'bottom' denotes whether this is a bottom block.
    """

    def is_bottom(self) -> bool:
        """
        Gets the value of the 'bottom' property.

        @return the 'bottom' value
        """
        ...

    def set_bottom(self, bottom: bool) -> None:
        """
        Sets the value of the 'bottom' property.

        @param bottom the new 'bottom' value
        """
        ...

    def get_height(self, face: BlockFace) -> NotNull["Height"]:
        """
        Gets the height of the specified face.

        @param face to check
        @return if face is enabled
        """
        ...

    def set_height(self, face: BlockFace, height: NotNull["Height"]) -> None:
        """
        Set the height of the specified face.

        @param face to set
        @param height the height
        """
        ...

    class Height:
        """
        The different heights a face may have.
        """

        NONE = ...
        LOW = ...
        TALL = ...

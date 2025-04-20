from typing import List
from org.bukkit import Material
from org.bukkit.material import TexturedMaterial

class SmoothBrick(TexturedMaterial):
    """
    Represents the different types of smooth bricks.

    @deprecated all usage of MaterialData is deprecated and subject to removal.
    Use {@link org.bukkit.block.data.BlockData}.
    """

    textures: List[Material]

    def __init__(self) -> None:
        """
        Initializes a SmoothBrick with the default material.
        """
        ...

    def __init__(self, type: Material) -> None:
        """
        Initializes a SmoothBrick with the specified material type.

        :param type: the type
        """
        ...

    @Deprecated(since="1.6.2")
    def __init__(self, type: Material, data: bytes) -> None:
        """
        Initializes a SmoothBrick with the specified material type and raw data value.

        :param type: the type
        :param data: the raw data value
        @deprecated Magic value
        """
        ...

    def get_textures(self) -> List[Material]:
        """
        Returns the list of textures for this SmoothBrick.

        :return: list of Material textures
        """
        ...

    def clone(self) -> 'SmoothBrick':
        """
        Clones this SmoothBrick.

        :return: a clone of this SmoothBrick
        """
        ...
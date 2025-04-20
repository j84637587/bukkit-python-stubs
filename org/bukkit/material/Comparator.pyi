from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import MaterialData
from typing import Literal

class Comparator(MaterialData, Directional, Redstone):
    DEFAULT_DIRECTION: BlockFace = BlockFace.NORTH
    DEFAULT_SUBTRACTION_MODE: bool = False
    DEFAULT_STATE: bool = False

    """
    Represents a comparator in the on or off state, in normal or subtraction mode and facing in a specific direction.

    @see Material.LEGACY_REDSTONE_COMPARATOR_OFF
    @see Material.LEGACY_REDSTONE_COMPARATOR_ON

    @deprecated all usage of MaterialData is deprecated and subject to removal.
    Use {@link org.bukkit.block.data.BlockData}.
    """
    def __init__(self) -> None:
        """
        Constructs a comparator switched off, with the default mode (normal) and facing the default direction (north).
        """
        ...

    def __init__(self, facing_direction: BlockFace) -> None:
        """
        Constructs a comparator switched off, with the default mode (normal) and facing the specified direction.

        @param facing_direction the direction the comparator is facing

        @see BlockFace
        """
        ...

    def __init__(self, facing_direction: BlockFace, is_subtraction: bool) -> None:
        """
        Constructs a comparator switched off, with the specified mode and facing the specified direction.

        @param facing_direction the direction the comparator is facing
        @param is_subtraction True if the comparator is in subtraction mode, false for normal comparator operation

        @see BlockFace
        """
        ...

    def __init__(self, facing_direction: BlockFace, is_subtraction: bool, state: bool) -> None:
        """
        Constructs a comparator switched on or off, with the specified mode and facing the specified direction.

        @param facing_direction the direction the comparator is facing
        @param is_subtraction True if the comparator is in subtraction mode, false for normal comparator operation
        @param state True if the comparator is in the on state

        @see BlockFace
        """
        ...

    def __init__(self, type: Material) -> None:
        ...
    
    @Deprecated(since="1.9")
    def __init__(self, type: Material, data: bytes) -> None:
        """
        @param type the type
        @param data the raw data value
        @deprecated Magic value
        """
        ...

    def set_subtraction_mode(self, is_subtraction: bool) -> None:
        """
        Sets whether the comparator is in subtraction mode.

        @param is_subtraction True if the comparator is in subtraction mode, false for normal comparator operation
        """
        ...

    def is_subtraction_mode(self) -> bool:
        """
        Checks whether the comparator is in subtraction mode

        @return True if the comparator is in subtraction mode, false if normal comparator operation
        """
        ...

    def set_facing_direction(self, face: BlockFace) -> None:
        """
        Sets the direction this comparator is facing

        @param face The direction to set this comparator to

        @see BlockFace
        """
        ...

    def get_facing(self) -> BlockFace:
        """
        Gets the direction this comparator is facing

        @return The direction this comparator is facing

        @see BlockFace
        """
        ...

    def __str__(self) -> str:
        ...
    
    def clone(self) -> 'Comparator':
        ...
    
    def is_powered(self) -> bool:
        """
        Checks if the comparator is powered

        @return true if the comparator is powered
        """
        ...

    def is_being_powered(self) -> bool:
        """
        Checks if the comparator is being powered

        @return true if the comparator is being powered
        """
        ...
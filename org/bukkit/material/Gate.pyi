from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import MaterialData
from typing import Literal

class Gate(MaterialData):
    """
    Represents a fence gate

    @deprecated all usage of MaterialData is deprecated and subject to removal.
    Use {@link org.bukkit.block.data.BlockData}.
    """
    
    OPEN_BIT: Literal[0x4]
    DIR_BIT: Literal[0x3]
    GATE_SOUTH: Literal[0x0]
    GATE_WEST: Literal[0x1]
    GATE_NORTH: Literal[0x2]
    GATE_EAST: Literal[0x3]

    def __init__(self) -> None:
        """
        Initializes a new Gate instance with Material.LEGACY_FENCE_GATE.
        """
        ...

    @Deprecated(since="1.13")
    def __init__(self, type: Material, data: bytes) -> None:
        """
        @param type the type
        @param data the raw data value
        @deprecated Magic value
        """
        ...

    def __init__(self, data: bytes) -> None:
        """
        Initializes a new Gate instance with Material.LEGACY_FENCE_GATE and specified data.
        """
        ...

    def set_facing_direction(self, face: BlockFace) -> None:
        """
        Sets the facing direction of the gate.

        @param face the direction to face
        """
        ...

    def get_facing(self) -> BlockFace:
        """
        Gets the current facing direction of the gate.

        @return the facing direction
        """
        ...

    def is_open(self) -> bool:
        """
        Checks if the gate is open.

        @return True if the gate is open, False otherwise
        """
        ...

    def set_open(self, is_open: bool) -> None:
        """
        Sets the open state of the gate.

        @param is_open True to open the gate, False to close it
        """
        ...

    def __str__(self) -> str:
        """
        Returns a string representation of the gate's state.

        @return a string indicating if the gate is open or closed and its facing direction
        """
        ...

    def clone(self) -> 'Gate':
        """
        Clones the gate instance.

        @return a clone of the gate
        """
        ...
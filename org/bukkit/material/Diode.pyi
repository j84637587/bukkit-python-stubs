from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import MaterialData
from typing import Optional

class Diode(MaterialData, Directional, Redstone):
    """
    Represents a diode/repeater in the on or off state, with a delay and facing
    in a specific direction.

    @see Material.LEGACY_DIODE_BLOCK_OFF
    @see Material.LEGACY_DIODE_BLOCK_ON

    @deprecated all usage of MaterialData is deprecated and subject to removal.
    Use {@link org.bukkit.block.data.BlockData}.
    """
    
    DEFAULT_DIRECTION: BlockFace = BlockFace.NORTH
    DEFAULT_DELAY: int = 1
    DEFAULT_STATE: bool = False

    def __init__(self) -> None:
        """
        Constructs a diode switched on, with a delay of 1 and facing the default
        direction (north).

        By default this constructor creates a diode that is switched on for
        backwards compatibility with past implementations.
        """
        ...

    def __init__(self, facingDirection: BlockFace) -> None:
        """
        Constructs a diode switched off, with a delay of 1 and facing the
        specified direction.

        @param facingDirection the direction the diode is facing

        @see BlockFace
        """
        ...

    def __init__(self, facingDirection: BlockFace, delay: int) -> None:
        """
        Constructs a diode switched off, with the specified delay and facing the
        specified direction.

        @param facingDirection the direction the diode is facing
        @param delay The number of ticks (1-4) before the diode turns on after
        being powered

        @see BlockFace
        """
        ...

    def __init__(self, facingDirection: BlockFace, delay: int, state: bool) -> None:
        """
        Constructs a diode switched on or off, with the specified delay and
        facing the specified direction.

        @param facingDirection the direction the diode is facing
        @param delay The number of ticks (1-4) before the diode turns on after
        being powered
        @param state True if the diode is in the on state

        @see BlockFace
        """
        ...

    def __init__(self, type: Material) -> None:
        ...
    
    def __init__(self, type: Material, data: bytes) -> None:
        """
        @param type the type
        @param data the raw data value
        @deprecated Magic value
        """
        ...

    def setDelay(self, delay: int) -> None:
        """
        Sets the delay of the repeater.

        @param delay The new delay (1-4)
        """
        ...

    def getDelay(self) -> int:
        """
        Gets the delay of the repeater in ticks.

        @return The delay (1-4)
        """
        ...

    def setFacingDirection(self, face: BlockFace) -> None:
        """
        Sets the direction this diode is facing.

        @param face The direction to set this diode to

        @see BlockFace
        """
        ...

    def getFacing(self) -> BlockFace:
        """
        Gets the direction this diode is facing

        @return The direction this diode is facing

        @see BlockFace
        """
        ...

    def __str__(self) -> str:
        ...
    
    def clone(self) -> 'Diode':
        ...
    
    def isPowered(self) -> bool:
        """
        Checks if the diode is powered.

        @return true if the diode is powered
        """
        ...
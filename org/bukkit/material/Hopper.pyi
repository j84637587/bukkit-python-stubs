from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import MaterialData
from org.bukkit.material import Directional
from org.bukkit.material import Redstone

"""
Represents a hopper in an active or deactivated state and facing in a
specific direction.

@see Material#HOPPER

@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class Hopper(MaterialData, Directional, Redstone):
    DEFAULT_DIRECTION: BlockFace = BlockFace.DOWN
    DEFAULT_ACTIVE: bool = True

    def __init__(self: "Hopper") -> None:
        """Constructs a hopper facing the default direction (down) and initially active."""
        ...

    def __init__(self: "Hopper", facingDirection: BlockFace) -> None:
        """Constructs a hopper facing the specified direction and initially active.

        @param facingDirection the direction the hopper is facing

        @see BlockFace
        """
        ...

    def __init__(self: "Hopper", facingDirection: BlockFace, isActive: bool) -> None:
        """Constructs a hopper facing the specified direction and either active or not.

        @param facingDirection the direction the hopper is facing
        @param isActive True if the hopper is initially active, false if
        deactivated

        @see BlockFace
        """
        ...

    def __init__(self: "Hopper", type: Material) -> None:
        """Initializes a hopper with the specified material type."""
        ...

    @Deprecated(since="1.9")
    def __init__(self: "Hopper", type: Material, data: bytes) -> None:
        """@param type the type
        @param data the raw data value
        @deprecated Magic value
        """
        ...

    def setActive(self: "Hopper", isActive: bool) -> None:
        """Sets whether the hopper is active or not.

        @param isActive True if the hopper is active, false if deactivated as if
        powered by redstone
        """
        ...

    def isActive(self: "Hopper") -> bool:
        """Checks whether the hopper is active or not.

        @return True if the hopper is active, false if deactivated
        """
        ...

    def setFacingDirection(self: "Hopper", face: BlockFace) -> None:
        """Sets the direction this hopper is facing

        @param face The direction to set this hopper to

        @see BlockFace
        """
        ...

    def getFacing(self: "Hopper") -> BlockFace:
        """Gets the direction this hopper is facing

        @return The direction this hopper is facing

        @see BlockFace
        """
        ...

    def __str__(self: "Hopper") -> str:
        """Returns a string representation of the hopper."""
        ...

    def clone(self: "Hopper") -> "Hopper":
        """Creates a clone of this hopper."""
        ...

    def isPowered(self: "Hopper") -> bool:
        """Checks if the hopper is powered.

        @return true if the hopper is powered
        """
        ...
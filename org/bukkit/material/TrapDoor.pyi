from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import SimpleAttachableMaterialData
from org.bukkit.material import Openable

"""
Represents a trap door

@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class TrapDoor(SimpleAttachableMaterialData, Openable):
    def __init__(self) -> None:
        super().__init__(Material.LEGACY_TRAP_DOOR)

    def __init__(self, type: Material) -> None:
        super().__init__(type)

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    def __init__(self, type: Material, data: bytes) -> None:
        super().__init__(type, data)

    def is_open(self) -> bool:
        ...

    def set_open(self, is_open: bool) -> None:
        ...

    """
    Test if trapdoor is inverted

    @return true if inverted (top half), false if normal (bottom half)
    """
    def is_inverted(self) -> bool:
        ...

    """
    Set trapdoor inverted state

    @param inv - true if inverted (top half), false if normal (bottom half)
    """
    def set_inverted(self, inv: bool) -> None:
        ...

    def get_attached_face(self) -> BlockFace:
        ...

    def set_facing_direction(self, face: BlockFace) -> None:
        ...

    def __str__(self) -> str:
        ...

    def clone(self) -> 'TrapDoor':
        ...
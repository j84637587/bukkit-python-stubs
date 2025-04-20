from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import SimpleAttachableMaterialData
from org.bukkit.material import Redstone

"""
Represents the tripwire hook

@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class TripwireHook(SimpleAttachableMaterialData, Redstone):

    def __init__(self) -> None:
        ...

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    @Deprecated(since="1.6.2")
    def __init__(self, type: Material, data: bytes) -> None:
        ...

    def __init__(self, dir: BlockFace) -> None:
        ...

    """
    Test if tripwire is connected

    @return true if connected, false if not
    """
    def is_connected(self) -> bool:
        ...

    """
    Set tripwire connection state

    @param connected - true if connected, false if not
    """
    def set_connected(self, connected: bool) -> None:
        ...

    """
    Test if hook is currently activated

    @return true if activated, false if not
    """
    def is_activated(self) -> bool:
        ...

    """
    Set hook activated state

    @param act - true if activated, false if not
    """
    def set_activated(self, act: bool) -> None:
        ...

    def set_facing_direction(self, face: BlockFace) -> None:
        ...

    def get_attached_face(self) -> BlockFace:
        ...

    def is_powered(self) -> bool:
        ...

    def clone(self) -> 'TripwireHook':
        ...

    def __str__(self) -> str:
        ...
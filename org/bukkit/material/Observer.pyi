from org.bukkit import Material
from org.bukkit.block import BlockFace
from org.bukkit.material import MaterialData
from typing import Any

class Observer(MaterialData, Directional, Redstone):
    """
    Represents an observer.

    @deprecated all usage of MaterialData is deprecated and subject to removal.
    Use {@link org.bukkit.block.data.BlockData}.
    """

    def __init__(self: "Observer") -> None:
        super().__init__(Material.LEGACY_OBSERVER)

    def __init__(self: "Observer", direction: BlockFace) -> None:
        self()
        self.set_facing_direction(direction)

    def __init__(self: "Observer", type: Material) -> None:
        super().__init__(type)

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    def __init__(self: "Observer", type: Material, data: bytes) -> None:
        super().__init__(type, data)

    def is_powered(self: "Observer") -> bool:
        ...

    def set_facing_direction(self: "Observer", face: BlockFace) -> None:
        ...

    def get_facing(self: "Observer") -> BlockFace:
        ...

    def __str__(self: "Observer") -> str:
        ...

    def clone(self: "Observer") -> "Observer":
        ...
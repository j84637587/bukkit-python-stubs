from org.bukkit import Material
from org.bukkit import NetherWartsState
from org.bukkit.material import MaterialData
from typing import Literal

class NetherWarts(MaterialData):
    """
    Represents nether wart

    @deprecated all usage of MaterialData is deprecated and subject to removal.
    Use {@link org.bukkit.block.data.BlockData}.
    """

    def __init__(self: "NetherWarts") -> None:
        super().__init__(Material.LEGACY_NETHER_WARTS)

    def __init__(self: "NetherWarts", state: NetherWartsState) -> None:
        self()
        self.set_state(state)

    def __init__(self: "NetherWarts", type: Material) -> None:
        super().__init__(type)

    @Deprecated(since="1.6.2")
    def __init__(self: "NetherWarts", type: Material, data: bytes) -> None:
        super().__init__(type, data)

    """
    Gets the current growth state of this nether wart

    @return NetherWartsState of this nether wart
    """
    def get_state(self: "NetherWarts") -> NetherWartsState:
        ...

    """
    Sets the growth state of this nether wart

    @param state New growth state of this nether wart
    """
    def set_state(self: "NetherWarts", state: NetherWartsState) -> None:
        ...

    def __str__(self: "NetherWarts") -> str:
        ...

    def clone(self: "NetherWarts") -> "NetherWarts":
        ...
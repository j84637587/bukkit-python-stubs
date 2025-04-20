from org.bukkit import CropState
from org.bukkit import Material
from org.bukkit.material import MaterialData

"""
Represents the different types of crops in different states of growth.

@see Material.LEGACY_CROPS
@see Material.LEGACY_CARROT
@see Material.LEGACY_POTATO
@see Material.LEGACY_BEETROOT_BLOCK
@see Material.LEGACY_NETHER_WARTS

@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class Crops(MaterialData):
    DEFAULT_TYPE: Material
    DEFAULT_STATE: CropState

    """
    Constructs a wheat crop block in the seeded state.
    """
    def __init__(self) -> None: ...

    """
    Constructs a wheat crop block in the given growth state

    @param state The growth state of the crops
    """
    def __init__(self, state: CropState) -> None: ...

    """
    Constructs a crop block of the given type and in the given growth state

    @param type The type of crops
    @param state The growth state of the crops
    """
    def __init__(self, type: Material, state: CropState) -> None: ...

    """
    Constructs a crop block of the given type and in the seeded state

    @param type The type of crops
    """
    def __init__(self, type: Material) -> None: ...

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    def __init__(self, type: Material, data: bytes) -> None: ...

    """
    Gets the current growth state of this crop

    For crops with only four growth states such as beetroot, only the values SEEDED, SMALL, TALL and RIPE will be
    returned.

    @return CropState of this crop
    """
    def get_state(self) -> CropState: ...

    """
    Sets the growth state of this crop

    For crops with only four growth states such as beetroot, the 8 CropStates are mapped into four states:

    SEEDED, SMALL, TALL and RIPE

    GERMINATED will change to SEEDED
    VERY_SMALL will change to SMALL
    MEDIUM will change to TALL
    VERY_TALL will change to RIPE

    @param state New growth state of this crop
    """
    def set_state(self, state: CropState) -> None: ...

    def __str__(self) -> str: ...

    def clone(self) -> 'Crops': ...
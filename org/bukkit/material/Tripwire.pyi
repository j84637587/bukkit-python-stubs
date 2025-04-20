from org.bukkit import Material
from org.bukkit.material import MaterialData

"""
Represents the tripwire

@deprecated all usage of MaterialData is deprecated and subject to removal.
Use {@link org.bukkit.block.data.BlockData}.
"""
class Tripwire(MaterialData):

    def __init__(self) -> None:
        super().__init__(Material.LEGACY_TRIPWIRE)

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    @deprecated(since="1.6.2")
    def __init__(self, type: Material, data: bytes) -> None:
        super().__init__(type, data)

    """
    Test if tripwire is currently activated

    @return true if activated, false if not
    """
    def is_activated(self) -> bool:
        ...

    """
    Set tripwire activated state

    @param act - true if activated, false if not
    """
    def set_activated(self, act: bool) -> None:
        ...

    """
    Test if object triggering this tripwire directly

    @return true if object activating tripwire, false if not
    """
    def is_object_triggering(self) -> bool:
        ...

    """
    Set object triggering state for this tripwire

    @param trig - true if object activating tripwire, false if not
    """
    def set_object_triggering(self, trig: bool) -> None:
        ...

    def clone(self) -> 'Tripwire':
        ...

    def __str__(self) -> str:
        ...
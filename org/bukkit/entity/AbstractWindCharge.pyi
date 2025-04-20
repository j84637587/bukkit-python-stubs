from org.jetbrains.annotations import ApiStatus
from org.bukkit.entity import Fireball

"""
Represents a Wind Charge.
"""

class AbstractWindCharge(Fireball):
    """
    Immediately explode this WindCharge.
    """

    def explode(self) -> None: ...

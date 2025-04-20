from org.bukkit.entity import ComplexEntityPart
from org.bukkit.entity import Damageable
from org.bukkit.entity import EnderDragon
from typing import Protocol

class EnderDragonPart(Protocol):
    """Represents an ender dragon part"""

    def get_parent(self) -> EnderDragon:
        ...
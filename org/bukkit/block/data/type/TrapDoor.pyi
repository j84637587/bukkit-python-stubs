from org.bukkit.block.data import Bisected
from org.bukkit.block.data import Directional
from org.bukkit.block.data import Openable
from org.bukkit.block.data import Powerable
from org.bukkit.block.data import Waterlogged

class TrapDoor(Bisected, Directional, Openable, Powerable, Waterlogged):
    """Interface representing a trap door."""
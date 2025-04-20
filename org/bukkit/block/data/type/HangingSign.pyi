from org.bukkit.block.data import Attachable
from org.bukkit.block.data import Rotatable
from org.bukkit.block.data import Waterlogged

class HangingSign(Attachable, Rotatable, Waterlogged):
    """Interface representing a hanging sign."""
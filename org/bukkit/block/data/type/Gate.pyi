from org.bukkit.block.data import Directional
from org.bukkit.block.data import Openable
from org.bukkit.block.data import Powerable

"""
'in_wall' indicates if the fence gate is attached to a wall, and if true the
texture is lowered by a small amount to blend in better.
"""
class Gate(Directional, Openable, Powerable):
    """
    Gets the value of the 'in_wall' property.

    @return: the 'in_wall' value
    """
    def is_in_wall(self) -> bool: ...

    """
    Sets the value of the 'in_wall' property.

    @param in_wall: the new 'in_wall' value
    """
    def set_in_wall(self, in_wall: bool) -> None: ...
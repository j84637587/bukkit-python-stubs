from org.bukkit.block.data import Directional
from org.bukkit.block.data import Lightable
from org.bukkit.block.data import Waterlogged

"""
'signal_fire' denotes whether the fire is extra smokey due to having a hay
bale placed beneath it.
"""
class Campfire(Directional, Lightable, Waterlogged):
    """
    Gets the value of the 'signal_fire' property.

    @return: the 'signal_fire' value
    """
    def is_signal_fire(self) -> bool: ...

    """
    Sets the value of the 'signal_fire' property.

    @param signal_fire: the new 'signal_fire' value
    """
    def set_signal_fire(self, signal_fire: bool) -> None: ...
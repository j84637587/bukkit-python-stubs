from org.bukkit.block.data import Directional
from org.bukkit.block.data import Powerable

"""
'has_book' is a quick flag to check whether this lectern has a book inside
it.
"""
class Lectern(Directional, Powerable):
    """
    Gets the value of the 'has_book' property.

    @return: the 'has_book' value
    """
    def has_book(self) -> bool: ...
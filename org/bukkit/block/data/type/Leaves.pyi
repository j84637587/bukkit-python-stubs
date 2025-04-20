from org.bukkit.block.data import Waterlogged

"""
'persistent' indicates whether or not leaves will be checked by the server to
see if they are subject to decay or not.
<br>
'distance' denotes how far the block is from a tree and is used in
conjunction with 'persistent' flag to determine if the leaves will decay or
not.
"""
class Leaves(Waterlogged):
    """
    Gets the value of the 'persistent' property.

    @return: the persistent value
    """
    def is_persistent(self) -> bool: ...

    """
    Sets the value of the 'persistent' property.

    @param persistent: the new 'persistent' value
    """
    def set_persistent(self, persistent: bool) -> None: ...

    """
    Gets the value of the 'distance' property.

    @return: the 'distance' value
    """
    def get_distance(self) -> int: ...

    """
    Sets the value of the 'distance' property.

    @param distance: the new 'distance' value
    """
    def set_distance(self, distance: int) -> None: ...
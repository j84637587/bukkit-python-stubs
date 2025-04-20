from org.bukkit.Location import Location
from org.jetbrains.annotations import ApiStatus, NotNull
from org.bukkit.entity import Monster
from org.bukkit.entity import Player

"""
Represents a Creaking.
"""
class Creaking(Monster):

    """
    Gets the home location for this Creaking (ie where its corresponding
    {@link org.bukkit.block.CreakingHeart} can be).

    @return the location of the home.
    """
        def get_home(self) -> Location: ...

    """
    Sets the home location for this Creaking.

    @param location the location of the home.
    """
    def set_home(self, location: NotNull[Location]) -> None: ...

    """
    Activate this Creaking to target and follow a player.

    @param player the target.
    """
    def activate(self, player: NotNull[Player]) -> None: ...

    """
    Deactivate this Creaking from the current target player.
    """
    def deactivate(self) -> None: ...

    """
    Gets if this Creaking is active.

    @return true if is active.
    """
    def is_active(self) -> bool: ...
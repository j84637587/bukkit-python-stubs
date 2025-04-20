from typing import Optional
from org.bukkit.Location import Location
from org.bukkit.entity.Player import Player
from org.bukkit.event.Cancellable import Cancellable
from org.bukkit.event.HandlerList import HandlerList
from com.google.common.base import Preconditions

"""
This event is fired when the spawn point of the player is changed.
"""
class PlayerSpawnChangeEvent(PlayerEvent, Cancellable):
    handlers: HandlerList

    def __init__(self, player: Player, new_spawn: Optional[Location], forced: bool, cause: 'Cause') -> None:
        ...

    """
    Gets the cause of spawn change.

    @return change cause
    """
    def getCause(self) -> 'Cause':
        ...

    """
    Gets if the spawn position will be used regardless of bed obstruction
    rules.

    @return true if is forced
    """
    def isForced(self) -> bool:
        ...

    """
    Sets if the spawn position will be used regardless of bed obstruction
    rules.

    @param forced true if forced
    """
    def setForced(self, forced: bool) -> None:
        ...

    """
    Gets the new spawn to be set.

    @return new spawn location
    """
    def getNewSpawn(self) -> Optional[Location]:
        ...

    """
    Sets the new spawn location.

    @param newSpawn new spawn location, with non-null world
    """
    def setNewSpawn(self, new_spawn: Optional[Location]) -> None:
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...

    def getHandlers(self) -> HandlerList:
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        ...

    class Cause:
        """
        Indicate the spawn was set by a command.
        """
        COMMAND = ...

        """
        Indicate the spawn was set by the player interacting with a bed.
        """
        BED = ...

        """
        Indicate the spawn was set by the player interacting with a respawn
        anchor.
        """
        RESPAWN_ANCHOR = ...

        """
        Indicate the spawn was set by the use of plugins.
        """
        PLUGIN = ...

        """
        Indicate the spawn was reset by an invalid bed position or empty
        respawn anchor.
        """
        RESET = ...

        """
        Indicate the spawn was caused by an unknown reason.
        """
        UNKNOWN = ...
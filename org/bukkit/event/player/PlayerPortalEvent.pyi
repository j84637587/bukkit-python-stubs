from org.bukkit.Location import Location
from org.bukkit.entity.Player import Player
from org.bukkit.event.HandlerList import HandlerList
from org.bukkit.event.player.PlayerTeleportEvent import PlayerTeleportEvent
from org.bukkit.event.player.TeleportCause import TeleportCause
from typing import Optional

class PlayerPortalEvent(PlayerTeleportEvent):
    """
    Called when a player is about to teleport because it is in contact with a
    portal which will generate an exit portal.
    <p>
    For other entities see {@link org.bukkit.event.entity.EntityPortalEvent}
    """

    handlers: HandlerList
    getSearchRadius: int
    canCreatePortal: bool
    creationRadius: int

    def __init__(self, player: Player, from_location: Location, to_location: Optional[Location] = None) -> None:
        ...

    def __init__(self, player: Player, from_location: Location, to_location: Optional[Location], cause: TeleportCause) -> None:
        ...

    def __init__(self, player: Player, from_location: Location, to_location: Optional[Location], cause: TeleportCause, getSearchRadius: int, canCreatePortal: bool, creationRadius: int) -> None:
        ...

    def setSearchRadius(self, searchRadius: int) -> None:
        """
        Set the Block radius to search in for available portals.

        :param searchRadius: the radius in which to search for a portal from the location
        """
        ...

    def getSearchRadius(self) -> int:
        """
        Gets the search radius value for finding an available portal.

        :return: the currently set search radius
        """
        ...

    def getCanCreatePortal(self) -> bool:
        """
        Returns whether the server will attempt to create a destination portal or not.

        :return: whether there should create be a destination portal created
        """
        ...

    def setCanCreatePortal(self, canCreatePortal: bool) -> None:
        """
        Sets whether the server should attempt to create a destination portal or not.

        :param canCreatePortal: Sets whether there should be a destination portal created
        """
        ...

    def setCreationRadius(self, creationRadius: int) -> None:
        """
        Sets the maximum radius the world is searched for a free space from the given location.

        If enough free space is found then the portal will be created there, if not it will force create with air-space at the target location.

        Does not apply to end portal target platforms which will always appear at the target location.

        :param creationRadius: the radius in which to create a portal from the location
        """
        ...

    def getCreationRadius(self) -> int:
        """
        Gets the maximum radius the world is searched for a free space from the given location.

        If enough free space is found then the portal will be created there, if not it will force create with air-space at the target location.

        Does not apply to end portal target platforms which will always appear at the target location.

        :return: the currently set creation radius
        """
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        ...
    
    def getHandlers(self) -> HandlerList:
        ...
from typing import Optional
from org.bukkit.Location import Location
from org.bukkit.entity.Player import Player
from org.bukkit.event.HandlerList import HandlerList
from org.jetbrains.annotations import NotNull

class PlayerRespawnEvent(PlayerEvent):
    """
    Called when a player respawns.
    """

    handlers: HandlerList

    def __init__(self, respawnPlayer: Player, respawnLocation: Location, isBedSpawn: bool) -> None:
        ...

    def __init__(self, respawnPlayer: Player, respawnLocation: Location, isBedSpawn: bool, isAnchorSpawn: bool) -> None:
        ...

    def __init__(self, respawnPlayer: Player, respawnLocation: Location, isBedSpawn: bool, isAnchorSpawn: bool, respawnReason: 'RespawnReason') -> None:
        ...

        def getRespawnLocation(self) -> Location:
        ...

    def setRespawnLocation(self, respawnLocation: Location) -> None:
        ...

    def isBedSpawn(self) -> bool:
        ...

    def isAnchorSpawn(self) -> bool:
        ...

        def getRespawnReason(self) -> 'RespawnReason':
        ...

        def getHandlers(self) -> HandlerList:
        ...

        @staticmethod
    def getHandlerList() -> HandlerList:
        ...

class RespawnReason:
    """
    An enum to specify the reason a respawn event was called.
    """
    DEATH = ...
    END_PORTAL = ...
    PLUGIN = ...
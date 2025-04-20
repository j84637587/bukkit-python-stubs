from org.bukkit.GameMode import GameMode
from org.bukkit.entity.Player import Player
from org.bukkit.event.Cancellable import Cancellable
from org.bukkit.event.HandlerList import HandlerList
from typing import Any

class PlayerGameModeChangeEvent(PlayerEvent, Cancellable):
    """
    Called when the GameMode of the player is changed.
    """
    
    handlers: HandlerList = HandlerList()
    cancelled: bool
    newGameMode: GameMode

    def __init__(self, player: Player, newGameMode: GameMode) -> None:
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...

    """
    Gets the GameMode the player is switched to.

    @return: player's new GameMode
    """
    def getNewGameMode(self) -> GameMode:
        ...

    def getHandlers(self) -> HandlerList:
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        ...
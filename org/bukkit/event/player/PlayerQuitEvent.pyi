from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import PlayerEvent
from typing import Optional

class PlayerQuitEvent(PlayerEvent):
    """
    Called when a player leaves a server
    """

    handlers: HandlerList = HandlerList()
    quitMessage: Optional[str]

    def __init__(self, who: Player, quitMessage: Optional[str]) -> None:
        super().__init__(who)
        self.quitMessage = quitMessage

    """
    Gets the quit message to send to all online players

    @return string quit message
    """
    def getQuitMessage(self) -> Optional[str]:
        ...

    """
    Sets the quit message to send to all online players

    @param quitMessage quit message
    """
    def setQuitMessage(self, quitMessage: Optional[str]) -> None:
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        ...
    
    def getHandlers(self) -> HandlerList:
        ...
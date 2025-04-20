from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import PlayerEvent
from typing import Any

class PlayerLevelChangeEvent(PlayerEvent):
    """
    Called when a players level changes
    """

    handlers: HandlerList = HandlerList()
    oldLevel: int
    newLevel: int

    def __init__(self, player: Player, oldLevel: int, newLevel: int) -> None:
        super().__init__(player)
        self.oldLevel = oldLevel
        self.newLevel = newLevel

    """
    Gets the old level of the player

    @return: The old level of the player
    """
    def getOldLevel(self) -> int:
        ...

    """
    Gets the new level of the player

    @return: The new (current) level of the player
    """
    def getNewLevel(self) -> int:
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        ...

    def getHandlers(self) -> HandlerList:
        ...
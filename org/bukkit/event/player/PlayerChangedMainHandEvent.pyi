from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.inventory import MainHand
from typing import Any

class PlayerChangedMainHandEvent(PlayerEvent):
    """
    Called when a player changes their main hand in the client settings.
    """

    handlers: HandlerList = HandlerList()
    mainHand: MainHand

    def __init__(self, who: Player, mainHand: MainHand) -> None:
        super().__init__(who)
        self.mainHand = mainHand

    """
    Gets the new main hand of the player. The old hand is still momentarily
    available via {@link Player#getMainHand()}.

    @return: the new {@link MainHand} of the player
    """
    def getMainHand(self) -> MainHand:
        return self.mainHand

    def getHandlers(self) -> HandlerList:
        return self.handlers

    @staticmethod
    def getHandlerList() -> HandlerList:
        return PlayerChangedMainHandEvent.handlers
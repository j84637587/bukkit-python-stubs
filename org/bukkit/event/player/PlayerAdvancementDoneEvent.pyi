from org.bukkit.advancement import Advancement
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import PlayerEvent
from typing import Any

class PlayerAdvancementDoneEvent(PlayerEvent):
    """
    Called when a player has completed all criteria in an advancement.
    """

    handlers: HandlerList = HandlerList()
    advancement: Advancement

    def __init__(self, who: Player, advancement: Advancement) -> None:
        super().__init__(who)
        self.advancement = advancement

    """
    Get the advancement which has been completed.

    @return: completed advancement
    """
    def getAdvancement(self) -> Advancement:
        ...

        def getHandlers(self) -> HandlerList:
        ...

        @staticmethod
    def getHandlerList() -> HandlerList:
        ...
from org.bukkit.DyeColor import DyeColor
from org.bukkit.entity.Player import Player
from org.bukkit.entity.Sheep import Sheep
from org.bukkit.event.Cancellable import Cancellable
from org.bukkit.event.HandlerList import HandlerList
from org.bukkit.event.entity.EntityEvent import EntityEvent
from typing import Optional

class SheepDyeWoolEvent(EntityEvent, Cancellable):
    """
    Called when a sheep's wool is dyed
    """
    handlers: HandlerList = HandlerList()
    cancel: bool
    color: DyeColor
    player: Optional[Player]

    def __init__(self, sheep: Sheep, color: DyeColor, player: Optional[Player] = None) -> None:
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...

    def getEntity(self) -> Sheep:
        ...

    def getPlayer(self) -> Optional[Player]:
        """
        Returns the player dyeing the sheep, if available.

        :return: player or None
        """
        ...

    def getColor(self) -> DyeColor:
        """
        Gets the DyeColor the sheep is being dyed

        :return: the DyeColor the sheep is being dyed
        """
        ...

    def setColor(self, color: DyeColor) -> None:
        """
        Sets the DyeColor the sheep is being dyed

        :param color: the DyeColor the sheep will be dyed
        """
        ...

    def getHandlers(self) -> HandlerList:
        ...
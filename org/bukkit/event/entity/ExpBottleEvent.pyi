from org.bukkit.block import Block
from org.bukkit.block import BlockFace
from org.bukkit.entity import Entity
from org.bukkit.entity import ThrownExpBottle
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import ProjectileHitEvent
from typing import Optional

class ExpBottleEvent(ProjectileHitEvent):
    """
    Called when a ThrownExpBottle hits and releases experience.
    """
    
    handlers: HandlerList = HandlerList()
    exp: int
    showEffect: bool = True

    def __init__(self, bottle: ThrownExpBottle, exp: int) -> None:
        """
        @Deprecated(since = "1.20.2")
        """
        self.__init__(bottle, None, None, None, exp)

    def __init__(self, bottle: ThrownExpBottle, hitEntity: Optional[Entity], hitBlock: Optional[Block], hitFace: Optional[BlockFace], exp: int) -> None:
        super().__init__(bottle, hitEntity, hitBlock, hitFace)
        self.exp = exp

    def getEntity(self) -> ThrownExpBottle:
        """
        @return: The ThrownExpBottle entity.
        """
        return self.entity  # type: ignore

    def getShowEffect(self) -> bool:
        """
        This method indicates if the particle effect should be shown.

        @return: true if the effect will be shown, false otherwise
        """
        return self.showEffect

    def setShowEffect(self, showEffect: bool) -> None:
        """
        This method sets if the particle effect will be shown.
        This does not change the experience created.

        @param showEffect: true indicates the effect will be shown, false indicates no effect will be shown
        """
        self.showEffect = showEffect

    def getExperience(self) -> int:
        """
        This method retrieves the amount of experience to be created.
        The number indicates a total amount to be divided into orbs.

        @return: the total amount of experience to be created
        """
        return self.exp

    def setExperience(self, exp: int) -> None:
        """
        This method sets the amount of experience to be created.
        The number indicates a total amount to be divided into orbs.

        @param exp: the total amount of experience to be created
        """
        self.exp = exp

    def getHandlers(self) -> HandlerList:
        """
        @return: The HandlerList for this event.
        """
        return self.handlers

    @staticmethod
    def getHandlerList() -> HandlerList:
        """
        @return: The static HandlerList for this event.
        """
        return ExpBottleEvent.handlers
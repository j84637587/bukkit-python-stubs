from typing import Literal
from org.bukkit.entity import Entity
from org.bukkit.event import Cancellable, HandlerList
from org.jetbrains.annotations import NotNull

class EntityRegainHealthEvent(EntityEvent, Cancellable):
    """
    Stores data for health-regain events
    """

    handlers: HandlerList = HandlerList()
    cancelled: bool
    amount: float
    regainReason: 'EntityRegainHealthEvent.RegainReason'

    def __init__(self, entity: Entity, amount: float, regainReason: 'EntityRegainHealthEvent.RegainReason') -> None:
        ...

    def getAmount(self) -> float:
        """
        Gets the amount of regained health

        Returns:
            The amount of health regained
        """
        ...

    def setAmount(self, amount: float) -> None:
        """
        Sets the amount of regained health

        Args:
            amount: the amount of health the entity will regain
        """
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...

    def getRegainReason(self) -> 'EntityRegainHealthEvent.RegainReason':
        """
        Gets the reason for why the entity is regaining health

        Returns:
            A RegainReason detailing the reason for the entity regaining health
        """
        ...

        def getHandlers(self) -> HandlerList:
        ...

        @staticmethod
    def getHandlerList() -> HandlerList:
        ...

    class RegainReason:
        """
        An enum to specify the type of health regaining that is occurring
        """
        REGEN: Literal['REGEN']
        SATIATED: Literal['SATIATED']
        EATING: Literal['EATING']
        ENDER_CRYSTAL: Literal['ENDER_CRYSTAL']
        MAGIC: Literal['MAGIC']
        MAGIC_REGEN: Literal['MAGIC_REGEN']
        WITHER_SPAWN: Literal['WITHER_SPAWN']
        WITHER: Literal['WITHER']
        CUSTOM: Literal['CUSTOM']
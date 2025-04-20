from org.bukkit.entity import AbstractHorse
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.event.entity import EntityEvent
from typing import Final

class HorseJumpEvent(EntityEvent, Cancellable):
    handlers: Final[HandlerList] = HandlerList()
    cancelled: bool
    power: float

    def __init__(self, horse: AbstractHorse, power: float) -> None:
        """
        Called when a horse jumps.
        """
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        """
        @deprecated horse jumping was moved client side.
        """
        ...

    def getEntity(self) -> AbstractHorse:
        ...

    def getPower(self) -> float:
        """
        Gets the power of the jump.
        <p>
        Power is a value that defines how much of the horse's jump strength
        should be used for the jump. Power is effectively multiplied times
        the horse's jump strength to determine how high the jump is; 0
        represents no jump strength while 1 represents full jump strength.
        Setting power to a value above 1 will use additional jump strength
        that the horse does not usually have.
        <p>
        Power does not affect how high the horse is capable of jumping, only
        how much of its jumping capability will be used in this jump. To set
        the horse's overall jump strength, see {@link
        AbstractHorse#setJumpStrength(double)}.
        @return jump strength
        """
        ...

    def setPower(self, power: float) -> None:
        """
        Sets the power of the jump.
        <p>
        Jump power can be set to a value above 1.0 which will increase the
        strength of this jump above the horse's actual jump strength.
        <p>
        Setting the jump power to 0 will result in the jump animation still
        playing, but the horse not leaving the ground. Only canceling this
        event will result in no jump animation at all.
        @param power power of the jump
        @deprecated horse jumping was moved client side.
        """
        ...

    def getHandlers(self) -> HandlerList:
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        ...
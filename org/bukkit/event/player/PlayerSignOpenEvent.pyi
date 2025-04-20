from org.bukkit.block import Sign
from org.bukkit.block.sign import Side
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from typing import Literal

class PlayerSignOpenEvent(PlayerEvent, Cancellable):
    """
    This event is fired when a sign is opened by the player.
    """

    handlers: HandlerList
    sign: Sign
    side: Side
    cause: 'PlayerSignOpenEvent.Cause'
    cancelled: bool

    def __init__(self, player: Player, sign: Sign, side: Side, cause: 'PlayerSignOpenEvent.Cause') -> None:
        ...

    def getSign(self) -> Sign:
        """
        Gets the sign that was opened.

        :return: opened sign
        """
        ...

    def getSide(self) -> Side:
        """
        Gets side of the sign opened.

        :return: side of sign opened
        """
        ...

    def getCause(self) -> 'PlayerSignOpenEvent.Cause':
        """
        Gets the cause of the sign open.

        :return: sign open cause
        """
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...

    def getHandlers(self) -> HandlerList:
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        ...

    class Cause:
        """
        Enum for the cause of the sign opening.
        """
        INTERACT: Literal['INTERACT']
        PLACE: Literal['PLACE']
        PLUGIN: Literal['PLUGIN']
        UNKNOWN: Literal['UNKNOWN']
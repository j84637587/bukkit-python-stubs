from org.bukkit.entity import Player
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.event.player import PlayerEvent
from org.bukkit.event.player import PlayerAnimationType
from typing import Any

class PlayerAnimationEvent(PlayerEvent, Cancellable):
    """
    Represents a player animation event
    """

    handlers: HandlerList = HandlerList()
    animationType: PlayerAnimationType
    isCancelled: bool = False

    def __init__(self, player: Player) -> None:
        """
        Construct a new PlayerAnimation event

        :param player: The player instance
        :param playerAnimationType: The animation type
        """
        ...

    def __init__(self, player: Player, playerAnimationType: PlayerAnimationType) -> None:
        """
        Construct a new PlayerAnimation event

        :param player: The player instance
        :param playerAnimationType: The animation type
        """
        ...

    def getAnimationType(self) -> PlayerAnimationType:
        """
        Get the type of this animation event

        :return: the animation type
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
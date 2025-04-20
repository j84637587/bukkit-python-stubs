from org.bukkit.entity import Player
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.util import Vector
from typing import Any

class PlayerVelocityEvent(PlayerEvent, Cancellable):
    """
    Called when the velocity of a player changes.
    """

    handlers: HandlerList = HandlerList()
    cancel: bool
    velocity: Vector

    def __init__(self, player: Player, velocity: Vector) -> None:
        """
        Initializes the PlayerVelocityEvent with the given player and velocity.

        :param player: The player whose velocity is changing.
        :param velocity: The velocity vector that will be sent to the player.
        """
        ...

    def isCancelled(self) -> bool:
        """
        Returns whether the event is cancelled.

        :return: True if the event is cancelled, otherwise false.
        """
        ...

    def setCancelled(self, cancel: bool) -> None:
        """
        Sets whether the event is cancelled.

        :param cancel: True to cancel the event, otherwise false.
        """
        ...

    def getVelocity(self) -> Vector:
        """
        Gets the velocity vector that will be sent to the player.

        :return: Vector the player will get.
        """
        ...

    def setVelocity(self, velocity: Vector) -> None:
        """
        Sets the velocity vector in meters per tick that will be sent to the player.

        :param velocity: The velocity vector that will be sent to the player.
        """
        ...

    def getHandlers(self) -> HandlerList:
        """
        Gets the handler list for this event.

        :return: HandlerList for this event.
        """
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        """
        Gets the static handler list for this event.

        :return: Static HandlerList for this event.
        """
        ...
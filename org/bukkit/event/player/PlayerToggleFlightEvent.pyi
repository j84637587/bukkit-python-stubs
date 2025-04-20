from org.bukkit.entity import Player
from org.bukkit.event import Cancellable, HandlerList
from org.jetbrains.annotations import NotNull

class PlayerToggleFlightEvent(PlayerEvent, Cancellable):
    """
    Called when a player toggles their flying state
    """

    handlers: HandlerList = HandlerList()
    isFlying: bool
    cancel: bool = False

    def __init__(self, player: NotNull[Player], isFlying: bool) -> None:
        """
        Initializes the PlayerToggleFlightEvent.

        :param player: The player involved in the event.
        :param isFlying: The flying state the player is trying to toggle.
        """
        ...

    def isFlying(self) -> bool:
        """
        Returns whether the player is trying to start or stop flying.

        :return: flying state
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
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable, HandlerList
from org.jetbrains.annotations import NotNull

class PlayerToggleSprintEvent(PlayerEvent, Cancellable):
    """
    Called when a player toggles their sprinting state
    """
    
    handlers: HandlerList = HandlerList()
    isSprinting: bool
    cancel: bool = False

    def __init__(self, player: NotNull[Player], isSprinting: bool) -> None:
        """
        Initializes the PlayerToggleSprintEvent.

        :param player: The player involved in the event.
        :param isSprinting: The sprinting state of the player.
        """
        ...

    def isSprinting(self) -> bool:
        """
        Gets whether the player is now sprinting or not.

        :return: sprinting state
        """
        ...

    def isCancelled(self) -> bool:
        """
        Checks if the event is cancelled.

        :return: True if the event is cancelled, False otherwise.
        """
        ...

    def setCancelled(self, cancel: bool) -> None:
        """
        Sets the cancellation state of the event.

        :param cancel: True to cancel the event, False otherwise.
        """
        ...

    def getHandlers(self) -> NotNull[HandlerList]:
        """
        Gets the handlers for this event.

        :return: The handler list for this event.
        """
        ...

    @staticmethod
    def getHandlerList() -> NotNull[HandlerList]:
        """
        Gets the static handler list for this event.

        :return: The static handler list for this event.
        """
        ...
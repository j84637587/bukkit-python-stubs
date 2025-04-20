from org.bukkit.entity import Hanging
from org.bukkit.event import Cancellable, HandlerList
from typing import Literal

class HangingBreakEvent(HangingEvent, Cancellable):
    """
    Triggered when a hanging entity is removed
    """

    handlers: HandlerList = HandlerList()
    cancelled: bool
    cause: 'HangingBreakEvent.RemoveCause'

    def __init__(self, hanging: Hanging, cause: 'HangingBreakEvent.RemoveCause') -> None:
        """
        Initializes a HangingBreakEvent.

        :param hanging: The hanging entity that is being removed.
        :param cause: The cause for the hanging entity's removal.
        """
        ...

    def getCause(self) -> 'HangingBreakEvent.RemoveCause':
        """
        Gets the cause for the hanging entity's removal.

        :return: the RemoveCause for the hanging entity's removal.
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

    class RemoveCause:
        """
        An enum to specify the cause of the removal.
        """
        ENTITY: Literal['ENTITY'] = 'ENTITY'
        EXPLOSION: Literal['EXPLOSION'] = 'EXPLOSION'
        OBSTRUCTION: Literal['OBSTRUCTION'] = 'OBSTRUCTION'
        PHYSICS: Literal['PHYSICS'] = 'PHYSICS'
        DEFAULT: Literal['DEFAULT'] = 'DEFAULT'

    def getHandlers(self) -> HandlerList:
        """
        Gets the handler list for this event.

        :return: the HandlerList for this event.
        """
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        """
        Gets the static handler list for this event.

        :return: the static HandlerList for this event.
        """
        ...
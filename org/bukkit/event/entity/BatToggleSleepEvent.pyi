from org.bukkit.entity import Bat
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.event.entity import EntityEvent
from typing import Literal

class BatToggleSleepEvent(EntityEvent, Cancellable):
    """
    Called when a bat attempts to sleep or wake up from its slumber.
    <p>
    If a Bat Toggle Sleep event is cancelled, the Bat will not toggle its sleep
    state.
    """

    handlers: HandlerList = HandlerList()

    def __init__(self, what: Bat, awake: bool) -> None:
        """
        Initialize the BatToggleSleepEvent.

        :param what: The bat that is toggling sleep.
        :param awake: True if the bat is attempting to awaken, false otherwise.
        """
        ...

    def is_awake(self) -> bool:
        """
        Get whether or not the bat is attempting to awaken.

        :return: true if trying to awaken, false otherwise
        """
        ...

    def set_cancelled(self, cancel: bool) -> None:
        ...
    
    def is_cancelled(self) -> bool:
        ...

    def get_handlers(self) -> HandlerList:
        ...

    @staticmethod
    def get_handler_list() -> HandlerList:
        ...
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.event.player import PlayerEvent
from typing import Optional

class PlayerKickEvent(PlayerEvent, Cancellable):
    """
    Called when a player gets kicked from the server
    """

    handlers: HandlerList = HandlerList()
    leave_message: str
    kick_reason: str
    cancel: bool

    def __init__(self, player_kicked: Player, kick_reason: str, leave_message: str) -> None:
        """
        Initializes the PlayerKickEvent.

        :param player_kicked: The player who is being kicked.
        :param kick_reason: The reason for the kick.
        :param leave_message: The message sent to all online players.
        """
        ...

    def get_reason(self) -> str:
        """
        Gets the reason why the player is getting kicked.

        :return: string kick reason
        """
        ...

    def get_leave_message(self) -> str:
        """
        Gets the leave message sent to all online players.

        :return: string leave message
        """
        ...

    def is_cancelled(self) -> bool:
        """
        Checks if the event is cancelled.

        :return: True if the event is cancelled, False otherwise.
        """
        ...

    def set_cancelled(self, cancel: bool) -> None:
        """
        Sets whether the event is cancelled.

        :param cancel: True to cancel the event, False otherwise.
        """
        ...

    def set_reason(self, kick_reason: str) -> None:
        """
        Sets the reason why the player is getting kicked.

        :param kick_reason: The new kick reason.
        """
        ...

    def set_leave_message(self, leave_message: str) -> None:
        """
        Sets the leave message sent to all online players.

        :param leave_message: The new leave message.
        """
        ...

    def get_handlers(self) -> HandlerList:
        """
        Gets the handlers for this event.

        :return: HandlerList for this event.
        """
        ...

    @staticmethod
    def get_handler_list() -> HandlerList:
        """
        Gets the static handler list for this event.

        :return: HandlerList for this event.
        """
        ...
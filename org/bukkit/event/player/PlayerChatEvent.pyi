from typing import Set
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit import Warning
from google.common.base import Preconditions
from org.jetbrains.annotations import NotNull

"""
Holds information for player chat and commands

@deprecated This event will fire from the main thread and allows the use of
    all of the Bukkit API, unlike the {@link AsyncPlayerChatEvent}.
    <p>
    Listening to this event forces chat to wait for the main thread which
    causes delays for chat. {@link AsyncPlayerChatEvent} is the encouraged
    alternative for thread safe implementations.
"""
class PlayerChatEvent(PlayerEvent, Cancellable):
    handlers: HandlerList = HandlerList()
    cancel: bool
    message: str
    format: str
    recipients: Set[Player]

    def __init__(self, player: Player, message: str) -> None:
        """
        Initializes a PlayerChatEvent with the specified player and message.
        """
        ...

    def __init__(self, player: Player, message: str, format: str, recipients: Set[Player]) -> None:
        """
        Initializes a PlayerChatEvent with the specified player, message, format, and recipients.
        """
        ...

    def isCancelled(self) -> bool:
        """
        Returns whether the event is cancelled.
        """
        ...

    def setCancelled(self, cancel: bool) -> None:
        """
        Sets whether the event is cancelled.
        """
        ...

        def getMessage(self) -> str:
        """
        Gets the message that the player is attempting to send.

        @return Message the player is attempting to send
        """
        ...

    def setMessage(self, message: str) -> None:
        """
        Sets the message that the player will send.

        @param message New message that the player will send
        """
        ...

    def setPlayer(self, player: Player) -> None:
        """
        Sets the player that this message will display as, or command will be
        executed as.

        @param player New player which this event will execute as
        """
        ...

        def getFormat(self) -> str:
        """
        Gets the format to use to display this chat message.

        @return String.Format compatible format string
        """
        ...

    def setFormat(self, format: str) -> None:
        """
        Sets the format to use to display this chat message.

        @param format String.Format compatible format string
        """
        ...

        def getRecipients(self) -> Set[Player]:
        """
        Gets a set of recipients that this chat message will be displayed to.

        @return All Players who will see this chat message
        """
        ...

        def getHandlers(self) -> HandlerList:
        """
        Returns the handler list for this event.
        """
        ...

        @staticmethod
    def getHandlerList() -> HandlerList:
        """
        Returns the static handler list for this event.
        """
        ...
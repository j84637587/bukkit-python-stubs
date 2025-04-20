from typing import Set
from org.bukkit.command import CommandSender
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.event.server import ServerEvent
from org.jetbrains.annotations import NotNull

class BroadcastMessageEvent(ServerEvent, Cancellable):
    """
    Event triggered for server broadcast messages such as from
    {@link org.bukkit.Server#broadcast(String, String)}.

    <b>This event behaves similarly to {@link AsyncPlayerChatEvent} in that it
    should be async if fired from an async thread. Please see that event for
    further information.</b>
    """

    handlers: HandlerList

    def __init__(self, message: str, recipients: Set[CommandSender]) -> None:
        """
        @deprecated since = "1.14"
        """
        self.__init__(False, message, recipients)

    def __init__(self, is_async: bool, message: str, recipients: Set[CommandSender]) -> None:
        ...

        def getMessage(self) -> str:
        """
        Get the message to broadcast.

        @return Message to broadcast
        """
        ...

    def setMessage(self, message: str) -> None:
        """
        Set the message to broadcast.

        @param message New message to broadcast
        """
        ...

        def getRecipients(self) -> Set[CommandSender]:
        """
        Gets a set of recipients that this chat message will be displayed to.
        <p>
        The set returned is not guaranteed to be mutable and may auto-populate
        on access. Any listener accessing the returned set should be aware that
        it may reduce performance for a lazy set implementation.
        <p>
        Listeners should be aware that modifying the list may throw {@link
        UnsupportedOperationException} if the event caller provides an
        unmodifiable set.

        @return All CommandSenders who will see this chat message
        """
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancelled: bool) -> None:
        ...

        def getHandlers(self) -> HandlerList:
        ...

        @staticmethod
    def getHandlerList() -> HandlerList:
        ...
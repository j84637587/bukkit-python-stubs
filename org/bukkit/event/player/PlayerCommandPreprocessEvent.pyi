from typing import Set
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable, HandlerList
from com.google.common.base import Preconditions
from org.jetbrains.annotations import NotNull

class PlayerCommandPreprocessEvent(PlayerEvent, Cancellable):
    """
    This event is called whenever a player runs a command (by placing a slash
    at the start of their message). It is called early in the command handling
    process, and modifications in this event (via {@link #setMessage(String)})
    will be shown in the behavior.
    <p>
    Many plugins will have <b>no use for this event</b>, and you should
    attempt to avoid using it if it is not necessary.
    <p>
    Some examples of valid uses for this event are:
    <ul>
    <li>Logging executed commands to a separate file
    <li>Variable substitution. For example, replacing
        <code>${nearbyPlayer}</code> with the name of the nearest other
        player, or simulating the <code>@a</code> and <code>@p</code>
        decorators used by Command Blocks in plugins that do not handle it.
    <li>Conditionally blocking commands belonging to other plugins. For
        example, blocking the use of the <code>/home</code> command in a
        combat arena.
    <li>Per-sender command aliases. For example, after a player runs the
        command <code>/calias cr gamemode creative</code>, the next time they
        run <code>/cr</code>, it gets replaced into
        <code>/gamemode creative</code>. (Global command aliases should be
        done by registering the alias.)
    </ul>
    <p>
    Examples of incorrect uses are:
    <ul>
    <li>Using this event to run command logic
    </ul>
    <p>
    If the event is cancelled, processing of the command will halt.
    <p>
    The state of whether or not there is a slash (<code>/</code>) at the
    beginning of the message should be preserved. If a slash is added or
    removed, unexpected behavior may result.
    """

    def __init__(self, player: Player, message: str) -> None:
        ...

    def __init__(self, player: Player, message: str, recipients: Set[Player]) -> None:
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...

        def getMessage(self) -> str:
        """
        Gets the command that the player is attempting to send.
        <p>
        All commands begin with a special character; implementations do not
        consider the first character when executing the content.
        <p>
        @return Message the player is attempting to send
        """
        ...

    def setMessage(self, command: str) -> None:
        """
        Sets the command that the player will send.
        <p>
        All commands begin with a special character; implementations do not
        consider the first character when executing the content.
        <p>
        @param command New message that the player will send
        @throws IllegalArgumentException if command is null or empty
        """
        ...

    def setPlayer(self, player: Player) -> None:
        """
        Sets the player that this command will be executed as.
        <p>
        @param player New player which this event will execute as
        @throws IllegalArgumentException if the player provided is null
        """
        ...

        def getRecipients(self) -> Set[Player]:
        """
        Gets a set of recipients that this chat message will be displayed to.
        <p>
        The set returned is not guaranteed to be mutable and may auto-populate
        on access. Any listener accessing the returned set should be aware that
        it may reduce performance for a lazy set implementation. Listeners
        should be aware that modifying the list may throw {@link
        UnsupportedOperationException} if the event caller provides an
        unmodifiable set.
        <p>
        @return All Players who will see this chat message
        @deprecated This method is provided for backward compatibility with no
            guarantee to the effect of viewing or modifying the set.
        """
        ...

        def getHandlers(self) -> HandlerList:
        ...

        @staticmethod
    def getHandlerList() -> HandlerList:
        ...
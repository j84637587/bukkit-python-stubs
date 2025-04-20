from org.bukkit.command import CommandSender
from org.bukkit.event import Cancellable, HandlerList
from typing import Literal

class ServerCommandEvent(ServerEvent, Cancellable):
    """
    This event is called when a command is run by a non-player. It is
    called early in the command handling process, and modifications in this
    event (via {@link #setCommand(String)}) will be shown in the behavior.
    <p>
    Many plugins will have <b>no use for this event</b>, and you should
    attempt to avoid using it if it is not necessary.
    <p>
    Some examples of valid uses for this event are:
    <ul>
    <li>Logging executed commands to a separate file
    <li>Variable substitution. For example, replacing <code>${ip:Steve}</code>
        with the connection IP of the player named Steve, or simulating the
        <code>@a</code> and <code>@p</code> decorators used by Command Blocks
        for plugins that do not handle it.
    <li>Conditionally blocking commands belonging to other plugins.
    <li>Per-sender command aliases. For example, after the console runs the
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

    handlers: HandlerList

    def __init__(self, sender: CommandSender, command: str) -> None:
        """
        Initializes the ServerCommandEvent with the given sender and command.

        :param sender: The command sender
        :param command: The command to execute
        """
        ...

    def getCommand(self) -> str:
        """
        Gets the command that the user is attempting to execute from the
        console

        :return: Command the user is attempting to execute
        """
        ...

    def setCommand(self, message: str) -> None:
        """
        Sets the command that the server will execute

        :param message: New message that the server will execute
        """
        ...

    def getSender(self) -> CommandSender:
        """
        Get the command sender.

        :return: The sender
        """
        ...

    def getHandlers(self) -> HandlerList:
        ...
    
    @staticmethod
    def getHandlerList() -> HandlerList:
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...
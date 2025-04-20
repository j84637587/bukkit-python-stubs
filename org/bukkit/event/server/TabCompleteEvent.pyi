from typing import List
from org.bukkit.command import CommandSender
from org.bukkit.event import Cancellable, Event, HandlerList
from org.jetbrains.annotations import NotNull

class TabCompleteEvent(Event, Cancellable):
    """
    Called when a {@link CommandSender} of any description (ie: player or
    console) attempts to tab complete.
    <br>
    Note that due to client changes, if the sender is a Player, this event will
    only begin to fire once command arguments are specified, not commands
    themselves. Plugins wishing to remove commands from tab completion are
    advised to ensure the client does not have permission for the relevant
    commands, or use {@link PlayerCommandSendEvent}.
    """

    handlers: HandlerList

    def __init__(self, sender: CommandSender, buffer: str, completions: List[str]) -> None:
        """
        Initialize the TabCompleteEvent.

        :param sender: the {@link CommandSender} instance
        :param buffer: command buffer, as entered
        :param completions: a list of offered completions
        """
        ...

        def getSender(self) -> CommandSender:
        """
        Get the sender completing this command.

        :return: the {@link CommandSender} instance
        """
        ...

        def getBuffer(self) -> str:
        """
        Return the entire buffer which formed the basis of this completion.

        :return: command buffer, as entered
        """
        ...

        def getCompletions(self) -> List[str]:
        """
        The list of completions which will be offered to the sender, in order.
        This list is mutable and reflects what will be offered.

        :return: a list of offered completions
        """
        ...

    def setCompletions(self, completions: List[str]) -> None:
        """
        Set the completions offered, overriding any already set.

        :param completions: the new completions
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
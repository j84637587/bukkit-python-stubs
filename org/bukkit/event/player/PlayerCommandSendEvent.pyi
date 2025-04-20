from typing import Collection
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import PlayerEvent
from typing import Any

class PlayerCommandSendEvent(PlayerEvent):
    """
    This event is called when the list of available server commands is sent to
    the player.
    <br>
    Commands may be removed from display using this event, but implementations
    are not required to securely remove all traces of the command. If secure
    removal of commands is required, then the command should be assigned a
    permission which is not granted to the player.
    """

    handlers: HandlerList = HandlerList()
    commands: Collection[str]

    def __init__(self, player: Player, commands: Collection[str]) -> None:
        """
        Initializes the PlayerCommandSendEvent with the specified player and commands.

        :param player: The player to whom the commands are sent.
        :param commands: The collection of commands to be sent.
        """
        super().__init__(player)
        self.commands = commands

    """
    Returns a mutable collection of all top level commands to be sent.
    <br>
    It is not legal to add entries to this collection, only remove them.
    Behaviour of adding entries is undefined.

    :return: collection of all commands
    """
    def getCommands(self) -> Collection[str]:
        ...

    def getHandlers(self) -> HandlerList:
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        ...
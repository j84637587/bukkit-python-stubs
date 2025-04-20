from org.bukkit.command import CommandSender
from org.bukkit.event import HandlerList
from org.bukkit.event.server import ServerCommandEvent
from typing import Any

class RemoteServerCommandEvent(ServerCommandEvent):
    """
    This event is called when a command is received over RCON. See the javadocs
    of {@link ServerCommandEvent} for more information.
    """

    handlers: HandlerList = HandlerList()

    def __init__(self, sender: CommandSender, command: str) -> None:
        super().__init__(sender, command)

    def get_handlers(self) -> HandlerList:
        return self.handlers

    @staticmethod
    def get_handler_list() -> HandlerList:
        return RemoteServerCommandEvent.handlers
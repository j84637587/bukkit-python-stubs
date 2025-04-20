from org.bukkit.command import CommandSender
from typing import Protocol

class ProxiedCommandSender(Protocol):
    """
    Interface for a proxied command sender.
    """

    def get_caller(self) -> CommandSender:
        """
        Returns the CommandSender which triggered this proxied command.

        Returns:
            CommandSender: the caller which triggered the command.
        """

    def get_callee(self) -> CommandSender:
        """
        Returns the CommandSender which is being used to call the command.

        Returns:
            CommandSender: the caller which the command is being run as.
        """
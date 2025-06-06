from org.bukkit.command import Command
from org.bukkit.command import CommandSender
from typing import List

class CommandExecutor:
    """
    Represents a class which contains a single method for executing commands
    """

    def on_command(self, sender: CommandSender, command: Command, label: str, args: List[str]) -> bool:
        """
        Executes the given command, returning its success.
        <br>
        If false is returned, then the "usage" plugin.yml entry for this command
        (if defined) will be sent to the player.

        :param sender: Source of the command
        :param command: Command which was executed
        :param label: Alias of the command which was used
        :param args: Passed command arguments
        :return: true if a valid command, otherwise false
        """
        ...
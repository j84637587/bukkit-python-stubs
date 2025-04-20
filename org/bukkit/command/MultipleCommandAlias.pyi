from typing import List
from org.bukkit.command import Command
from org.bukkit.command import CommandSender
from org.jetbrains.annotations import NotNull

class MultipleCommandAlias(Command):
    """
    Represents a command that delegates to one or more other commands
    """

    def __init__(self, name: str, commands: List[Command]) -> None:
        ...

        def get_commands(self) -> List[Command]:
        """
        Gets the commands associated with the multi-command alias.

        :return: commands associated with alias
        """
        ...

    def execute(self, sender: CommandSender, command_label: str, args: List[str]) -> bool:
        ...
from typing import List
from org.bukkit.command import Command
from org.bukkit import Bukkit
from org.jetbrains.annotations import NotNull
from org.bukkit.command import CommandSender

class FormattedCommandAlias(Command):
    """
    Represents a command alias that can format commands based on given format strings.
    """

    def __init__(self, alias: str, format_strings: List[str]) -> None:
        """
        Initializes a new FormattedCommandAlias.

        :param alias: The alias for the command.
        :param format_strings: The format strings to use for the command.
        """
        ...

    def execute(self, sender: CommandSender, command_label: str, args: List[str]) -> bool:
        """
        Executes the command with the given sender, command label, and arguments.

        :param sender: The sender of the command.
        :param command_label: The label of the command.
        :param args: The arguments for the command.
        :return: True if the command was successfully executed, False otherwise.
        """
        ...

    def build_command(self, format_string: str, args: List[str]) -> str:
        """
        Builds the command string based on the format string and arguments.

        :param format_string: The format string to build the command from.
        :param args: The arguments to replace in the format string.
        :return: The built command string.
        """
        ...

    @staticmethod
    def in_range(i: int, j: int, k: int) -> bool:
        """
        Checks if a number is within a specified range.

        :param i: The number to check.
        :param j: The lower bound of the range.
        :param k: The upper bound of the range.
        :return: True if the number is within the range, False otherwise.
        """
        ...
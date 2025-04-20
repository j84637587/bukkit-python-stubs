from typing import List
from org.bukkit.command import Command
from org.jetbrains.annotations import NotNull

class BukkitCommand(Command):
    """Abstract class representing a Bukkit command."""

    def __init__(self, name: str) -> None:
        """Initialize a BukkitCommand with a name.

        Args:
            name (str): The name of the command.
        """
        ...

    def __init__(self, name: str, description: str, usage_message: str, aliases: List[str]) -> None:
        """Initialize a BukkitCommand with a name, description, usage message, and aliases.

        Args:
            name (str): The name of the command.
            description (str): The description of the command.
            usage_message (str): The usage message for the command.
            aliases (List[str]): A list of aliases for the command.
        """
        ...
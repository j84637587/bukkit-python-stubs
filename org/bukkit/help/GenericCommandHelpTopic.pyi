from typing import List, Optional
from org.bukkit.command import Command
from org.bukkit.command import CommandSender
from org.bukkit.command import ConsoleCommandSender
from org.bukkit.help import HelpTopic
from org.jetbrains.annotations import NotNull

"""
Lacking an alternative, the help system will create instances of
GenericCommandHelpTopic for each command in the server's CommandMap. You
can use this class as a base class for custom help topics, or as an example
for how to write your own.
"""
class GenericCommandHelpTopic(HelpTopic):
    command: Command

    def __init__(self, command: Command) -> None:
        ...

    def can_see(self, sender: CommandSender) -> bool:
        ...
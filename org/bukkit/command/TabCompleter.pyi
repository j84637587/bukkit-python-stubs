from typing import List, Optional
from org.bukkit.command import CommandSender, Command

class TabCompleter:
    """
    Represents a class which can suggest tab completions for commands.
    """

    def on_tab_complete(
        self,
        sender: CommandSender,
        command: Command,
        label: str,
        args: List[str]
    ) -> Optional[List[str]]:
        """
        Requests a list of possible completions for a command argument.

        :param sender: Source of the command. For players tab-completing a
                       command inside of a command block, this will be the player, not
                       the command block.
        :param command: Command which was executed
        :param label: Alias of the command which was used
        :param args: The arguments passed to the command, including final
                     partial argument to be completed
        :return: A List of possible completions for the final argument, or None
                 to default to the command executor
        """
        ...
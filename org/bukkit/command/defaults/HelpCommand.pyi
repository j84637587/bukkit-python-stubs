from typing import List, Optional, Dict, Set
from org.bukkit.command import CommandSender, ConsoleCommandSender
from org.bukkit import Bukkit, ChatColor
from org.bukkit.help import HelpMap, HelpTopic, HelpTopicComparator, IndexHelpTopic
from org.bukkit.util import ChatPaginator
from com.google.common.base import Joiner, Preconditions
from com.google.common.collect import ImmutableList

class HelpCommand(BukkitCommand):
    """
    Shows the help menu
    """
    
    def __init__(self) -> None:
        """
        Initializes the HelpCommand with default values.
        """
        ...

    def execute(self, sender: CommandSender, current_alias: str, args: List[str]) -> bool:
        """
        Executes the help command.

        :param sender: The command sender.
        :param current_alias: The current alias used for the command.
        :param args: The arguments passed to the command.
        :return: True if the command was executed successfully.
        """
        ...

    def tabComplete(self, sender: CommandSender, alias: str, args: List[str]) -> List[str]:
        """
        Completes the command based on the provided arguments.

        :param sender: The command sender.
        :param alias: The alias used for the command.
        :param args: The arguments passed to the command.
        :return: A list of possible completions.
        """
        ...

    def findPossibleMatches(self, search_string: str) -> Optional[HelpTopic]:
        """
        Finds possible matches for the given search string.

        :param search_string: The string to search for.
        :return: A HelpTopic if matches are found, otherwise None.
        """
        ...

    @staticmethod
    def damerauLevenshteinDistance(s1: Optional[str], s2: Optional[str]) -> int:
        """
        Computes the Damerau-Levenshtein Distance between two strings.

        :param s1: The first string being compared.
        :param s2: The second string being compared.
        :return: The number of substitutions, deletions, insertions, and transpositions required to get from s1 to s2.
        """
        ...
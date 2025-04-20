from typing import Collection, Optional
from org.bukkit.ChatColor import ChatColor
from org.bukkit.command.CommandSender import CommandSender
from org.bukkit.command.ConsoleCommandSender import ConsoleCommandSender
from org.bukkit.entity.Player import Player
from org.bukkit.util.ChatPaginator import ChatPaginator
from org.jetbrains.annotations import NotNull, Nullable

class HelpTopic:
    pass  # Placeholder for the superclass

class IndexHelpTopic(HelpTopic):
    """
    This help topic generates a list of other help topics. This class is useful
    for adding your own index help topics. To enforce a particular order, use a
    sorted collection.
    <p>
    If a preamble is provided to the constructor, that text will be displayed
    before the first item in the index.
    """

    permission: Optional[str]
    preamble: Optional[str]
    allTopics: Collection[HelpTopic]

    def __init__(self: "IndexHelpTopic", 
                 name: str, 
                 shortText: Optional[str], 
                 permission: Optional[str], 
                 topics: Collection[HelpTopic], 
                 preamble: Optional[str] = None) -> None:
        ...

    def setTopicsCollection(self: "IndexHelpTopic", 
                            topics: Collection[HelpTopic]) -> None:
        """
        Sets the contents of the internal allTopics collection.

        @param topics The topics to set.
        """
        ...

    def canSee(self: "IndexHelpTopic", 
               sender: CommandSender) -> bool:
        ...

    def amendCanSee(self: "IndexHelpTopic", 
                    amendedPermission: Optional[str]) -> None:
        ...

    def getFullText(self: "IndexHelpTopic", 
                    sender: CommandSender) -> str:
        ...

    def buildPreamble(self: "IndexHelpTopic", 
                      sender: CommandSender) -> str:
        """
        Builds the topic preamble. Override this method to change how the index
        preamble looks.

        @param sender The command sender requesting the preamble.
        @return The topic preamble.
        """
        ...

    def buildIndexLine(self: "IndexHelpTopic", 
                       sender: CommandSender, 
                       topic: HelpTopic) -> str:
        """
        Builds individual lines in the index topic. Override this method to
        change how index lines are rendered.

        @param sender The command sender requesting the index line.
        @param topic  The topic to render into an index line.
        @return The rendered index line.
        """
        ...
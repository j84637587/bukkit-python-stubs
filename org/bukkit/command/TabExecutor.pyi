from org.bukkit.command import TabCompleter
from org.bukkit.command import CommandExecutor

class TabExecutor(TabCompleter, CommandExecutor):
    """This class is provided as a convenience to implement both TabCompleter and
    CommandExecutor.
    """
    pass
from typing import List
from org.bukkit import Bukkit
from org.bukkit import ChatColor
from org.bukkit.command import CommandSender
from org.bukkit.plugin import Plugin
from org.jetbrains.annotations import NotNull

class PluginsCommand(BukkitCommand):
    def __init__(self: 'PluginsCommand', name: str) -> None:
        """Gets a list of plugins running on the server"""
        ...

    def execute(self: 'PluginsCommand', sender: CommandSender, current_alias: str, args: List[str]) -> bool:
        """Executes the command."""
        ...

    def tabComplete(self: 'PluginsCommand', sender: CommandSender, alias: str, args: List[str]) -> List[str]:
        """Completes the command."""
        ...

    def getPluginList(self: 'PluginsCommand') -> str:
        """Returns a string representation of the plugin list."""
        ...
from typing import List
from org.bukkit import Bukkit
from org.bukkit import ChatColor
from org.bukkit.command import Command
from org.bukkit.command import CommandSender
from org.jetbrains.annotations import NotNull

class ReloadCommand(Command):
    def __init__(self: "ReloadCommand", name: str) -> None:
        """Reloads the server configuration and plugins"""
        ...

    def execute(self: "ReloadCommand", sender: CommandSender, current_alias: str, args: List[str]) -> bool:
        """Executes the reload command"""
        ...

    def tabComplete(self: "ReloadCommand", sender: CommandSender, alias: str, args: List[str]) -> List[str]:
        """Completes the tab for the reload command"""
        ...
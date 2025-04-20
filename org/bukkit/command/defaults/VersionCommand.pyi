from typing import List, Set, Optional
from org.bukkit import Bukkit, ChatColor
from org.bukkit.command import CommandSender
from org.bukkit.plugin import Plugin, PluginDescriptionFile
from org.bukkit.command.defaults import BukkitCommand
from org.jetbrains.annotations import NotNull

class VersionCommand(BukkitCommand):
    def __init__(self: 'VersionCommand', name: str) -> None:
        """Gets the version of this server including any plugins in use."""
        super().__init__(name)
        self.description: str
        self.usageMessage: str
        self.setPermission("bukkit.command.version")
        self.setAliases(["ver", "about"])

    def execute(self: 'VersionCommand', sender: CommandSender, currentAlias: str, args: List[str]) -> bool:
        """Executes the command."""
        ...

    def describeToSender(self: 'VersionCommand', plugin: Plugin, sender: CommandSender) -> None:
        """Describes the plugin to the sender."""
        ...

        def getNameList(self: 'VersionCommand', names: List[str]) -> str:
        """Gets a formatted string of names."""
        ...

        def tabComplete(self: 'VersionCommand', sender: CommandSender, alias: str, args: List[str]) -> List[str]:
        """Completes the tab for the command."""
        ...

    def sendVersion(self: 'VersionCommand', sender: CommandSender) -> None:
        """Sends the version information to the sender."""
        ...

    def obtainVersion(self: 'VersionCommand') -> None:
        """Obtains the version information."""
        ...

    def setVersionMessage(self: 'VersionCommand', msg: str) -> None:
        """Sets the version message."""
        ...

    @staticmethod
    def getDistance(repo: str, hash: str) -> int:
        """Gets the distance from the given repo and hash."""
        ...
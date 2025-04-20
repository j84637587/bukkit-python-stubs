from collections.abc import Collection
from typing import List, Dict, Optional, Union
from org.bukkit.Location import Location
from org.bukkit.Server import Server
from org.bukkit.command.Command import Command
from org.bukkit.command.CommandMap import CommandMap
from org.bukkit.command.defaults.BukkitCommand import BukkitCommand
from org.bukkit.command.defaults.HelpCommand import HelpCommand
from org.bukkit.command.defaults.PluginsCommand import PluginsCommand
from org.bukkit.command.defaults.ReloadCommand import ReloadCommand
from org.bukkit.command.defaults.TimingsCommand import TimingsCommand
from org.bukkit.command.defaults.VersionCommand import VersionCommand
from org.bukkit.entity.Player import Player
from org.bukkit.util.StringUtil import StringUtil
from org.jetbrains.annotations import NotNull, Nullable


class SimpleCommandMap(CommandMap):
    knownCommands: Dict[str, Command]
    server: Server

    def __init__(self, server: Server) -> None:
        """Initializes SimpleCommandMap with the given server."""
        ...

    def setDefaultCommands(self) -> None:
        """Sets the default commands."""
        ...

    def setFallbackCommands(self) -> None:
        """Sets the fallback commands."""
        ...

    def registerAll(self, fallbackPrefix: str, commands: List[Command]) -> None:
        """Registers all commands with the given fallback prefix."""
        ...

    def register(self, fallbackPrefix: str, command: Command) -> bool:
        """Registers a command with the given fallback prefix."""
        ...

    def register(self, label: str, fallbackPrefix: str, command: Command) -> bool:
        """Registers a command with the given label and fallback prefix."""
        ...

    def register(self, label: str, command: Command, isAlias: bool, fallbackPrefix: str) -> bool:
        """Registers a command with the given name if possible."""
        ...

    def dispatch(self, sender: CommandSender, commandLine: str) -> bool:
        """Dispatches the command to the appropriate command handler."""
        ...

    def clearCommands(self) -> None:
        """Clears all registered commands."""
        ...

    def getCommand(self, name: str) -> Optional[Command]:
        """Gets the command with the given name."""
        ...

    def tabComplete(self, sender: CommandSender, cmdLine: str) -> Optional[List[str]]:
        """Completes the command line for tab completion."""
        ...

    def tabComplete(self, sender: CommandSender, cmdLine: str, location: Optional[Location]) -> Optional[List[str]]:
        """Completes the command line for tab completion with a location."""
        ...

    def getCommands(self) -> Collection[Command]:
        """Returns an unmodifiable collection of known commands."""
        ...

    def registerServerAliases(self) -> None:
        """Registers server aliases."""
        ...
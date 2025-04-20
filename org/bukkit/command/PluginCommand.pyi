from typing import List, Optional, Union
from org.bukkit.command import Command, CommandExecutor, TabCompleter, CommandSender, CommandException
from org.bukkit.plugin import Plugin
from com.google.common.base import Preconditions
from org.jetbrains.annotations import NotNull, Nullable

"""
Represents a {@link Command} belonging to a plugin
"""
class PluginCommand(Command, PluginIdentifiableCommand):
    owning_plugin: Plugin
    executor: Optional[CommandExecutor]
    completer: Optional[TabCompleter]

    def __init__(self: 'PluginCommand', name: str, owner: Plugin) -> None:
        ...

    """
    Executes the command, returning its success

    @param sender Source object which is executing this command
    @param commandLabel The alias of the command used
    @param args All arguments passed to the command, split via ' '
    @return true if the command was successful, otherwise false
    """
    def execute(self: 'PluginCommand', sender: CommandSender, command_label: str, args: List[str]) -> bool:
        ...

    """
    Sets the {@link CommandExecutor} to run when parsing this command

    @param executor New executor to run
    """
    def set_executor(self: 'PluginCommand', executor: Optional[CommandExecutor]) -> None:
        ...

    """
    Gets the {@link CommandExecutor} associated with this command

    @return CommandExecutor object linked to this command
    """
        def get_executor(self: 'PluginCommand') -> CommandExecutor:
        ...

    """
    Sets the {@link TabCompleter} to run when tab-completing this command.
    <p>
    If no TabCompleter is specified, and the command's executor implements
    TabCompleter, then the executor will be used for tab completion.

    @param completer New tab completer
    """
    def set_tab_completer(self: 'PluginCommand', completer: Optional[TabCompleter]) -> None:
        ...

    """
    Gets the {@link TabCompleter} associated with this command.

    @return TabCompleter object linked to this command
    """
        def get_tab_completer(self: 'PluginCommand') -> Optional[TabCompleter]:
        ...

    """
    Gets the owner of this PluginCommand

    @return Plugin that owns this command
    """
        def get_plugin(self: 'PluginCommand') -> Plugin:
        ...

    """
    {@inheritDoc}
    <p>
    Delegates to the tab completer if present.
    <p>
    If it is not present or returns null, will delegate to the current
    command executor if it implements {@link TabCompleter}. If a non-null
    list has not been found, will default to standard player name
    completion in {@link
    Command#tabComplete(CommandSender, String, String[])}.
    <p>
    This method does not consider permissions.

    @throws CommandException if the completer or executor throw an
        exception during the process of tab-completing.
    @throws IllegalArgumentException if sender, alias, or args is null
    """
        def tab_complete(self: 'PluginCommand', sender: CommandSender, alias: str, args: List[str]) -> List[str]:
        ...

    def __str__(self: 'PluginCommand') -> str:
        ...
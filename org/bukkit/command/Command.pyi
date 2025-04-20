from typing import List, Optional, Union, Type
from org.bukkit.command import CommandSender, CommandMap
from org.bukkit import Bukkit, ChatColor, GameRule, Location, Server
from org.bukkit.entity import Player
from org.bukkit.entity.minecart import CommandMinecart
from org.bukkit.permissions import Permissible
from org.jetbrains.annotations import NotNull, Nullable

"""
Represents a Command, which executes various tasks upon user input
"""

class Command:
    def __init__(self, name: str) -> None: ...
    def __init__(
        self, name: str, description: str, usage_message: str, aliases: List[str]
    ) -> None: ...

    """
    Executes the command, returning its success

    @param sender Source object which is executing this command
    @param command_label The alias of the command used
    @param args All arguments passed to the command, split via ' '
    @return true if the command was successful, otherwise false
    """
    def execute(
        self, sender: CommandSender, command_label: str, args: List[str]
    ) -> bool: ...

    """
    Executed on tab completion for this command, returning a list of
    options the player can tab through.

    @param sender Source object which is executing this command
    @param alias the alias being used
    @param args All arguments passed to the command, split via ' '
    @return a list of tab-completions for the specified arguments. This
        will never be null. List may be immutable.
    @throws IllegalArgumentException if sender, alias, or args is null
    """
    def tab_complete(
        self, sender: CommandSender, alias: str, args: List[str]
    ) -> List[str]: ...

    """
    Executed on tab completion for this command, returning a list of
    options the player can tab through.

    @param sender Source object which is executing this command
    @param alias the alias being used
    @param args All arguments passed to the command, split via ' '
    @param location The position looked at by the sender, or null if none
    @return a list of tab-completions for the specified arguments. This
        will never be null. List may be immutable.
    @throws IllegalArgumentException if sender, alias, or args is null
    """
    def tab_complete(
        self,
        sender: CommandSender,
        alias: str,
        args: List[str],
        location: Optional[Location],
    ) -> List[str]: ...

    """
    Returns the name of this command

    @return Name of this command
    """
    def get_name(self) -> str: ...

    """
    Sets the name of this command.
    <p>
    May only be used before registering the command.
    Will return true if the new name is set, and false
    if the command has already been registered.

    @param name New command name
    @return returns true if the name change happened instantly or false if
        the command has already been registered
    """
    def set_name(self, name: str) -> bool: ...

    """
    Gets the permission required by users to be able to perform this
    command

    @return Permission name, or null if none
    """
    def get_permission(self) -> Optional[str]: ...

    """
    Sets the permission required by users to be able to perform this
    command

    @param permission Permission name or null
    """
    def set_permission(self, permission: Optional[str]) -> None: ...

    """
    Tests the given {@link CommandSender} to see if they can perform this
    command.
    <p>
    If they do not have permission, they will be informed that they cannot
    do this.

    @param target User to test
    @return true if they can use it, otherwise false
    """
    def test_permission(self, target: CommandSender) -> bool: ...

    """
    Tests the given {@link CommandSender} to see if they can perform this
    command.
    <p>
    No error is sent to the sender.

    @param target User to test
    @return true if they can use it, otherwise false
    """
    def test_permission_silent(self, target: CommandSender) -> bool: ...

    """
    Returns the label for this command

    @return Label of this command
    """
    def get_label(self) -> str: ...

    """
    Sets the label of this command.
    <p>
    May only be used before registering the command.
    Will return true if the new name is set, and false
    if the command has already been registered.

    @param name The command's name
    @return returns true if the name change happened instantly or false if
        the command was already registered
    """
    def set_label(self, name: str) -> bool: ...

    """
    Registers this command to a CommandMap.
    Once called it only allows changes the registered CommandMap

    @param commandMap the CommandMap to register this command to
    @return true if the registration was successful (the current registered
        CommandMap was the passed CommandMap or null) false otherwise
    """
    def register(self, command_map: CommandMap) -> bool: ...

    """
    Unregisters this command from the passed CommandMap applying any
    outstanding changes

    @param commandMap the CommandMap to unregister
    @return true if the unregistration was successful (the current
        registered CommandMap was the passed CommandMap or null) false
        otherwise
    """
    def unregister(self, command_map: CommandMap) -> bool: ...

    """
    Returns the current registered state of this command

    @return true if this command is currently registered false otherwise
    """
    def is_registered(self) -> bool: ...

    """
    Returns a list of active aliases of this command

    @return List of aliases
    """
    def get_aliases(self) -> List[str]: ...

    """
    Returns a message to be displayed on a failed permission check for this
    command

    @return Permission check failed message
    @deprecated permission messages have not worked for player-executed
    commands since 1.13 as clients without permission to execute a command
    are unaware of its existence and therefore will not send an unknown
    command execution to the server. This message will only ever be shown to
    consoles or when this command is executed with
    {@link Bukkit#dispatchCommand(CommandSender, String)}.
    """
    def get_permission_message(self) -> Optional[str]: ...

    """
    Gets a brief description of this command

    @return Description of this command
    """
    def get_description(self) -> str: ...

    """
    Gets an example usage of this command

    @return One or more example usages
    """
    def get_usage(self) -> str: ...

    """
    Sets the list of aliases to request on registration for this command.
    This is not effective outside of defining aliases in the {@link
    PluginDescriptionFile#getCommands()} (under the
    `<code>aliases</code>' node) is equivalent to this method.

    @param aliases aliases to register to this command
    @return this command object, for chaining
    """
    def set_aliases(self, aliases: List[str]) -> "Command": ...

    """
    Sets a brief description of this command. Defining a description in the
    {@link PluginDescriptionFile#getCommands()} (under the
    `<code>description</code>' node) is equivalent to this method.

    @param description new command description
    @return this command object, for chaining
    """
    def set_description(self, description: str) -> "Command": ...

    """
    Sets the message sent when a permission check fails

    @param permission_message new permission message, null to indicate
        default message, or an empty string to indicate no message
    @return this command object, for chaining
    @deprecated permission messages have not worked for player-executed
    commands since 1.13 as clients without permission to execute a command
    are unaware of its existence and therefore will not send an unknown
    command execution to the server. This message will only ever be shown to
    consoles or when this command is executed with
    {@link Bukkit#dispatchCommand(CommandSender, String)}.
    """
    def set_permission_message(
        self, permission_message: Optional[str]
    ) -> "Command": ...

    """
    Sets the example usage of this command

    @param usage new example usage
    @return this command object, for chaining
    """
    def set_usage(self, usage: str) -> "Command": ...
    @staticmethod
    def broadcast_command_message(source: CommandSender, message: str) -> None: ...
    @staticmethod
    def broadcast_command_message(
        source: CommandSender, message: str, send_to_source: bool
    ) -> None: ...
    def __str__(self) -> str: ...

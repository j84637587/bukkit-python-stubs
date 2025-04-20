from typing import List, Optional
from org.bukkit.command import Command
from org.bukkit.command import CommandSender
from org.bukkit.command import CommandException
from org.bukkit import Location

class CommandMap:
    """
    Interface for CommandMap.
    """

    def register_all(self, fallback_prefix: str, commands: List[Command]) -> None:
        """
        Registers all the commands belonging to a certain plugin.
        <p>
        Caller can use:-
        <ul>
        <li>command.getName() to determine the label registered for this
            command
        <li>command.getAliases() to determine the aliases which where
            registered
        </ul>
        
        @param fallback_prefix: a prefix which is prepended to each command with
            a ':' one or more times to make the command unique
        @param commands: a list of commands to register
        """
        ...

    def register(self, label: str, fallback_prefix: str, command: Command) -> bool:
        """
        Registers a command. Returns true on success; false if name is already
        taken and fallback had to be used.
        <p>
        Caller can use:-
        <ul>
        <li>command.getName() to determine the label registered for this
            command
        <li>command.getAliases() to determine the aliases which where
            registered
        </ul>
        
        @param label: the label of the command, without the '/'-prefix.
        @param fallback_prefix: a prefix which is prepended to the command with a
            ':' one or more times to make the command unique
        @param command: the command to register
        @return: true if command was registered with the passed in label, false
            otherwise, which indicates the fallback_prefix was used one or more
            times
        """
        ...

    def register(self, fallback_prefix: str, command: Command) -> bool:
        """
        Registers a command. Returns true on success; false if name is already
        taken and fallback had to be used.
        <p>
        Caller can use:-
        <ul>
        <li>command.getName() to determine the label registered for this
            command
        <li>command.getAliases() to determine the aliases which where
            registered
        </ul>
        
        @param fallback_prefix: a prefix which is prepended to the command with a
            ':' one or more times to make the command unique
        @param command: the command to register, from which label is determined
            from the command name
        @return: true if command was registered with the passed in label, false
            otherwise, which indicates the fallback_prefix was used one or more
            times
        """
        ...

    def dispatch(self, sender: CommandSender, cmd_line: str) -> bool:
        """
        Looks for the requested command and executes it if found.
        
        @param sender: The command's sender
        @param cmd_line: command + arguments. Example: "/test abc 123"
        @return: returns false if no target is found, true otherwise.
        @throws CommandException: Thrown when the executor for the given command
            fails with an unhandled exception
        """
        ...

    def clear_commands(self) -> None:
        """
        Clears all registered commands.
        """
        ...

    def get_command(self, name: str) -> Optional[Command]:
        """
        Gets the command registered to the specified name
        
        @param name: Name of the command to retrieve
        @return: Command with the specified name or None if a command with that
            label doesn't exist
        """
        ...

    def tab_complete(self, sender: CommandSender, cmd_line: str) -> Optional[List[str]]:
        """
        Looks for the requested command and executes an appropriate
        tab-completer if found. This method will also tab-complete partial
        commands.
        
        @param sender: The command's sender.
        @param cmd_line: The entire command string to tab-complete, excluding
            initial slash.
        @return: a list of possible tab-completions. This list may be immutable.
            Will be None if no matching command of which sender has permission.
        @throws CommandException: Thrown when the tab-completer for the given
            command fails with an unhandled exception
        @throws IllegalArgumentException: if either sender or cmd_line are None
        """
        ...

    def tab_complete(self, sender: CommandSender, cmd_line: str, location: Optional[Location]) -> Optional[List[str]]:
        """
        Looks for the requested command and executes an appropriate
        tab-completer if found. This method will also tab-complete partial
        commands.
        
        @param sender: The command's sender.
        @param cmd_line: The entire command string to tab-complete, excluding
            initial slash.
        @param location: The position looked at by the sender, or None if none
        @return: a list of possible tab-completions. This list may be immutable.
            Will be None if no matching command of which sender has permission.
        @throws CommandException: Thrown when the tab-completer for the given
            command fails with an unhandled exception
        @throws IllegalArgumentException: if either sender or cmd_line are None
        """
        ...
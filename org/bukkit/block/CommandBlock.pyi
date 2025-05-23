from typing import Optional

class CommandBlock:
    """
    Represents a captured state of a command block.
    """

    def get_command(self) -> str:
        """
        Gets the command that this CommandBlock will run when powered.
        This will never return null. If the CommandBlock does not have a
        command, an empty String will be returned instead.

        @return Command that this CommandBlock will run when powered.
        """
        ...

    def set_command(self, command: Optional[str]) -> None:
        """
        Sets the command that this CommandBlock will run when powered.
        Setting the command to null is the same as setting it to an empty
        String.

        @param command Command that this CommandBlock will run when powered.
        """
        ...

    def get_name(self) -> str:
        """
        Gets the name of this CommandBlock. The name is used with commands
        that this CommandBlock executes. This name will never be null, and
        by default is "@".

        @return Name of this CommandBlock.
        """
        ...

    def set_name(self, name: Optional[str]) -> None:
        """
        Sets the name of this CommandBlock. The name is used with commands
        that this CommandBlock executes. Setting the name to null is the
        same as setting it to "@".

        @param name New name for this CommandBlock.
        """
        ...
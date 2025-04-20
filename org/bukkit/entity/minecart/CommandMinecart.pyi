from org.bukkit.entity import Minecart
from typing import Optional

class CommandMinecart(Minecart):
    """
    Interface for CommandMinecart that extends Minecart.
    """

    def get_command(self) -> str:
        """
        Gets the command that this CommandMinecart will run when activated.
        This will never return null. If the CommandMinecart does not have a
        command, an empty String will be returned instead.

        @return: Command that this CommandMinecart will run when powered.
        """
        ...

    def set_command(self, command: Optional[str]) -> None:
        """
        Sets the command that this CommandMinecart will run when activated.
        Setting the command to null is the same as setting it to an empty
        String.

        @param command: Command that this CommandMinecart will run when
                        activated.
        """
        ...

    def set_name(self, name: Optional[str]) -> None:
        """
        Sets the name of this CommandMinecart. The name is used with commands
        that this CommandMinecart executes. Setting the name to null is the
        same as setting it to "@".

        @param name: New name for this CommandMinecart.
        """
        ...
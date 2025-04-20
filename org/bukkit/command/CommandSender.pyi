from typing import Optional, Union
from uuid import UUID
from org.bukkit.Server import Server
from org.bukkit.permissions.Permissible import Permissible

class CommandSender(Permissible):
    """
    Interface representing a command sender.
    """

    def send_message(self, message: str) -> None:
        """
        Sends this sender a message.

        :param message: Message to be displayed
        """
        ...

    def send_message(self, *messages: str) -> None:
        """
        Sends this sender multiple messages.

        :param messages: An array of messages to be displayed
        """
        ...

    def send_message(self, sender: Optional[UUID], message: str) -> None:
        """
        Sends this sender a message.

        :param sender: The sender of this message
        :param message: Message to be displayed
        """
        ...

    def send_message(self, sender: Optional[UUID], *messages: str) -> None:
        """
        Sends this sender multiple messages.

        :param sender: The sender of this message
        :param messages: An array of messages to be displayed
        """
        ...

    def get_server(self) -> Server:
        """
        Returns the server instance that this command is running on.

        :return: Server instance
        """
        ...

    def get_name(self) -> str:
        """
        Gets the name of this command sender.

        :return: Name of the sender
        """
        ...
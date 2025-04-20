from org.bukkit.plugin.messaging import Messenger
from typing import Optional

class MessageTooLargeException(RuntimeError):
    """
    Thrown if a Plugin Message is sent that is too large to be sent.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of MessageTooLargeException with a default message.
        """
        ...

    def __init__(self, message: bytes) -> None:
        """
        Initializes a new instance of MessageTooLargeException with a message of the specified length.

        :param message: The message that was too large.
        """
        ...

    def __init__(self, length: int) -> None:
        """
        Initializes a new instance of MessageTooLargeException with a message indicating the length of the attempted message.

        :param length: The length of the message that was too large.
        """
        ...

    def __init__(self, msg: str) -> None:
        """
        Initializes a new instance of MessageTooLargeException with the specified message.

        :param msg: The detail message.
        """
        ...
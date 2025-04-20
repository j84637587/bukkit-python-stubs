from typing import Optional

class ChannelNameTooLongException(RuntimeError):
    """
    Thrown if a Plugin Channel is too long.
    """
    
    def __init__(self) -> None:
        """
        Initializes the exception with a default message.
        """
        ...

    def __init__(self, channel: str) -> None:
        """
        Initializes the exception with a message that includes the channel name.

        :param channel: The name of the channel that was too long.
        """
        ...
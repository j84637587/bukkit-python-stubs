# channel_not_registered_exception.pyi

from builtins import RuntimeError

class ChannelNotRegisteredException(RuntimeError):
    """
    Thrown if a Plugin attempts to send a message on an unregistered channel.
    """

    def __init__(self) -> None:
        ...

    def __init__(self, channel: str) -> None:
        ...
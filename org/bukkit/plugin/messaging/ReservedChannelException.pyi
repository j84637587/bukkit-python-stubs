# org/bukkit/plugin/messaging/ReservedChannelException.pyi

from builtins import RuntimeError

class ReservedChannelException(RuntimeError):
    """
    Thrown if a plugin attempts to register for a reserved channel (such as
    "REGISTER")
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of ReservedChannelException with a default message.
        """
        ...

    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of ReservedChannelException with a specified channel name.

        :param name: The name of the reserved channel that was attempted to be registered.
        """
        ...
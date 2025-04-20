# org/bukkit/command/CommandException.pyi

from typing import Optional, Type

class CommandException(RuntimeError):
    """
    Thrown when an unhandled exception occurs during the execution of a Command
    """

    def __init__(self, msg: Optional[str] = None) -> None:
        """
        Creates a new instance of <code>CommandException</code> without detail
        message.
        """
        ...

    def __init__(self, msg: str, cause: Optional[Type[BaseException]] = None) -> None:
        """
        Constructs an instance of <code>CommandException</code> with the
        specified detail message.

        :param msg: the detail message.
        :param cause: the cause of the exception.
        """
        ...
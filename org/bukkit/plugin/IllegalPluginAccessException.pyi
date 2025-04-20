# org/bukkit/plugin/IllegalPluginAccessException.pyi

from typing import Optional

class IllegalPluginAccessException(RuntimeError):
    """
    Thrown when a plugin attempts to interact with the server when it is not
    enabled
    """

    def __init__(self, msg: Optional[str] = None) -> None:
        """
        Constructs an instance of <code>IllegalPluginAccessException</code>
        with the specified detail message.

        :param msg: the detail message.
        """
        ...
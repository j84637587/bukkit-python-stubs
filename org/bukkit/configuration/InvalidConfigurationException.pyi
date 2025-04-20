# org/bukkit/configuration/InvalidConfigurationException.pyi

from typing import Optional, Any

class InvalidConfigurationException(Exception):
    """
    Exception thrown when attempting to load an invalid {@link Configuration}
    """

    def __init__(self) -> None:
        """
        Creates a new instance of InvalidConfigurationException without a
        message or cause.
        """
        ...

    def __init__(self, msg: str) -> None:
        """
        Constructs an instance of InvalidConfigurationException with the
        specified message.

        :param msg: The details of the exception.
        """
        ...

    def __init__(self, cause: Exception) -> None:
        """
        Constructs an instance of InvalidConfigurationException with the
        specified cause.

        :param cause: The cause of the exception.
        """
        ...

    def __init__(self, msg: str, cause: Exception) -> None:
        """
        Constructs an instance of InvalidConfigurationException with the
        specified message and cause.

        :param cause: The cause of the exception.
        :param msg: The details of the exception.
        """
        ...
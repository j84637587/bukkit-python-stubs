from typing import Optional, Type

class InvalidDescriptionException(Exception):
    """
    Thrown when attempting to load an invalid PluginDescriptionFile
    """
    serialVersionUID: int = 5721389122281775896

    def __init__(self, cause: Optional[Type[Throwable]], message: Optional[str] = None) -> None:
        """
        Constructs a new InvalidDescriptionException based on the given
        Exception

        :param message: Brief message explaining the cause of the exception
        :param cause: Exception that triggered this Exception
        """
        ...

    def __init__(self, cause: Optional[Type[Throwable]]) -> None:
        """
        Constructs a new InvalidDescriptionException based on the given
        Exception

        :param cause: Exception that triggered this Exception
        """
        ...

    def __init__(self, message: str) -> None:
        """
        Constructs a new InvalidDescriptionException with the given message

        :param message: Brief message explaining the cause of the exception
        """
        ...

    def __init__(self) -> None:
        """
        Constructs a new InvalidDescriptionException
        """
        ...
from typing import Optional, Union

class InvalidPluginException(Exception):
    """
    Thrown when attempting to load an invalid Plugin file
    """
    serialVersionUID: int = -8242141640709409544

    def __init__(self, cause: Optional[Union[Exception, Throwable]] = None) -> None:
        """
        Constructs a new InvalidPluginException based on the given Exception

        :param cause: Exception that triggered this Exception
        """
        ...

    def __init__(self) -> None:
        """
        Constructs a new InvalidPluginException
        """
        ...

    def __init__(self, message: str, cause: Optional[Union[Exception, Throwable]] = None) -> None:
        """
        Constructs a new InvalidPluginException with the specified detail
        message and cause.

        :param message: the detail message (which is saved for later retrieval
                        by the getMessage() method).
        :param cause: the cause (which is saved for later retrieval by the
                      getCause() method). (A null value is permitted, and indicates that
                      the cause is nonexistent or unknown.)
        """
        ...

    def __init__(self, message: str) -> None:
        """
        Constructs a new InvalidPluginException with the specified detail
        message

        :param message: The detail message is saved for later retrieval by the
                        getMessage() method.
        """
        ...
from typing import Optional, Union

class UnknownDependencyException(RuntimeError):
    """
    Thrown when attempting to load an invalid Plugin file
    """

    def __init__(self, throwable: Optional[Union[Throwable, str]] = None, message: Optional[str] = None) -> None:
        """
        Constructs a new UnknownDependencyException based on the given
        Exception

        :param throwable: Exception that triggered this Exception
        :param message: Brief message explaining the cause of the exception
        """
        ...

    def __init__(self, message: str) -> None:
        """
        Constructs a new UnknownDependencyException with the given message

        :param message: Brief message explaining the cause of the exception
        """
        ...

    def __init__(self, throwable: Throwable, message: str) -> None:
        """
        Constructs a new UnknownDependencyException based on the given
        Exception

        :param message: Brief message explaining the cause of the exception
        :param throwable: Exception that triggered this Exception
        """
        ...

    def __init__(self) -> None:
        """
        Constructs a new UnknownDependencyException
        """
        ...
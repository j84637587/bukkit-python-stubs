from typing import Optional, Union

class EventException(Exception):
    """
    Constructs a new EventException based on the given Exception

    @param throwable Exception that triggered this Exception
    """
    def __init__(self, throwable: Optional[Throwable] = None) -> None: ...

    """
    Constructs a new EventException
    """
    def __init__(self) -> None: ...

    """
    Constructs a new EventException with the given message

    @param cause The exception that caused this
    @param message The message
    """
    def __init__(self, cause: Optional[Throwable], message: str) -> None: ...

    """
    Constructs a new EventException with the given message

    @param message The message
    """
    def __init__(self, message: str) -> None: ...

    """
    If applicable, returns the Exception that triggered this Exception

    @return Inner exception, or null if one does not exist
    """
    def get_cause(self) -> Optional[Throwable]: ...
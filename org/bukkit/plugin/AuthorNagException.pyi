# org/bukkit/plugin/AuthorNagException.pyi

from typing import Optional

class AuthorNagException(RuntimeError):
    """
    Constructs a new AuthorNagException based on the given Exception

    :param message: Brief message explaining the cause of the exception
    """
    def __init__(self, message: str) -> None: ...
    
    def get_message(self) -> str: ...
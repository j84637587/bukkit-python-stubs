from typing import Protocol

class Flying(Protocol):
    pass

class Enemy(Protocol):
    pass

class Phantom(Flying, Enemy):
    """
    Represents a phantom.
    """

    def get_size(self) -> int:
        """
        @return The size of the phantom
        """
        ...

    def set_size(self, sz: int) -> None:
        """
        @param sz The new size of the phantom.
        """
        ...
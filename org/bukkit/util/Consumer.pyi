from typing import TypeVar, Protocol

T = TypeVar('T')

class Consumer(Protocol[T]):
    """
    Represents an operation that accepts a single input argument and returns no
    result.

    Attributes:
        T: the type of the input to the operation
    """

    def accept(self, t: T) -> None:
        """
        Performs this operation on the given argument.

        Args:
            t: the input argument
        """
        ...
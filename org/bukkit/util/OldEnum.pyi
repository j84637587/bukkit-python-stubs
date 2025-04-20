from typing import TypeVar, Protocol

T = TypeVar('T', bound='OldEnum')

class OldEnum(Protocol[T]):
    """
    Class which holds common methods which are present in an enum.

    @param <T> the type of the old enum.
    @deprecated only for backwards compatibility.
    """

    def compare_to(self, other: T) -> int:
        """
        @param other to compare to.
        @return negative if this old enum is lower, zero if equal and positive if
        higher than the given old enum.
        @deprecated only for backwards compatibility, old enums can not be
        compared.
        """
        ...

    def name(self) -> str:
        """
        @return the name of the old enum.
        @deprecated only for backwards compatibility.
        """
        ...

    def ordinal(self) -> int:
        """
        @return the ordinal of the old enum.
        @deprecated only for backwards compatibility, it is not guaranteed that
        an old enum always has the same ordinal.
        """
        ...
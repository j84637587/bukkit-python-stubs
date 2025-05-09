from typing import Collection, Iterable, TypeVar

T = TypeVar('T', bound=Collection)

class StringUtil:
    """
    Utility class for string operations.
    """

    @staticmethod
    def copy_partial_matches(token: str, originals: Iterable[str], collection: T) -> T:
        """
        Copies all elements from the iterable collection of originals to the
        collection provided.

        Args:
            token: String to search for.
            originals: An iterable collection of strings to filter.
            collection: The collection to add matches to.

        Returns:
            The collection provided that would have the elements copied into.

        Raises:
            UnsupportedOperationException: if the collection is immutable
                and originals contains a string which starts with the specified
                search string.
            IllegalArgumentException: if any parameter is null.
            IllegalArgumentException: if originals contains a null element.
                Note: the collection may be modified before this is thrown.
        """
        ...

    @staticmethod
    def starts_with_ignore_case(string: str, prefix: str) -> bool:
        """
        This method uses a region to check case-insensitive equality. This
        means the internal array does not need to be copied like a
        toLowerCase() call would.

        Args:
            string: String to check.
            prefix: Prefix of string to compare.

        Returns:
            True if provided string starts with, ignoring case, the prefix
            provided.

        Raises:
            NullPointerException: if prefix is null.
            IllegalArgumentException: if string is null.
        """
        ...
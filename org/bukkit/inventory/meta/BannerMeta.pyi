from typing import List
from org.bukkit.block.banner import Pattern

class BannerMeta:
    """
    Interface for BannerMeta.
    """

    def get_patterns(self) -> List[Pattern]:
        """
        Returns a list of patterns on this banner

        Returns:
            List[Pattern]: the patterns
        """
        ...

    def set_patterns(self, patterns: List[Pattern]) -> None:
        """
        Sets the patterns used on this banner

        Args:
            patterns (List[Pattern]): the new list of patterns
        """
        ...

    def add_pattern(self, pattern: Pattern) -> None:
        """
        Adds a new pattern on top of the existing patterns

        Args:
            pattern (Pattern): the new pattern to add
        """
        ...

    def get_pattern(self, i: int) -> Pattern:
        """
        Returns the pattern at the specified index

        Args:
            i (int): the index

        Returns:
            Pattern: the pattern

        Raises:
            IndexError: when index is not in [0, numberOfPatterns()) range
        """
        ...

    def remove_pattern(self, i: int) -> Pattern:
        """
        Removes the pattern at the specified index

        Args:
            i (int): the index

        Returns:
            Pattern: the removed pattern

        Raises:
            IndexError: when index is not in [0, numberOfPatterns()) range
        """
        ...

    def set_pattern(self, i: int, pattern: Pattern) -> None:
        """
        Sets the pattern at the specified index

        Args:
            i (int): the index
            pattern (Pattern): the new pattern

        Raises:
            IndexError: when index is not in [0, numberOfPatterns()) range
        """
        ...

    def number_of_patterns(self) -> int:
        """
        Returns the number of patterns on this banner

        Returns:
            int: the number of patterns
        """
        ...
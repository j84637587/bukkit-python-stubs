from typing import List
from .dye_color import DyeColor
from .pattern import Pattern

class Banner:
    """
    Represents a captured state of a banner.
    """

    def get_base_color(self) -> DyeColor:
        """
        Returns the base color for this banner

        Returns:
            DyeColor: the base color
        """
        ...

    def set_base_color(self, color: DyeColor) -> None:
        """
        Sets the base color for this banner.
        <b>Only valid for shield pseudo banners, otherwise base depends on block
        type</b>

        Args:
            color (DyeColor): the base color
        """
        ...

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
        Adds a new pattern on top of the existing
        patterns

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
        """
        ...

    def remove_pattern(self, i: int) -> Pattern:
        """
        Removes the pattern at the specified index

        Args:
            i (int): the index

        Returns:
            Pattern: the removed pattern
        """
        ...

    def set_pattern(self, i: int, pattern: Pattern) -> None:
        """
        Sets the pattern at the specified index

        Args:
            i (int): the index
            pattern (Pattern): the new pattern
        """
        ...

    def number_of_patterns(self) -> int:
        """
        Returns the number of patterns on this
        banner

        Returns:
            int: the number of patterns
        """
        ...
from org.bukkit.material import Colorable
from typing import List

class SignSide(Colorable):
    """
    Represents a side of a sign.
    """

    def get_lines(self) -> List[str]:
        """
        Gets all the lines of text currently on this side of the sign.

        :return: Array of Strings containing each line of text
        """
        ...

    def get_line(self, index: int) -> str:
        """
        Gets the line of text at the specified index on this side of the sign.
        <p>
        For example, getLine(0) will return the first line of text.

        :param index: Line number to get the text from, starting at 0
        :return: Text on the given line
        :raises IndexError: Thrown when the line does not exist
        """
        ...

    def set_line(self, index: int, line: str) -> None:
        """
        Sets the line of text at the specified index on this side of the sign.
        <p>
        For example, setLine(0, "Line One") will set the first line of text to
        "Line One".

        :param index: Line number to set the text at, starting from 0
        :param line: New text to set at the specified index
        :raises IndexError: If the index is out of the range 0..3
        """
        ...

    def is_glowing_text(self) -> bool:
        """
        Gets whether this side of the sign has glowing text.

        :return: if this side of the sign has glowing text
        """
        ...

    def set_glowing_text(self, glowing: bool) -> None:
        """
        Sets whether this side of the sign has glowing text.

        :param glowing: if this side of the sign has glowing text
        """
        ...
from typing import List, Optional

from org.bukkit import ChatColor

class ChatPaginator:
    GUARANTEED_NO_WRAP_CHAT_PAGE_WIDTH: int = 55
    AVERAGE_CHAT_PAGE_WIDTH: int = 65
    UNBOUNDED_PAGE_WIDTH: int = 2147483647  # Integer.MAX_VALUE
    OPEN_CHAT_PAGE_HEIGHT: int = 20
    CLOSED_CHAT_PAGE_HEIGHT: int = 10
    UNBOUNDED_PAGE_HEIGHT: int = 2147483647  # Integer.MAX_VALUE

    """
    The ChatPaginator takes a raw string of arbitrary length and breaks it down
    into an array of strings appropriate for displaying on the Minecraft player
    console.
    """

    @staticmethod
    def paginate(unpaginated_string: Optional[str], page_number: int) -> 'ChatPage':
        """
        Breaks a raw string up into pages using the default width and height.

        :param unpaginated_string: The raw string to break.
        :param page_number: The page number to fetch.
        :return: A single chat page.
        """
        ...

    @staticmethod
    def paginate(unpaginated_string: Optional[str], page_number: int, line_length: int, page_height: int) -> 'ChatPage':
        """
        Breaks a raw string up into pages using a provided width and height.

        :param unpaginated_string: The raw string to break.
        :param page_number: The page number to fetch.
        :param line_length: The desired width of a chat line.
        :param page_height: The desired number of lines in a page.
        :return: A single chat page.
        """
        ...

    @staticmethod
    def word_wrap(raw_string: Optional[str], line_length: int) -> List[str]:
        """
        Breaks a raw string up into a series of lines. Words are wrapped using
        spaces as decimeters and the newline character is respected.

        :param raw_string: The raw string to break.
        :param line_length: The length of a line of text.
        :return: An array of word-wrapped lines.
        """
        ...

class ChatPage:
    lines: List[str]
    page_number: int
    total_pages: int

    def __init__(self, lines: List[str], page_number: int, total_pages: int) -> None:
        ...
    
    def get_page_number(self) -> int:
        ...
    
    def get_total_pages(self) -> int:
        ...
    
    def get_lines(self) -> List[str]:
        ...
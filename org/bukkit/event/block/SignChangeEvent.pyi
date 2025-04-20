from org.bukkit.block import Block
from org.bukkit.block.sign import Side
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable, HandlerList
from typing import List, Optional

class SignChangeEvent(BlockEvent, Cancellable):
    """
    Called when a sign is changed by a player.
    <p>
    If a Sign Change event is cancelled, the sign will not be changed.
    """

    handlers: HandlerList

    def __init__(self, the_block: Block, the_player: Player, the_lines: List[str], side: Side) -> None:
        ...

    @classmethod
    def get_handler_list(cls) -> HandlerList:
        ...

    @Deprecated(since="1.19.4")
    def __init__(self, the_block: Block, the_player: Player, the_lines: List[str]) -> None:
        ...

    def get_player(self) -> Player:
        """
        Gets the player changing the sign involved in this event.

        @return: the Player involved in this event
        """
        ...

    def get_lines(self) -> List[str]:
        """
        Gets all of the lines of text from the sign involved in this event.

        @return: the String array for the sign's lines new text
        """
        ...

    def get_line(self, index: int) -> Optional[str]:
        """
        Gets a single line of text from the sign involved in this event.

        @param index: index of the line to get
        @return: the String containing the line of text associated with the
            provided index
        @raises IndexOutOfBoundsException: thrown when the provided index is > 3 or < 0
        """
        ...

    def set_line(self, index: int, line: Optional[str]) -> None:
        """
        Sets a single line for the sign involved in this event

        @param index: index of the line to set
        @param line: text to set
        @raises IndexOutOfBoundsException: thrown when the provided index is > 3 or < 0
        """
        ...

    def get_side(self) -> Side:
        """
        Returns which side is changed.

        @return: the affected side of the sign
        """
        ...

    def is_cancelled(self) -> bool:
        ...

    def set_cancelled(self, cancel: bool) -> None:
        ...

    def get_handlers(self) -> HandlerList:
        ...
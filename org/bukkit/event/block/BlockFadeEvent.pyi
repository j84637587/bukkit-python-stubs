from org.bukkit.block import Block
from org.bukkit.block import BlockState
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.block import BlockEvent
from typing import Any

class BlockFadeEvent(BlockEvent, Cancellable):
    """
    Called when a block fades, melts or disappears based on world conditions
    <p>
    Examples:
    <ul>
    <li>Snow melting due to being near a light source.
    <li>Ice melting due to being near a light source.
    <li>Fire burning out after time, without destroying fuel block.
    <li>Coral fading to dead coral due to lack of water</li>
    <li>Turtle Egg bursting when a turtle hatches</li>
    </ul>
    <p>
    If a Block Fade event is cancelled, the block will not fade, melt or
    disappear.
    """

    handlers: HandlerList

    def __init__(self, block: Block, new_state: BlockState) -> None:
        """
        Initializes the BlockFadeEvent.

        :param block: The block that is fading, melting or disappearing.
        :param new_state: The new state of the block.
        """
        ...

    def get_new_state(self) -> BlockState:
        """
        Gets the state of the block that will be fading, melting or
        disappearing.

        :return: The block state of the block that will be fading, melting or
            disappearing.
        """
        ...

    def is_cancelled(self) -> bool:
        """
        Checks if the event is cancelled.

        :return: True if the event is cancelled, otherwise False.
        """
        ...

    def set_cancelled(self, cancel: bool) -> None:
        """
        Sets whether the event is cancelled.

        :param cancel: True to cancel the event, otherwise False.
        """
        ...

    def get_handlers(self) -> HandlerList:
        """
        Gets the handlers for this event.

        :return: The handler list for this event.
        """
        ...

    @staticmethod
    def get_handler_list() -> HandlerList:
        """
        Gets the static handler list for this event.

        :return: The static handler list for this event.
        """
        ...
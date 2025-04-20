from org.bukkit.block import Block
from org.bukkit.event import Event
from typing import Any
from typing import Optional

class BlockEvent(Event):
    """
    Represents a block related event.
    """

    def __init__(self, the_block: Block) -> None:
        """
        Initializes the BlockEvent with the specified block.

        :param the_block: The Block which is involved in this event.
        """
        ...

    def get_block(self) -> Block:
        """
        Gets the block involved in this event.

        :return: The Block which block is involved in this event.
        """
        ...
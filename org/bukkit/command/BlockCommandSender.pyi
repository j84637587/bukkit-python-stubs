from org.bukkit.block import Block
from org.bukkit.command import CommandSender
from typing import Protocol

class BlockCommandSender(CommandSender, Protocol):
    """
    Interface for a command sender that is associated with a block.
    """

    def get_block(self) -> Block:
        """
        Returns the block this command sender belongs to.

        Returns:
            Block: for the command sender.
        """
        ...
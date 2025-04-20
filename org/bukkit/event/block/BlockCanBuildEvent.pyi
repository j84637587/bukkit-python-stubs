from org.bukkit.Material import Material
from org.bukkit.block import Block
from org.bukkit.block.data import BlockData
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.block import BlockEvent
from typing import Optional

class BlockCanBuildEvent(BlockEvent):
    """
    Called when we try to place a block, to see if we can build it here or not.
    <p>
    Note:
    <ul>
    <li>The Block returned by getBlock() is the block we are trying to place
        on, not the block we are trying to place.
    <li>If you want to figure out what is being placed, use {@link
        #getMaterial()} instead.
    </ul>
    """

    handlers: HandlerList

    def __init__(self, block: Block, type: BlockData, can_build: bool) -> None:
        """
        @param block the block involved in this event
        @param player the player placing the block
        @param type the id of the block to place
        @param canBuild whether we can build
        """
        ...

    def is_buildable(self) -> bool:
        """
        Gets whether or not the block can be built here.
        <p>
        By default, returns Minecraft's answer on whether the block can be
        built here or not.

        @return boolean whether or not the block can be built
        """
        ...

    def set_buildable(self, cancel: bool) -> None:
        """
        Sets whether the block can be built here or not.

        @param cancel true if you want to allow the block to be built here
            despite Minecraft's default behaviour
        """
        ...

    def get_material(self) -> Material:
        """
        Gets the Material that we are trying to place.

        @return The Material that we are trying to place
        """
        ...

    def get_block_data(self) -> BlockData:
        """
        Gets the BlockData that we are trying to place.

        @return The BlockData that we are trying to place
        """
        ...

    def get_player(self) -> Optional[Player]:
        """
        Gets the player who placed the block involved in this event.
        <br>
        May be null for legacy calls of the event.

        @return The Player who placed the block involved in this event
        """
        ...

    @classmethod
    def get_handlers(cls) -> HandlerList:
        ...

    @classmethod
    def get_handler_list(cls) -> HandlerList:
        ...
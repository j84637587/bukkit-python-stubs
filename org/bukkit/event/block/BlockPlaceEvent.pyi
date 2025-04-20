from org.bukkit.block import Block
from org.bukkit.block import BlockState
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.inventory import EquipmentSlot
from org.bukkit.inventory import ItemStack
from typing import Any

class BlockPlaceEvent(BlockEvent, Cancellable):
    """
    Called when a block is placed by a player.
    <p>
    If a Block Place event is cancelled, the block will not be placed.
    """

    handlers: HandlerList

    def __init__(self, placed_block: Block, replaced_block_state: BlockState, placed_against: Block, 
                 item_in_hand: ItemStack, the_player: Player, can_build: bool, hand: EquipmentSlot) -> None:
        ...

    @classmethod
    def get_handler_list(cls) -> HandlerList:
        ...

    def is_cancelled(self) -> bool:
        ...

    def set_cancelled(self, cancel: bool) -> None:
        ...

    def get_player(self) -> Player:
        """
        Gets the player who placed the block involved in this event.

        @return: The Player who placed the block involved in this event
        """
        ...

    def get_block_placed(self) -> Block:
        """
        Clarity method for getting the placed block. Not really needed except
        for reasons of clarity.

        @return: The Block that was placed
        """
        ...

    def get_block_replaced_state(self) -> BlockState:
        """
        Gets the BlockState for the block which was replaced. Material type air
        mostly.

        @return: The BlockState for the block which was replaced.
        """
        ...

    def get_block_against(self) -> Block:
        """
        Gets the block that this block was placed against

        @return: Block the block that the new block was placed against
        """
        ...

    def get_item_in_hand(self) -> ItemStack:
        """
        Gets the item in the player's hand when they placed the block.

        @return: The ItemStack for the item in the player's hand when they
            placed the block
        """
        ...

    def get_hand(self) -> EquipmentSlot:
        """
        Gets the hand which placed the block
        @return: Main or off-hand, depending on which hand was used to place the block
        """
        ...

    def can_build(self) -> bool:
        """
        Gets the value whether the player would be allowed to build here.
        Defaults to spawn if the server was going to stop them (such as, the
        player is in Spawn). Note that this is an entirely different check
        than BLOCK_CANBUILD, as this refers to a player, not universe-physics
        rule like cactus on dirt.

        @return: boolean whether the server would allow a player to build here
        """
        ...

    def set_build(self, can_build: bool) -> None:
        """
        Sets the canBuild state of this event. Set to true if you want the
        player to be able to build.

        @param can_build: true if you want the player to be able to build
        """
        ...
from typing import List
from org.bukkit.block import Block
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.inventory import EquipmentSlot, ItemStack
from org.jetbrains.annotations import NotNull

class PlayerHarvestBlockEvent(PlayerEvent, Cancellable):
    """
    This event is called whenever a player harvests a block.
    <br>
    A 'harvest' is when a block drops an item (usually some sort of crop) and
    changes state, but is not broken in order to drop the item.
    <br>
    This event is not called for when a block is broken, to handle that, listen
    for {@link org.bukkit.event.block.BlockBreakEvent} and
    {@link org.bukkit.event.block.BlockDropItemEvent}.
    """

    handlers: HandlerList
    cancel: bool
    harvested_block: Block
    hand: EquipmentSlot
    items_harvested: List[ItemStack]

    def __init__(self, player: Player, harvested_block: Block, hand: EquipmentSlot, items_harvested: List[ItemStack]) -> None:
        ...

    @classmethod
    def __init__(self, player: Player, harvested_block: Block, items_harvested: List[ItemStack]) -> None:
        ...

        def get_harvested_block(self) -> Block:
        """
        Gets the block that is being harvested.

        @return The block that is being harvested
        """
        ...

        def get_hand(self) -> EquipmentSlot:
        """
        Get the hand used to harvest the block.

        @return the hand
        """
        ...

        def get_items_harvested(self) -> List[ItemStack]:
        """
        Gets a list of items that are being harvested from this block.

        @return A list of items that are being harvested from this block
        """
        ...

    def is_cancelled(self) -> bool:
        ...

    def set_cancelled(self, cancel: bool) -> None:
        ...

        def get_handlers(self) -> HandlerList:
        ...

        @classmethod
    def get_handler_list(cls) -> HandlerList:
        ...
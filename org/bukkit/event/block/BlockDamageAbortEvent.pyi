from org.bukkit.block import Block
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.inventory import ItemStack
from typing import Any

class BlockDamageAbortEvent(BlockEvent):
    """
    Called when a player stops damaging a Block.
    @see BlockDamageEvent
    """

    handlers: HandlerList = HandlerList()
    player: Player
    itemstack: ItemStack

    def __init__(self, player: Player, block: Block, item_in_hand: ItemStack) -> None:
        """
        Initializes a BlockDamageAbortEvent.

        :param player: The player that stopped damaging the block.
        :param block: The block that was being damaged.
        :param item_in_hand: The item currently in the player's hand.
        """
        ...

    def getPlayer(self) -> Player:
        """
        Gets the player that stopped damaging the block involved in this event.

        :return: The player that stopped damaging the block
        """
        ...

    def getItemInHand(self) -> ItemStack:
        """
        Gets the ItemStack for the item currently in the player's hand.

        :return: The ItemStack for the item currently in the player's hand
        """
        ...

    def getHandlers(self) -> HandlerList:
        """
        Returns the handler list for this event.

        :return: The handler list for this event
        """
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        """
        Gets the handler list for this event.

        :return: The handler list for this event
        """
        ...
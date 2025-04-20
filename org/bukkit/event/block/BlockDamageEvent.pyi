from org.bukkit.block import Block
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.inventory import ItemStack
from typing import Any

class BlockDamageEvent(BlockEvent, Cancellable):
    """
    Called when a block is damaged by a player.
    <p>
    If a Block Damage event is cancelled, the block will not be damaged.
    @see BlockDamageAbortEvent
    """

    handlers: HandlerList = HandlerList()
    player: Player
    instaBreak: bool
    cancel: bool
    itemstack: ItemStack

    def __init__(self, player: Player, block: Block, itemInHand: ItemStack, instaBreak: bool) -> None:
        ...

    """
    Gets the player damaging the block involved in this event.

    @return The player damaging the block involved in this event
    """
    def getPlayer(self) -> Player:
        ...

    """
    Gets if the block is set to instantly break when damaged by the player.

    @return true if the block should instantly break when damaged by the
        player
    """
    def getInstaBreak(self) -> bool:
        ...

    """
    Sets if the block should instantly break when damaged by the player.

    @param bool true if you want the block to instantly break when damaged
        by the player
    """
    def setInstaBreak(self, bool: bool) -> None:
        ...

    """
    Gets the ItemStack for the item currently in the player's hand.

    @return The ItemStack for the item currently in the player's hand
    """
    def getItemInHand(self) -> ItemStack:
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...

    def getHandlers(self) -> HandlerList:
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        ...
from org.bukkit.block import Block
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event.block import BlockExpEvent
from typing import Literal

class BlockBreakEvent(BlockExpEvent, Cancellable):
    """
    Called when a block is broken by a player.
    <p>
    If you wish to have the block drop experience, you must set the experience
    value above 0. By default, experience will be set in the event if:
    <ol>
    <li>The player is not in creative or adventure mode
    <li>The player can loot the block (ie: does not destroy it completely, by
        using the correct tool)
    <li>The player does not have silk touch
    <li>The block drops experience in vanilla Minecraft
    </ol>
    <p>
    Note:
    Plugins wanting to simulate a traditional block drop should set the block
    to air and utilize their own methods for determining what the default drop
    for the block being broken is and what to do about it, if anything.
    <p>
    If a Block Break event is cancelled, the block will not break and
    experience will not drop.
    """

    def __init__(self, theBlock: Block, player: Player) -> None:
        """
        Initializes a BlockBreakEvent.

        :param theBlock: The block being broken.
        :param player: The player breaking the block.
        """
        ...

    def getPlayer(self) -> Player:
        """
        Gets the Player that is breaking the block involved in this event.

        :return: The Player that is breaking the block involved in this event
        """
        ...

    def setDropItems(self, dropItems: bool) -> None:
        """
        Sets whether or not the block will attempt to drop items as it normally
        would.

        If and only if this is false then BlockDropItemEvent will not be
        called after this event.

        :param dropItems: Whether or not the block will attempt to drop items
        """
        ...

    def isDropItems(self) -> bool:
        """
        Gets whether or not the block will attempt to drop items.

        If and only if this is false then BlockDropItemEvent will not be
        called after this event.

        :return: Whether or not the block will attempt to drop items
        """
        ...

    def isCancelled(self) -> bool:
        """
        Checks if the event is cancelled.

        :return: True if the event is cancelled, otherwise false.
        """
        ...

    def setCancelled(self, cancel: bool) -> None:
        """
        Sets the cancellation state of the event.

        :param cancel: True to cancel the event, otherwise false.
        """
        ...
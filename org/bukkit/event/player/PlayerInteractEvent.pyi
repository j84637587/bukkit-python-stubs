from org.bukkit.Material import Material
from org.bukkit.block import Block
from org.bukkit.block import BlockFace
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.block import Action
from org.bukkit.event.block import BlockCanBuildEvent
from org.bukkit.inventory import EquipmentSlot
from org.bukkit.inventory import ItemStack
from org.bukkit.util import Vector
from typing import Optional

class PlayerInteractEvent(PlayerEvent, Cancellable):
    """
    Represents an event that is called when a player interacts with an object or
    air, potentially fired once for each hand. The hand can be determined using
    {@link #getHand()}.
    <p>
    This event will fire as cancelled if the vanilla behavior is to do nothing
    (e.g interacting with air). For the purpose of avoiding doubt, this means
    that the event will only be in the cancelled state if it is fired as a result
    of some prediction made by the server where no subsequent code will run,
    rather than when the subsequent interaction activity (e.g. placing a block in
    an illegal position ({@link BlockCanBuildEvent}) will fail.
    """

    handlers: HandlerList

    def __init__(self, who: Player, action: Action, item: Optional[ItemStack], 
                 clicked_block: Optional[Block], clicked_face: BlockFace, 
                 hand: Optional[EquipmentSlot] = None, 
                 clicked_position: Optional[Vector] = None) -> None:
        ...

    def getAction(self) -> Action:
        """
        Returns the action type

        @return Action returns the type of interaction
        """
        ...

    def isCancelled(self) -> bool:
        """
        Gets the cancellation state of this event. Set to true if you want to
        prevent buckets from placing water and so forth

        @return boolean cancellation state
        @deprecated This event has two possible cancellation states, one for
        {@link #useInteractedBlock()} and one for {@link #useItemInHand()}. It is
        possible a call might have the former false, but the latter true, eg in
        the case of using a firework whilst gliding. Callers should check the
        relevant methods individually.
        """
        ...

    def setCancelled(self, cancel: bool) -> None:
        """
        Sets the cancellation state of this event. A canceled event will not be
        executed in the server, but will still pass to other plugins
        <p>
        Canceling this event will prevent use of food (player won't lose the
        food item), prevent bows/snowballs/eggs from firing, etc. (player won't
        lose the ammo)

        @param cancel true if you wish to cancel this event
        """
        ...

    def getItem(self) -> Optional[ItemStack]:
        """
        Returns the item in hand represented by this event

        @return ItemStack the item used
        """
        ...

    def getMaterial(self) -> Material:
        """
        Convenience method. Returns the material of the item represented by
        this event

        @return Material the material of the item used
        """
        ...

    def hasBlock(self) -> bool:
        """
        Check if this event involved a block

        @return boolean true if it did
        """
        ...

    def hasItem(self) -> bool:
        """
        Check if this event involved an item

        @return boolean true if it did
        """
        ...

    def isBlockInHand(self) -> bool:
        """
        Convenience method to inform the user whether this was a block
        placement event.

        @return boolean true if the item in hand was a block
        """
        ...

    def getClickedBlock(self) -> Optional[Block]:
        """
        Returns the clicked block

        @return Block returns the block clicked with this item.
        """
        ...

    def getBlockFace(self) -> BlockFace:
        """
        Returns the face of the block that was clicked

        @return BlockFace returns the face of the block that was clicked
        """
        ...

    def useInteractedBlock(self) -> Result:
        """
        This controls the action to take with the block (if any) that was
        clicked on. This event gets processed for all blocks, but most don't
        have a default action

        @return the action to take with the interacted block
        """
        ...

    def setUseInteractedBlock(self, use_interacted_block: Result) -> None:
        """
        @param useInteractedBlock the action to take with the interacted block
        """
        ...

    def useItemInHand(self) -> Result:
        """
        This controls the action to take with the item the player is holding.
        This includes both blocks and items (such as flint and steel or
        records). When this is set to default, it will be allowed if no action
        is taken on the interacted block.

        @return the action to take with the item in hand
        """
        ...

    def setUseItemInHand(self, use_item_in_hand: Result) -> None:
        """
        @param useItemInHand the action to take with the item in hand
        """
        ...

    def getHand(self) -> Optional[EquipmentSlot]:
        """
        The hand used to perform this interaction. May be null in the case of
        {@link Action#PHYSICAL}.

        @return the hand used to interact. May be null.
        """
        ...

    def getClickedPosition(self) -> Optional[Vector]:
        """
        Gets the exact position on the block the player interacted with, this will
        be null outside of {@link Action#RIGHT_CLICK_BLOCK}.
        <p>
        All vector components are between 0.0 and 1.0 inclusive.

        @return the clicked position. May be null.
        """
        ...

    def getHandlers(self) -> HandlerList:
        """
        @return HandlerList
        """
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        """
        @return HandlerList
        """
        ...
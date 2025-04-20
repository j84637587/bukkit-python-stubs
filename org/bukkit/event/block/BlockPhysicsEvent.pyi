from org.bukkit.Material import Material
from org.bukkit.block import Block
from org.bukkit.block.data import BlockData
from org.bukkit.event import Cancellable, HandlerList
from typing import Any

class BlockPhysicsEvent(BlockEvent, Cancellable):
    """
    Thrown when a block physics check is called.
    <br>
    This event is a high frequency event, it may be called thousands of times per
    a second on a busy server. Plugins are advised to listen to the event with
    caution and only perform lightweight checks when using it.
    <br>
    In addition to this, cancelling the event is liable to leave the world in an
    inconsistent state. For example if you use the event to leave a block
    floating in mid air when that block has a requirement to be attached to
    something, there is no guarantee that the floating block will persist across
    server restarts or map upgrades.
    <br>
    Plugins should also note that where possible this event may only called for
    the "root" block of physics updates in order to limit event spam. Physics
    updates that cause other blocks to change their state may not result in an
    event for each of those blocks (usually adjacent). If you are concerned about
    monitoring these changes then you should check adjacent blocks yourself.
    """

    handlers: HandlerList

    def __init__(self, block: Block, changed: BlockData, sourceBlock: Block) -> None:
        ...

    def __init__(self, block: Block, changed: BlockData) -> None:
        ...

    """
    Gets the source block that triggered this event.

    Note: This will default to block if not set.

    @return The source block
    """
    def getSourceBlock(self) -> Block:
        ...

    """
    Gets the type of block that changed, causing this event

    @return Changed block's type
    """
    def getChangedType(self) -> Material:
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
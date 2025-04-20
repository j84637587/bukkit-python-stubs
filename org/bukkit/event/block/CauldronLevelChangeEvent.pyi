from typing import Optional, Type
from org.bukkit.block import Block
from org.bukkit.block import BlockState
from org.bukkit.block.data import BlockData
from org.bukkit.block.data import Levelled
from org.bukkit.entity import Entity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.block import BlockEvent
from org.jetbrains.annotations import NotNull, Nullable

class CauldronLevelChangeEvent(BlockEvent, Cancellable):
    handlers: HandlerList

    def __init__(self: "CauldronLevelChangeEvent", block: Block, entity: Optional[Entity], reason: "ChangeReason", newBlock: BlockState) -> None:
        """
        Initialize the CauldronLevelChangeEvent.

        :param block: The block that is changing.
        :param entity: The entity that caused the change, may be None.
        :param reason: The reason for the change.
        :param newBlock: The new state of the block.
        """
        ...

        def getEntity(self: "CauldronLevelChangeEvent") -> Optional[Entity]:
        """
        Get entity which did this. May be null.

        :return: acting entity
        """
        ...

        def getReason(self: "CauldronLevelChangeEvent") -> "ChangeReason":
        """
        Gets the reason for the level change.

        :return: The reason for the change.
        """
        ...

        def getNewState(self: "CauldronLevelChangeEvent") -> BlockState:
        """
        Gets the new state of the cauldron.

        :return: The block state of the block that will be changed.
        """
        ...

    @Deprecated(since="1.17")
    def getOldLevel(self: "CauldronLevelChangeEvent") -> int:
        """
        Gets the old level of the cauldron.

        :return: old level
        """
        ...

    @Deprecated(since="1.17")
    def getNewLevel(self: "CauldronLevelChangeEvent") -> int:
        """
        Gets the new level of the cauldron.

        :return: new level
        """
        ...

    @Deprecated(since="1.17")
    def setNewLevel(self: "CauldronLevelChangeEvent", newLevel: int) -> None:
        """
        Sets the new level of the cauldron.

        :param newLevel: new level
        """
        ...

    def isCancelled(self: "CauldronLevelChangeEvent") -> bool:
        """
        Check if the event is cancelled.

        :return: True if cancelled, False otherwise.
        """
        ...

    def setCancelled(self: "CauldronLevelChangeEvent", cancelled: bool) -> None:
        """
        Set the event as cancelled or not.

        :param cancelled: True to cancel the event, False otherwise.
        """
        ...

        def getHandlers(self: "CauldronLevelChangeEvent") -> HandlerList:
        """
        Get the handlers for this event.

        :return: The handler list.
        """
        ...

        @staticmethod
    def getHandlerList() -> HandlerList:
        """
        Get the static handler list for this event.

        :return: The handler list.
        """
        ...

class ChangeReason:
    """
    Enum representing the reasons for a cauldron level change.
    """
    BUCKET_FILL: Type["ChangeReason"]
    BUCKET_EMPTY: Type["ChangeReason"]
    BOTTLE_FILL: Type["ChangeReason"]
    BOTTLE_EMPTY: Type["ChangeReason"]
    BANNER_WASH: Type["ChangeReason"]
    ARMOR_WASH: Type["ChangeReason"]
    SHULKER_WASH: Type["ChangeReason"]
    EXTINGUISH: Type["ChangeReason"]
    EVAPORATE: Type["ChangeReason"]
    NATURAL_FILL: Type["ChangeReason"]
    UNKNOWN: Type["ChangeReason"]
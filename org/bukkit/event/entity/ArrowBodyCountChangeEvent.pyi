from typing import Any
from org.bukkit.entity import LivingEntity
from org.bukkit.event import Cancellable, HandlerList
from org.jetbrains.annotations import NotNull

class ArrowBodyCountChangeEvent(EntityEvent, Cancellable):
    """
    Called when an arrow enters or exists an entity's body.
    """

    handlers: HandlerList = HandlerList()
    cancelled: bool
    isReset: bool
    oldAmount: int
    newAmount: int

    def __init__(self, entity: LivingEntity, oldAmount: int, newAmount: int, isReset: bool) -> None:
        """
        Initializes the ArrowBodyCountChangeEvent.

        :param entity: The LivingEntity involved in the event.
        :param oldAmount: The old amount of arrows in the entity's body.
        :param newAmount: The new amount of arrows in the entity's body.
        :param isReset: Whether the event was called because the entity was reset.
        """
        ...

    def isReset(self) -> bool:
        """
        Whether the event was called because the entity was reset.

        :return: was reset
        """
        ...

    def getOldAmount(self) -> int:
        """
        Gets the old amount of arrows in the entity's body.

        :return: amount of arrows
        """
        ...

    def getNewAmount(self) -> int:
        """
        Get the new amount of arrows in the entity's body.

        :return: amount of arrows
        """
        ...

    def setNewAmount(self, newAmount: int) -> None:
        """
        Sets the final amount of arrows in the entity's body.

        :param newAmount: amount of arrows
        """
        ...

        def getEntity(self) -> LivingEntity:
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
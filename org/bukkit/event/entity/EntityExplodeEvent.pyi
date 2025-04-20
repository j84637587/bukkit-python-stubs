from typing import List
from org.bukkit import ExplosionResult
from org.bukkit.Location import Location
from org.bukkit.block import Block
from org.bukkit.entity import Entity
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import EntityEvent
from org.jetbrains.annotations import NotNull

class EntityExplodeEvent(EntityEvent, Cancellable):
    """
    Called when an entity explodes
    """

    handlers: HandlerList

    def __init__(self, what: Entity, location: Location, blocks: List[Block], yield: float, result: ExplosionResult) -> None:
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...

        def getExplosionResult(self) -> ExplosionResult:
        """
        Returns the result of the explosion if it is not cancelled.

        @return: the result of the explosion
        """
        ...

        def blockList(self) -> List[Block]:
        """
        Returns the list of blocks that would have been removed or were removed
        from the explosion event.

        @return: All blown-up blocks
        """
        ...

        def getLocation(self) -> Location:
        """
        Returns the location where the explosion happened.
        <p>
        It is not possible to get this value from the Entity as the Entity no
        longer exists in the world.

        @return: The location of the explosion
        """
        ...

    def getYield(self) -> float:
        """
        Returns the percentage of blocks to drop from this explosion

        @return: The yield.
        """
        ...

    def setYield(self, yield: float) -> None:
        """
        Sets the percentage of blocks to drop from this explosion

        @param yield: The new yield percentage
        """
        ...

        def getHandlers(self) -> HandlerList:
        ...

        @staticmethod
    def getHandlerList() -> HandlerList:
        ...
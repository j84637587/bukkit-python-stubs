from typing import List
from org.bukkit.entity import Entity, LightningStrike, Pig, PigZombie
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.event.entity import EntityTransformEvent
from org.jetbrains.annotations import NotNull

class PigZapEvent(EntityTransformEvent, Cancellable):
    """
    Stores data for pigs being zapped
    """
    handlers: HandlerList

    def __init__(self, pig: Pig, bolt: LightningStrike, pigzombie: PigZombie) -> None:
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...

        def getEntity(self) -> Pig:
        ...

        def getLightning(self) -> LightningStrike:
        """
        Gets the bolt which is striking the pig.

        @return lightning entity
        """
        ...

        @Deprecated(since="1.13.2")
    def getPigZombie(self) -> PigZombie:
        """
        Gets the zombie pig that will replace the pig, provided the event is
        not cancelled first.

        @return resulting entity
        """
        ...

        def getHandlers(self) -> HandlerList:
        ...

        @staticmethod
    def getHandlerList() -> HandlerList:
        ...
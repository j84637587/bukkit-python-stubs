from org.bukkit.entity import Creeper
from org.bukkit.entity import LightningStrike
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.event.entity import EntityEvent
from typing import Optional

class CreeperPowerEvent(EntityEvent, Cancellable):
    """
    Called when a Creeper is struck by lightning.
    <p>
    If a Creeper Power event is cancelled, the Creeper will not be powered.
    """

    handlers: HandlerList

    def __init__(self, creeper: Creeper, bolt: LightningStrike, cause: 'CreeperPowerEvent.PowerCause') -> None:
        ...

    def __init__(self, creeper: Creeper, cause: 'CreeperPowerEvent.PowerCause') -> None:
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...

    def getEntity(self) -> Creeper:
        ...

    def getLightning(self) -> Optional[LightningStrike]:
        """
        Gets the lightning bolt which is striking the Creeper.

        @return The Entity for the lightning bolt which is striking the Creeper
        """
        ...

    def getCause(self) -> 'CreeperPowerEvent.PowerCause':
        """
        Gets the cause of the creeper being (un)powered.

        @return A PowerCause value detailing the cause of change in power.
        """
        ...

    def getHandlers(self) -> HandlerList:
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        ...

    class PowerCause:
        """
        An enum to specify the cause of the change in power
        """
        LIGHTNING = ...
        SET_ON = ...
        SET_OFF = ...
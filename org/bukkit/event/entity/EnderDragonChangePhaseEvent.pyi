from typing import Optional
from org.bukkit.entity import EnderDragon
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.event.entity import EntityEvent

class EnderDragonChangePhaseEvent(EntityEvent, Cancellable):
    """
    Called when an EnderDragon switches controller phase.
    """

    handlers: HandlerList = HandlerList()
    cancel: bool
    currentPhase: Optional[EnderDragon.Phase]
    newPhase: EnderDragon.Phase

    def __init__(self, enderDragon: EnderDragon, currentPhase: Optional[EnderDragon.Phase], newPhase: EnderDragon.Phase) -> None:
        """
        Initializes the EnderDragonChangePhaseEvent.

        :param enderDragon: The EnderDragon involved in the event.
        :param currentPhase: The current phase of the EnderDragon.
        :param newPhase: The new phase that the EnderDragon will switch to.
        """
        ...

    def getEntity(self) -> EnderDragon:
        """
        Gets the EnderDragon involved in this event.

        :return: The EnderDragon.
        """
        ...

    def getCurrentPhase(self) -> Optional[EnderDragon.Phase]:
        """
        Gets the current phase that the dragon is in. This method will return None
        when a dragon is first spawned and hasn't yet been assigned a phase.

        :return: The current dragon phase.
        """
        ...

    def getNewPhase(self) -> EnderDragon.Phase:
        """
        Gets the new phase that the dragon will switch to.

        :return: The new dragon phase.
        """
        ...

    def setNewPhase(self, newPhase: EnderDragon.Phase) -> None:
        """
        Sets the new phase for the ender dragon.

        :param newPhase: The new dragon phase.
        """
        ...

    def isCancelled(self) -> bool:
        """
        Checks if the event is cancelled.

        :return: True if the event is cancelled, False otherwise.
        """
        ...

    def setCancelled(self, cancel: bool) -> None:
        """
        Sets the cancellation state of the event.

        :param cancel: True to cancel the event, False otherwise.
        """
        ...

    def getHandlers(self) -> HandlerList:
        """
        Gets the handlers for this event.

        :return: The HandlerList for this event.
        """
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        """
        Gets the static HandlerList for this event.

        :return: The static HandlerList for this event.
        """
        ...
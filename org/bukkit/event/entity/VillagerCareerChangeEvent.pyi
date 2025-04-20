from org.bukkit.entity import Villager
from org.bukkit.entity.Villager import Profession
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from typing import Literal, Type

class VillagerCareerChangeEvent(EntityEvent, Cancellable):
    """
    Represents an event where a villager's career is changing.
    """

    handlers: HandlerList = HandlerList()
    cancelled: bool
    profession: Profession
    reason: 'ChangeReason'

    def __init__(self, what: Villager, profession: Profession, reason: 'ChangeReason') -> None:
        """
        Initializes the VillagerCareerChangeEvent.

        :param what: The villager whose career is changing.
        :param profession: The new profession of the villager.
        :param reason: The reason for the career change.
        """
        ...

    def getEntity(self) -> Villager:
        """
        Gets the villager associated with this event.

        :return: The villager involved in this event.
        """
        ...

    def getProfession(self) -> Profession:
        """
        Gets the future profession of the villager.

        :return: The profession the villager will change to.
        """
        ...

    def setProfession(self, profession: Profession) -> None:
        """
        Sets the profession the villager will become from this event.

        :param profession: New profession.
        """
        ...

    def getReason(self) -> 'ChangeReason':
        """
        Gets the reason for why the villager's career is changing.

        :return: Reason for villager's profession changing.
        """
        ...

    def isCancelled(self) -> bool:
        """
        Checks if the event is cancelled.

        :return: True if the event is cancelled, otherwise False.
        """
        ...

    def setCancelled(self, cancel: bool) -> None:
        """
        Sets the cancellation state of the event.

        :param cancel: True to cancel the event, otherwise False.
        """
        ...

    def getHandlers(self) -> HandlerList:
        """
        Gets the handlers for this event.

        :return: The handler list for this event.
        """
        ...

    @classmethod
    def getHandlerList(cls) -> HandlerList:
        """
        Gets the static handler list for this event.

        :return: The static handler list.
        """
        ...

    class ChangeReason:
        """
        Reasons for the villager's profession changing.
        """
        LOSING_JOB: Literal['LOSING_JOB'] = 'LOSING_JOB'
        EMPLOYED: Literal['EMPLOYED'] = 'EMPLOYED'
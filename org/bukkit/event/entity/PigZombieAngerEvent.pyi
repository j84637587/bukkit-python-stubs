from typing import Optional
from org.bukkit.entity import Entity, PigZombie
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.event.entity import EntityEvent


class PigZombieAngerEvent(EntityEvent, Cancellable):
    """
    Called when a Pig Zombie is angered by another entity.
    <p>
    If the event is cancelled, the pig zombie will not be angered.
    """

    handlers: HandlerList

    def __init__(self, pig_zombie: PigZombie, target: Optional[Entity], new_anger: int) -> None:
        """
        Initializes the PigZombieAngerEvent.

        :param pig_zombie: The PigZombie that is angered.
        :param target: The entity that triggered the anger update, or None.
        :param new_anger: The new anger level.
        """
        ...

    def get_target(self) -> Optional[Entity]:
        """
        Gets the entity (if any) which triggered this anger update.

        :return: triggering entity, or None
        """
        ...

    def get_new_anger(self) -> int:
        """
        Gets the new anger resulting from this event.

        :return: new anger
        """
        ...

    def set_new_anger(self, new_anger: int) -> None:
        """
        Sets the new anger resulting from this event.

        :param new_anger: the new anger
        """
        ...

    def get_entity(self) -> PigZombie:
        ...
    
    def is_cancelled(self) -> bool:
        ...
    
    def set_cancelled(self, cancel: bool) -> None:
        ...
    
    def get_handlers(self) -> HandlerList:
        ...
    
    @staticmethod
    def get_handler_list() -> HandlerList:
        ...
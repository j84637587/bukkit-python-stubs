from typing import Optional
from org.bukkit.entity import LivingEntity
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.inventory import ItemStack

class EntityBreedEvent(EntityEvent, Cancellable):
    """
    Called when one Entity breeds with another Entity.
    """

    handlers: HandlerList = HandlerList()

    def __init__(self, child: LivingEntity, mother: LivingEntity, father: LivingEntity, 
                 breeder: Optional[LivingEntity], bred_with: Optional[ItemStack], 
                 experience: int) -> None:
        """
        Initializes the EntityBreedEvent.

        :param child: The child entity.
        :param mother: The mother entity.
        :param father: The father entity.
        :param breeder: The entity responsible for breeding, can be None.
        :param bred_with: The ItemStack used to initiate breeding, can be None.
        :param experience: The experience amount granted by breeding.
        """
        ...

    def getEntity(self) -> LivingEntity:
        """
        :return: The entity involved in the event.
        """
        ...

    def getMother(self) -> LivingEntity:
        """
        Gets the parent creating this entity.

        :return: The "birth" parent.
        """
        ...

    def getFather(self) -> LivingEntity:
        """
        Gets the other parent of the newly born entity.

        :return: The other parent.
        """
        ...

    def getBreeder(self) -> Optional[LivingEntity]:
        """
        Gets the Entity responsible for breeding. Breeder is None for spontaneous conception.

        :return: The Entity who initiated breeding.
        """
        ...

    def getBredWith(self) -> Optional[ItemStack]:
        """
        The ItemStack that was used to initiate breeding, if present.

        :return: ItemStack used to initiate breeding.
        """
        ...

    def getExperience(self) -> int:
        """
        Get the amount of experience granted by breeding.

        :return: experience amount.
        """
        ...

    def setExperience(self, experience: int) -> None:
        """
        Set the amount of experience granted by breeding.

        :param experience: experience amount.
        """
        ...

    def isCancelled(self) -> bool:
        """
        :return: True if the event is cancelled, False otherwise.
        """
        ...

    def setCancelled(self, cancel: bool) -> None:
        """
        Set whether the event is cancelled.

        :param cancel: True to cancel the event, False otherwise.
        """
        ...

    def getHandlers(self) -> HandlerList:
        """
        :return: The HandlerList for this event.
        """
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        """
        :return: The static HandlerList for this event.
        """
        ...
from typing import List
from org.bukkit.damage import DamageSource
from org.bukkit.entity import LivingEntity
from org.bukkit.event import HandlerList
from org.bukkit.inventory import ItemStack
from org.jetbrains.annotations import NotNull

class EntityDeathEvent(EntityEvent):
    """
    Thrown whenever a LivingEntity dies
    """

    handlers: HandlerList = HandlerList()
    damageSource: DamageSource
    drops: List[ItemStack]
    dropExp: int

    def __init__(self, entity: LivingEntity, damageSource: DamageSource, drops: List[ItemStack]) -> None:
        """
        Initializes the EntityDeathEvent with the given parameters.
        """
        ...

    def __init__(self, what: LivingEntity, damageSource: DamageSource, drops: List[ItemStack], droppedExp: int) -> None:
        """
        Initializes the EntityDeathEvent with the given parameters.
        """
        ...

        def getEntity(self) -> LivingEntity:
        """
        Returns the LivingEntity involved in this event.
        """
        ...

        def getDamageSource(self) -> DamageSource:
        """
        Gets the source of damage which caused the death.

        @return: a DamageSource detailing the source of the damage for the death.
        """
        ...

    def getDroppedExp(self) -> int:
        """
        Gets how much EXP should be dropped from this death.
        <p>
        This does not indicate how much EXP should be taken from the entity in
        question, merely how much should be created after its death.

        @return: Amount of EXP to drop.
        """
        ...

    def setDroppedExp(self, exp: int) -> None:
        """
        Sets how much EXP should be dropped from this death.
        <p>
        This does not indicate how much EXP should be taken from the entity in
        question, merely how much should be created after its death.

        @param exp: Amount of EXP to drop.
        """
        ...

        def getDrops(self) -> List[ItemStack]:
        """
        Gets all the items which will drop when the entity dies.

        @return: Items to drop when the entity dies.
        """
        ...

        def getHandlers(self) -> HandlerList:
        """
        Returns the HandlerList for this event.
        """
        ...

        @staticmethod
    def getHandlerList() -> HandlerList:
        """
        Returns the static HandlerList for this event.
        """
        ...
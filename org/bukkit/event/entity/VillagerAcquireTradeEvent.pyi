from org.bukkit.entity import AbstractVillager
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.inventory import MerchantRecipe
from typing import Any

class VillagerAcquireTradeEvent(EntityEvent, Cancellable):
    """
    Called whenever a villager acquires a new trade.
    """

    handlers: HandlerList = HandlerList()
    cancelled: bool
    recipe: MerchantRecipe

    def __init__(self, what: AbstractVillager, recipe: MerchantRecipe) -> None:
        ...

    def getRecipe(self) -> MerchantRecipe:
        """
        Get the recipe to be acquired.

        Returns:
            MerchantRecipe: the new recipe
        """
        ...

    def setRecipe(self, recipe: MerchantRecipe) -> None:
        """
        Set the recipe to be acquired.

        Args:
            recipe (MerchantRecipe): the new recipe
        """
        ...

    def isCancelled(self) -> bool:
        ...
    
    def setCancelled(self, cancel: bool) -> None:
        ...

    def getEntity(self) -> AbstractVillager:
        ...
    
    def getHandlers(self) -> HandlerList:
        ...
    
    @staticmethod
    def getHandlerList() -> HandlerList:
        ...
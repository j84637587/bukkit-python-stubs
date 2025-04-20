from org.bukkit.entity import AbstractVillager
from org.bukkit.entity import Villager
from org.bukkit.event import Cancellable
from org.bukkit.event import HandlerList
from org.bukkit.inventory import MerchantRecipe
from typing import Optional

class VillagerReplenishTradeEvent(EntityEvent, Cancellable):
    """
    Called when a `Villager` is about to restock one of its trades.
    <p>
    If this event passes, the villager will reset the
    `MerchantRecipe.getUses() uses` of the affected `getRecipe() MerchantRecipe` to <code>0</code>.
    """

    handlers: HandlerList = HandlerList()
    cancelled: bool
    recipe: MerchantRecipe

    def __init__(self, what: AbstractVillager, recipe: MerchantRecipe) -> None:
        """
        Initialize the VillagerReplenishTradeEvent.

        :param what: The villager that is restocking.
        :param recipe: The recipe to replenish.
        """
        ...

    def getRecipe(self) -> MerchantRecipe:
        """
        Get the recipe to replenish.

        :return: The replenished recipe.
        """
        ...

    def setRecipe(self, recipe: MerchantRecipe) -> None:
        """
        Set the recipe to replenish.

        :param recipe: The replenished recipe.
        """
        ...

    @Deprecated(since="1.18.1")
    def getBonus(self) -> int:
        """
        Get the bonus uses added.

        :return: The extra uses added.
        """
        ...

    @Deprecated(since="1.18.1")
    def setBonus(self, bonus: int) -> None:
        """
        Set the bonus uses added.

        :param bonus: The extra uses added.
        """
        ...

    def isCancelled(self) -> bool:
        """
        Check if the event is cancelled.

        :return: True if the event is cancelled, False otherwise.
        """
        ...

    def setCancelled(self, cancel: bool) -> None:
        """
        Set the event as cancelled.

        :param cancel: True to cancel the event, False otherwise.
        """
        ...

    def getEntity(self) -> AbstractVillager:
        """
        Get the villager entity involved in the event.

        :return: The villager entity.
        """
        ...

    def getHandlers(self) -> HandlerList:
        """
        Get the handler list for this event.

        :return: The handler list.
        """
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        """
        Get the static handler list for this event.

        :return: The static handler list.
        """
        ...
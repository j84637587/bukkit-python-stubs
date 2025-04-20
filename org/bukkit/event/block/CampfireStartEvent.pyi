from org.bukkit.block import Block
from org.bukkit.event import HandlerList
from org.bukkit.inventory import CampfireRecipe, ItemStack
from typing import Any

class CampfireStartEvent(InventoryBlockStartEvent):
    """
    Called when a Campfire starts to cook.
    """

    handlers: HandlerList = HandlerList()
    cookingTime: int
    campfireRecipe: CampfireRecipe

    def __init__(self, furnace: Block, source: ItemStack, recipe: CampfireRecipe) -> None:
        """
        Initializes the CampfireStartEvent.

        :param furnace: The block associated with the campfire.
        :param source: The item stack being cooked.
        :param recipe: The campfire recipe.
        """
        ...

    def getRecipe(self) -> CampfireRecipe:
        """
        Gets the CampfireRecipe associated with this event.

        :return: the CampfireRecipe being cooked
        """
        ...

    def getTotalCookTime(self) -> int:
        """
        Gets the total cook time associated with this event.

        :return: the total cook time
        """
        ...

    def setTotalCookTime(self, cookTime: int) -> None:
        """
        Sets the total cook time for this event.

        :param cookTime: the new total cook time
        """
        ...

    def getHandlers(self) -> HandlerList:
        """
        Gets the handlers for this event.

        :return: the handler list
        """
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        """
        Gets the static handler list for this event.

        :return: the handler list
        """
        ...
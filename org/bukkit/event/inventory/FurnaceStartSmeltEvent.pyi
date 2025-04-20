from org.bukkit.block import Block
from org.bukkit.event import HandlerList
from org.bukkit.event.block import InventoryBlockStartEvent
from org.bukkit.inventory import CookingRecipe
from org.bukkit.inventory import ItemStack
from typing import TypeVar

T = TypeVar('T', bound=CookingRecipe)

class FurnaceStartSmeltEvent(InventoryBlockStartEvent):
    """
    Called when a Furnace starts smelting.
    """

    handlers: HandlerList = HandlerList()
    recipe: T
    totalCookTime: int

    def __init__(self, furnace: Block, source: ItemStack, recipe: T) -> None:
        super().__init__(furnace, source)
        self.recipe = recipe
        self.totalCookTime = recipe.getCookingTime()

    """
    Gets the FurnaceRecipe associated with this event

    @return: the FurnaceRecipe being cooked
    """
    def getRecipe(self) -> T:
        ...

    """
    Gets the total cook time associated with this event

    @return: the total cook time
    """
    def getTotalCookTime(self) -> int:
        ...

    """
    Sets the total cook time for this event

    @param cookTime: the new total cook time
    """
    def setTotalCookTime(self, cookTime: int) -> None:
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        ...

    def getHandlers(self) -> HandlerList:
        ...
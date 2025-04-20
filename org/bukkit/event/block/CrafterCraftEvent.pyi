from typing import List
from org.bukkit.block import Block
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.inventory import CraftingRecipe, ItemStack

class CrafterCraftEvent(BlockEvent, Cancellable):
    """
    Event called when a Crafter is about to craft an item.
    """

    handlers: HandlerList = HandlerList()
    recipe: CraftingRecipe
    result: ItemStack
    remainingItems: List[ItemStack]
    cancelled: bool

    def __init__(self, theBlock: Block, recipe: CraftingRecipe, result: ItemStack, remainingItems: List[ItemStack]) -> None:
        ...

    @classmethod
    def getHandlerList(cls) -> HandlerList:
        ...

    @Deprecated(since="1.21.4")
    def __init__(self, theBlock: Block, recipe: CraftingRecipe, result: ItemStack) -> None:
        ...

    def getResult(self) -> ItemStack:
        ...

    def setResult(self, result: ItemStack) -> None:
        ...

    def getRemainingItems(self) -> List[ItemStack]:
        ...

    def getRecipe(self) -> CraftingRecipe:
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...

    def getHandlers(self) -> HandlerList:
        ...
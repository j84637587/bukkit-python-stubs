from org.bukkit.event.inventory import InventoryEvent
from org.bukkit.event import HandlerList
from org.bukkit.inventory import CraftingInventory, InventoryView, Recipe
from typing import Optional

class PrepareItemCraftEvent(InventoryEvent):
    handlers: HandlerList = HandlerList()

    def __init__(self, what: CraftingInventory, view: InventoryView, isRepair: bool) -> None:
        """
        Initialize the PrepareItemCraftEvent.

        :param what: The crafting inventory.
        :param view: The inventory view.
        :param isRepair: True if this event is triggered by a tool repair.
        """
        ...

    def getRecipe(self) -> Optional[Recipe]:
        """
        Get the recipe that has been formed. If this event was triggered by a
        tool repair, this will be a temporary shapeless recipe representing the
        repair.

        :return: The recipe being crafted.
        """
        ...

    def getInventory(self) -> CraftingInventory:
        """
        Get the crafting inventory on which the recipe was formed.

        :return: The crafting inventory.
        """
        ...

    def isRepair(self) -> bool:
        """
        Check if this event was triggered by a tool repair operation rather
        than a crafting recipe.

        :return: True if this is a repair.
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
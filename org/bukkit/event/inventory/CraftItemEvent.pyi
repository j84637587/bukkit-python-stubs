from org.bukkit.event.inventory import InventoryClickEvent
from org.bukkit.event.inventory import InventoryAction
from org.bukkit.event.inventory import ClickType
from org.bukkit.inventory import CraftingInventory
from org.bukkit.inventory import InventoryView
from org.bukkit.inventory import Recipe
from org.jetbrains.annotations import NotNull

class CraftItemEvent(InventoryClickEvent):
    """
    Called when the recipe of an Item is completed inside a crafting matrix.
    """

    def __init__(self, recipe: NotNull[Recipe], what: NotNull[InventoryView], type: NotNull[SlotType], slot: int, click: NotNull[ClickType], action: NotNull[InventoryAction]) -> None:
        ...

    def __init__(self, recipe: NotNull[Recipe], what: NotNull[InventoryView], type: NotNull[SlotType], slot: int, click: NotNull[ClickType], action: NotNull[InventoryAction], key: int) -> None:
        ...

        def getRecipe(self) -> Recipe:
        ...

        def getInventory(self) -> CraftingInventory:
        ...
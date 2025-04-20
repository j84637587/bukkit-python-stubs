from org.bukkit.block import Block
from org.bukkit.event import HandlerList
from org.bukkit.event.inventory import FurnaceStartSmeltEvent
from org.bukkit.inventory import ItemStack
from typing import Any
from org.jetbrains.annotations import NotNull

"""
Used when:
<ul>
<li>A Furnace starts smelting {@link FurnaceStartSmeltEvent}</li>
<li>A Brewing-Stand starts brewing {@link BrewingStartEvent}</li>
<li>A Campfire starts cooking {@link CampfireStartEvent}</li>
</ul>
"""
class InventoryBlockStartEvent(BlockEvent):
    handlers: HandlerList = HandlerList()
    source: ItemStack

    def __init__(self, block: Block, source: ItemStack) -> None:
        super().__init__(block)
        self.source = source

    """
    Gets the source ItemStack for this event.

    @return: the source ItemStack
    """
        def getSource(self) -> ItemStack:
        ...

        def getHandlers(self) -> HandlerList:
        ...

        @staticmethod
    def getHandlerList() -> HandlerList:
        ...
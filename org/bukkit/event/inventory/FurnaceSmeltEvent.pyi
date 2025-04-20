from org.bukkit.block import Block
from org.bukkit.event.block import BlockCookEvent
from org.bukkit.inventory import ItemStack
from typing import Any

class FurnaceSmeltEvent(BlockCookEvent):
    """
    Called when an ItemStack is successfully smelted in a furnace.
    """

    def __init__(self, furnace: Block, source: ItemStack, result: ItemStack) -> None:
        ...
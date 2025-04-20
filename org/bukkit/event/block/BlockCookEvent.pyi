from org.bukkit.block import Block
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.inventory import ItemStack
from typing import Any

class BlockCookEvent(BlockEvent, Cancellable):
    """
    Called when an ItemStack is successfully cooked in a block.
    """

    handlers: HandlerList

    def __init__(self, block: Block, source: ItemStack, result: ItemStack) -> None:
        ...

    """
    Gets the smelted ItemStack for this event

    @return smelting source ItemStack
    """
    def get_source(self) -> ItemStack:
        ...

    """
    Gets the resultant ItemStack for this event

    @return smelting result ItemStack
    """
    def get_result(self) -> ItemStack:
        ...

    """
    Sets the resultant ItemStack for this event

    @param result new result ItemStack
    """
    def set_result(self, result: ItemStack) -> None:
        ...

    def is_cancelled(self) -> bool:
        ...

    def set_cancelled(self, cancel: bool) -> None:
        ...

    def get_handlers(self) -> HandlerList:
        ...

    @staticmethod
    def get_handler_list() -> HandlerList:
        ...
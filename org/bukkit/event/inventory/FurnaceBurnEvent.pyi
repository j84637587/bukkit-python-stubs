from org.bukkit.block import Block
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.event.block import BlockEvent
from org.bukkit.inventory import ItemStack
from typing import Any

class FurnaceBurnEvent(BlockEvent, Cancellable):
    """
    Called when an ItemStack is successfully burned as fuel in a furnace.
    """

    handlers: HandlerList

    def __init__(self, furnace: Block, fuel: ItemStack, burn_time: int) -> None:
        ...

    """
    Gets the fuel ItemStack for this event

    @return the fuel ItemStack
    """
    def get_fuel(self) -> ItemStack:
        ...

    """
    Gets the burn time for this fuel

    @return the burn time for this fuel
    """
    def get_burn_time(self) -> int:
        ...

    """
    Sets the burn time for this fuel

    @param burn_time the burn time for this fuel
    """
    def set_burn_time(self, burn_time: int) -> None:
        ...

    """
    Gets whether the furnace's fuel is burning or not.

    @return whether the furnace's fuel is burning or not.
    """
    def is_burning(self) -> bool:
        ...

    """
    Sets whether the furnace's fuel is burning or not.

    @param burning true if the furnace's fuel is burning
    """
    def set_burning(self, burning: bool) -> None:
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
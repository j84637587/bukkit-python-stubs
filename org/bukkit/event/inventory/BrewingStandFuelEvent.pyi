from org.bukkit.block import Block
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.event.block import BlockEvent
from org.bukkit.inventory import ItemStack
from typing import Any

class BrewingStandFuelEvent(BlockEvent, Cancellable):
    """
    Called when an ItemStack is about to increase the fuel level of a brewing
    stand.
    """

    handlers: HandlerList

    def __init__(self, brewing_stand: Block, fuel: ItemStack, fuel_power: int) -> None:
        ...

    """
    Gets the ItemStack of the fuel before the amount was subtracted.

    @return: the fuel ItemStack
    """
    def get_fuel(self) -> ItemStack:
        ...

    """
    Gets the fuel power for this fuel. Each unit of power can fuel one
    brewing operation.

    @return: the fuel power for this fuel
    """
    def get_fuel_power(self) -> int:
        ...

    """
    Sets the fuel power for this fuel. Each unit of power can fuel one
    brewing operation.

    @param fuel_power: the fuel power for this fuel
    """
    def set_fuel_power(self, fuel_power: int) -> None:
        ...

    """
    Gets whether the brewing stand's fuel will be reduced / consumed or not.

    @return: whether the fuel will be reduced or not
    """
    def is_consuming(self) -> bool:
        ...

    """
    Sets whether the brewing stand's fuel will be reduced / consumed or not.

    @param consuming: whether the fuel will be reduced or not
    """
    def set_consuming(self, consuming: bool) -> None:
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
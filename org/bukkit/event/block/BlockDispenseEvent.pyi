from org.bukkit.block import Block
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.inventory import ItemStack
from org.bukkit.util import Vector
from typing import Any

class BlockDispenseEvent(BlockEvent, Cancellable):
    """
    Called when an item is dispensed from a block.
    <p>
    If a Block Dispense event is cancelled, the block will not dispense the
    item.
    """

    handlers: HandlerList = HandlerList()
    cancelled: bool
    item: ItemStack
    velocity: Vector

    def __init__(self, block: Block, dispensed: ItemStack, velocity: Vector) -> None:
        """
        Initializes a BlockDispenseEvent.

        :param block: The block from which the item is dispensed
        :param dispensed: The item being dispensed
        :param velocity: The velocity of the dispensed item
        """
        ...

    def get_item(self) -> ItemStack:
        """
        Gets the item that is being dispensed. Modifying the returned item will
        have no effect, you must use {@link
        #setItem(org.bukkit.inventory.ItemStack)} instead.

        :return: An ItemStack for the item being dispensed
        """
        ...

    def set_item(self, item: ItemStack) -> None:
        """
        Sets the item being dispensed.

        :param item: the item being dispensed
        """
        ...

    def get_velocity(self) -> Vector:
        """
        Gets the velocity in meters per tick.
        <p>
        Note: Modifying the returned Vector will not change the velocity, you
        must use {@link #setVelocity(org.bukkit.util.Vector)} instead.

        :return: A Vector for the dispensed item's velocity
        """
        ...

    def set_velocity(self, vel: Vector) -> None:
        """
        Sets the velocity of the item being dispensed in meters per tick.

        :param vel: the velocity of the item being dispensed
        """
        ...

    def is_cancelled(self) -> bool:
        """
        Checks if the event is cancelled.

        :return: True if the event is cancelled, otherwise False
        """
        ...

    def set_cancelled(self, cancel: bool) -> None:
        """
        Sets the cancellation state of the event.

        :param cancel: True to cancel the event, otherwise False
        """
        ...

    def get_handlers(self) -> HandlerList:
        """
        Gets the handlers for this event.

        :return: The HandlerList for this event
        """
        ...

    @staticmethod
    def get_handler_list() -> HandlerList:
        """
        Gets the static handler list for this event.

        :return: The static HandlerList for this event
        """
        ...
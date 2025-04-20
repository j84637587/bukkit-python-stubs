from org.bukkit.block import Block
from org.bukkit.entity import Entity
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.inventory import ItemStack
from typing import Any

class BlockShearEntityEvent(BlockEvent, Cancellable):
    """
    Event fired when a dispenser shears a nearby sheep.
    """

    handlers: HandlerList = HandlerList()

    def __init__(self, dispenser: Block, sheared: Entity, tool: ItemStack) -> None:
        ...

    def get_entity(self) -> Entity:
        """
        Gets the entity that was sheared.

        Returns:
            Entity: the entity that was sheared.
        """
        ...

    def get_tool(self) -> ItemStack:
        """
        Gets the item used to shear this sheep.

        Returns:
            ItemStack: the item used to shear this sheep.
        """
        ...

    def is_cancelled(self) -> bool:
        ...

    def set_cancelled(self, cancelled: bool) -> None:
        ...

    def get_handlers(self) -> HandlerList:
        ...

    @staticmethod
    def get_handler_list() -> HandlerList:
        ...
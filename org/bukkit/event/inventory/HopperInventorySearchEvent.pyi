from org.bukkit.block import Block
from org.bukkit.event import HandlerList
from org.bukkit.event.block import BlockEvent
from org.bukkit.inventory import Inventory
from typing import Optional

class HopperInventorySearchEvent(BlockEvent):
    """
    Event that gets called each time a Hopper attempts to find its
    source/attached containers.
    """

    handlers: HandlerList

    class ContainerType:
        """
        The source container the hopper is looking for.

        This is the Inventory above the Hopper where it extracts items from.
        """
        SOURCE = ...
        """
        The container the hopper is attached to.

        This is the Inventory the Hopper pushes items into.
        """
        DESTINATION = ...

    def __init__(self, inventory: Inventory, container_type: 'HopperInventorySearchEvent.ContainerType', hopper: Block, search_block: Block) -> None:
        ...

    def set_inventory(self, inventory: Optional[Inventory]) -> None:
        """
        Set the Inventory that the Hopper will use for its
        source/attached Container.

        :param inventory: the inventory to use
        """
        ...

    def get_inventory(self) -> Optional[Inventory]:
        """
        Gets the Inventory that the Hopper will use for its
        source/attached Container.

        :return: the inventory which will be used
        """
        ...

    def get_container_type(self) -> 'HopperInventorySearchEvent.ContainerType':
        """
        Gets the Container type the Hopper is searching for.

        :return: the container type being searched for
        """
        ...

    def get_search_block(self) -> Block:
        """
        Gets the Block that is being searched for an inventory.

        :return: block being searched for an inventory
        """
        ...

    def get_handlers(self) -> HandlerList:
        ...
    
    @staticmethod
    def get_handler_list() -> HandlerList:
        ...
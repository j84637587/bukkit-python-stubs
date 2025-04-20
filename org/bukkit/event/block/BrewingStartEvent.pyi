from org.bukkit.block import Block
from org.bukkit.event import HandlerList
from org.bukkit.inventory import ItemStack
from typing import Any

class BrewingStartEvent(InventoryBlockStartEvent):
    """
    Called when a brewing stand starts to brew.
    """

    handlers: HandlerList = HandlerList()
    brewingTime: int

    def __init__(self, furnace: Block, source: ItemStack, brewingTime: int) -> None:
        """
        Initializes the BrewingStartEvent.

        :param furnace: The block associated with the brewing stand.
        :param source: The item stack being brewed.
        :param brewingTime: The initial brewing time.
        """
        ...

    def get_total_brew_time(self) -> int:
        """
        Gets the total brew time associated with this event.

        :return: the total brew time
        """
        ...

    def set_total_brew_time(self, brewTime: int) -> None:
        """
        Sets the total brew time for this event.

        :param brewTime: the new total brew time
        """
        ...

    def get_handlers(self) -> HandlerList:
        """
        Returns the handler list for this event.

        :return: the handler list
        """
        ...

    @staticmethod
    def get_handler_list() -> HandlerList:
        """
        Gets the static handler list for this event.

        :return: the static handler list
        """
        ...
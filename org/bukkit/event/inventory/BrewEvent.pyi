from typing import List
from org.bukkit.block import Block
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.event.block import BlockEvent
from org.bukkit.inventory import BrewerInventory, ItemStack
from org.jetbrains.annotations import NotNull

class BrewEvent(BlockEvent, Cancellable):
    """
    Called when the brewing of the contents inside the Brewing Stand is
    complete.
    """

    handlers: HandlerList

    def __init__(self, brewer: Block, contents: BrewerInventory, results: List[ItemStack], fuelLevel: int) -> None:
        ...

        def getContents(self) -> BrewerInventory:
        """
        Gets the contents of the Brewing Stand.

        <b>Note:</b> The brewer inventory still holds the items found prior to
        the finalization of the brewing process, e.g. the plain water bottles.

        @return the contents
        """
        ...

    def getFuelLevel(self) -> int:
        """
        Gets the remaining fuel level.

        @return the remaining fuel
        """
        ...

        def getResults(self) -> List[ItemStack]:
        """
        Gets the resulting items in the Brewing Stand.

        The returned list, in case of a server-created event instance, is
        mutable. Any changes in the returned list will reflect in the brewing
        result if the event is not cancelled. If the size of the list is reduced,
        remaining items will be set to air.

        @return List of {@link ItemStack} resulting for this operation
        """
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...

        def getHandlers(self) -> HandlerList:
        ...

        @staticmethod
    def getHandlerList() -> HandlerList:
        ...
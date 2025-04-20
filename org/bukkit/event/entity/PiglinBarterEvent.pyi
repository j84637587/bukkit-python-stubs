from typing import List
from org.bukkit.entity import Piglin
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.inventory import ItemStack
from org.bukkit.event.entity import EntityEvent

class PiglinBarterEvent(EntityEvent, Cancellable):
    """
    Stores all data related to the bartering interaction with a piglin.

    This event can be triggered by a piglin picking up an item that's on its
    bartering list.
    """

    handlers: HandlerList = HandlerList()
    cancelled: bool
    outcome: List[ItemStack]
    input: ItemStack

    def __init__(self, what: Piglin, input: ItemStack, outcome: List[ItemStack]) -> None:
        super().__init__(what)
        self.input = input
        self.outcome = outcome

    def getEntity(self) -> Piglin:
        return super().getEntity()

    """
    Gets the input of the barter.

    @return The item that was used to barter with
    """
    def getInput(self) -> ItemStack:
        return self.input.clone()

    """
    Returns a mutable list representing the outcome of the barter.

    @return A mutable list of the item the player will receive
    """
    def getOutcome(self) -> List[ItemStack]:
        return self.outcome

    def isCancelled(self) -> bool:
        return self.cancelled

    def setCancelled(self, cancel: bool) -> None:
        self.cancelled = cancel

    def getHandlers(self) -> HandlerList:
        return self.handlers

    @staticmethod
    def getHandlerList() -> HandlerList:
        return PiglinBarterEvent.handlers
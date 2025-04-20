from typing import List, Optional
from org.bukkit.block import Block
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable, HandlerList
from org.bukkit.inventory import ItemStack
from org.jetbrains.annotations import ApiStatus, NotNull, Nullable

class BlockDispenseLootEvent(BlockEvent, Cancellable):
    """
    Called when a block dispenses loot from its designated LootTable. This is not
    to be confused with events like {@link BlockDispenseEvent} which fires when a
    singular item is dispensed from its inventory container.
    <br><br>
    Example: A player unlocks a trial chamber vault and the vault block dispenses
    its loot.
    """

    handlers: HandlerList

    def __init__(self, player: Optional[Player], the_block: Block, dispensed_loot: List[ItemStack]) -> None:
        ...

    """
    Gets the loot that will be dispensed.

    @return the loot that will be dispensed
    """
        def get_dispensed_loot(self) -> List[ItemStack]:
        ...

    """
    Sets the loot that will be dispensed.

    @param dispensedLoot new loot to dispense
    """
    def set_dispensed_loot(self, dispensed_loot: Optional[List[ItemStack]]) -> None:
        ...

    """
    Gets the player associated with this event.
    <br>
    <b>Warning:</b> Some event instances like a
    {@link org.bukkit.block.TrialSpawner} dispensing its reward loot may not
    have a player associated with them and will return null.

    @return the player who unlocked the vault
    """
        def get_player(self) -> Optional[Player]:
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
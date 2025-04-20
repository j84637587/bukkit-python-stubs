from typing import Protocol
from org.bukkit.entity import EntityDeathEvent
import org.bukkit.block import Block

class SculkCatalyst(Protocol):
    """
    Represents a captured state of a sculk catalyst.
    """

    def bloom(self, block: Block, charges: int) -> None:
        """
        Causes a new sculk bloom, as if an entity just died around this catalyst.
        Typically, charges should be set to the exp reward of a mob
        (EntityDeathEvent.getDroppedExp()), which is usually
        3-5 for animals, and 5-10 for the average mob (up to 50 for
        wither skeletons). Roughly speaking, for each charge, 1 more
        sculk block will be placed.
        If charges > 1000, multiple cursors will be spawned in the
        block.

        :param block: which block to spawn the cursor in
        :param charges: how much charge to spawn.
        """
        ...
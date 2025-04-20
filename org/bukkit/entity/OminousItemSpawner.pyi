from org.bukkit.inventory import ItemStack
from org.jetbrains.annotations import ApiStatus, Nullable
from org.bukkit.entity import Entity
from typing import Optional

"""
Represents an ominous item spawner.
"""

class OminousItemSpawner(Entity):
    """
    Gets the item which will be spawned by this spawner.

    @return: the item
    """

    def get_item(self) -> Optional[ItemStack]: ...

    """
    Sets the item which will be spawned by this spawner.

    @param item: the item
    """
    def set_item(self, item: Optional[ItemStack]) -> None: ...

    """
    Gets the ticks after which this item will be spawned.

    @return: total spawn ticks
    """
    def get_spawn_item_after_ticks(self) -> int: ...

    """
    Sets the ticks after which this item will be spawned.

    @param ticks: total spawn ticks
    """
    def set_spawn_item_after_ticks(self, ticks: int) -> None: ...

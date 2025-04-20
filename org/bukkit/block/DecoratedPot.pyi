from typing import List, Dict
from org.bukkit import Material
from .tag import Tag
import org.bukkit.block_inventory_holder import BlockInventoryHolder
from .decorated_pot_inventory import DecoratedPotInventory
from .tile_state import TileState
from .side import Side
from typing import Optional

"""
Represents a captured state of a decorated pot.
"""
class DecoratedPot(TileState, BlockInventoryHolder):

    """
    Set the sherd on the provided side.

    @param side the side to set
    @param sherd the sherd, or None to set a blank side.
    @raises ValueError if the sherd is not either
    tagged by Tag.ITEMS_DECORATED_POT_SHERDS, Material.BRICK,
    or None
    """
    def set_sherd(self, side: Side, sherd: Optional[Material]) -> None: ...

    """
    Get the sherd on the provided side.

    @param side the side to get
    @return the sherd on the side or Material.BRICK if it's blank
    """
    def get_sherd(self, side: Side) -> Material: ...

    """
    Gets a Map of all sides on this decorated pot and the sherds on them.
    If a side does not have a specific sherd on it, Material.BRICK
    will be the value of that side.

    @return the sherds
    """
    def get_sherds(self) -> Dict[Side, Material]: ...

    """
    Gets the sherds on this decorated pot. For faces without a specific sherd,
    Material.BRICK is used in its place.

    @return the sherds
    @deprecated in favor of get_sherds()
    """
    def get_shards(self) -> List[Material]: ...

    """
    @return inventory
    @see Container.get_inventory()
    """
    def get_inventory(self) -> DecoratedPotInventory: ...

    """
    @return snapshot inventory
    @see Container.get_snapshot_inventory()
    """
    def get_snapshot_inventory(self) -> DecoratedPotInventory: ...

    """
    A side on a decorated pot. Sides are relative to the facing state of a
    org.bukkit.block.data.type.DecoratedPot.
    """
    class Side:
        BACK = ...
        LEFT = ...
        RIGHT = ...
        FRONT = ...
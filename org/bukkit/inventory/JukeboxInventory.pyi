from org.bukkit.block import Jukebox
from org.jetbrains.annotations import Nullable
from org.bukkit.inventory import Inventory
from org.bukkit.inventory import ItemStack

"""
Interface to the inventory of a Jukebox.
"""
class JukeboxInventory(Inventory):
    """
    Set the record in the jukebox.
    <p>
    This will immediately start playing the inserted item or stop playing if the
    item provided is null.

    @param item the new record
    """
    def set_record(self, item: Nullable[ItemStack]) -> None: ...

    """
    Get the record in the jukebox.

    @return the current record
    """
        def get_record(self) -> Nullable[ItemStack]: ...

        def get_holder(self) -> Nullable[Jukebox]: ...
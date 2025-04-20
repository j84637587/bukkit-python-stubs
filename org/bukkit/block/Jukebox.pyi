from typing import Optional
from org.bukkit import Material
from org.bukkit.inventory import BlockInventoryHolder, ItemStack, JukeboxInventory

class Jukebox(BlockInventoryHolder):
    """
    Represents a captured state of a jukebox.
    """

    def get_playing(self) -> Material:
        """
        Gets the record inserted into the jukebox.

        Returns:
            The record Material, or AIR if none is inserted
        """
        ...

    def set_playing(self, record: Optional[Material]) -> None:
        """
        Sets the record being played.

        Args:
            record: The record Material, or None/AIR to stop playing
        """
        ...

    def has_record(self) -> bool:
        """
        Gets whether or not this jukebox has a record.
        A jukebox can have a record but not be playing if it was stopped
        with stopPlaying or if a record has finished playing.

        Returns:
            True if this jukebox has a record, false if it the jukebox is empty
        """
        ...

    def get_record(self) -> ItemStack:
        """
        Gets the record item inserted into the jukebox.

        Returns:
            a copy of the inserted record, or an air stack if none
        """
        ...

    def set_record(self, record: Optional[ItemStack]) -> None:
        """
        Sets the record being played. The jukebox will start playing automatically.

        Args:
            record: the record to insert or None/AIR to empty
        """
        ...

    def is_playing(self) -> bool:
        """
        Checks if the jukebox is playing a record.

        Returns:
            True if there is a record playing
        """
        ...

    def start_playing(self) -> bool:
        """
        Starts the jukebox playing if there is a record.

        Returns:
            True if the jukebox had a record and was able to start playing,
            false if the jukebox was already playing or did not have a record
        """
        ...

    def stop_playing(self) -> None:
        """
        Stops the jukebox playing without ejecting the record.
        """
        ...

    def eject(self) -> bool:
        """
        Stops the jukebox playing and ejects the current record.
        If the block represented by this state is no longer a jukebox,
        this will do nothing and return false.

        Returns:
            True if a record was ejected; false if there was none playing

        Raises:
            IllegalStateException: if this block state is not placed
        """
        ...

    def get_inventory(self) -> JukeboxInventory:
        """
        @return inventory
        @see Container#getInventory()
        """
        ...

    def get_snapshot_inventory(self) -> JukeboxInventory:
        """
        @return snapshot inventory
        @see Container#getSnapshotInventory()
        """
        ...
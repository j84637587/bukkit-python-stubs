from org.bukkit.Location import Location
from org.bukkit.event.entity.CreatureSpawnEvent import CreatureSpawnEvent
from org.bukkit.inventory.InventoryHolder import InventoryHolder
from typing import Optional

class Allay(InventoryHolder):
    """
    An Allay.
    """

    def can_duplicate(self) -> bool:
        """
        Gets if the allay can duplicate.
        <br>
        <b>Note:</b> Duplication is based when the
        {@link #getDuplicationCooldown} its lower than zero.

        @return: if the allay can duplicate itself.
        """
        ...

    def set_can_duplicate(self, can_duplicate: bool) -> None:
        """
        Sets if the allay can duplicate.
        <br>
        <b>Note:</b> this value can be overridden later by
        {@link #getDuplicationCooldown} if is lower than zero. You can also use
        {@link #setDuplicationCooldown} to allow the allay to duplicate

        @param can_duplicate: if the allay can duplicate itself
        """
        ...

    def get_duplication_cooldown(self) -> int:
        """
        Gets the cooldown for duplicating the allay.

        @return: the time in ticks when allay can duplicate
        """
        ...

    def set_duplication_cooldown(self, cooldown: int) -> None:
        """
        Sets the cooldown before the allay can duplicate again.

        @param cooldown: the cooldown, use a negative number to deny allay to
        duplicate again.
        """
        ...

    def reset_duplication_cooldown(self) -> None:
        """
        Reset the cooldown for duplication.

        This will set the cooldown ticks to the same value as is set after an
        Allay has duplicated.
        """
        ...

    def is_dancing(self) -> bool:
        """
        Gets if the allay is dancing.

        @return: {@code True} if it is dancing, false otherwise.
        """
        ...

    def start_dancing(self, location: Location) -> None:
        """
        Causes the allay to start dancing because of the provided jukebox
        location.

        @param location: the location of the jukebox

        @raises IllegalArgumentException: if the block at the location is not a
        jukebox
        """
        ...

    def start_dancing(self) -> None:
        """
        Force sets the dancing status of the allay.
        <br>
        <b>Note:</b> This method forces the allay to dance, ignoring any nearby
        jukebox being required.
        """
        ...

    def stop_dancing(self) -> None:
        """
        Makes the allay stop dancing.
        """
        ...

    def duplicate_allay(self) -> Optional['Allay']:
        """
        This make the current allay duplicate itself without dance or item
        necessary.
        <b>Note:</b> this will fire a {@link CreatureSpawnEvent}

        @return: the new entity {@link Allay} or null if the spawn was cancelled
        """
        ...

    def get_jukebox(self) -> Optional[Location]:
        """
        Gets the jukebox the allay is set to dance to.

        @return: the location of the jukebox to dance if it exists
        """
        ...
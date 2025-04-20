from typing import Collection, Optional
from org.bukkit.Location import Location
from org.bukkit.entity.Animals import Animals

class Sniffer(Animals):
    """
    Represents a Sniffer.
    """

    def get_explored_locations(self) -> Collection[Location]:
        """
        Gets the locations explored by the sniffer.
        <br>
        <b>Note:</b> the returned locations use sniffer's current world.

        @return a collection of locations
        """
        ...

    def remove_explored_location(self, location: Location) -> None:
        """
        Remove a location of the explored locations.
        <br>
        <b>Note:</b> the location must be in the sniffer's current world for this
        method to have any effect.

        @param location the location to remove
        @see #getExploredLocations()
        """
        ...

    def add_explored_location(self, location: Location) -> None:
        """
        Add a location to the explored locations.
        <br>
        <b>Note:</b> the location must be in the sniffer's current world for this
        method to have any effect.

        @param location the location to add
        @see #getExploredLocations()
        """
        ...

    def get_state(self) -> 'Sniffer.State':
        """
        Get the current state of the sniffer.

        @return the state of the sniffer
        """
        ...

    def set_state(self, state: 'Sniffer.State') -> None:
        """
        Set a new state for the sniffer.
        <br>
        This will also make the sniffer make the transition to the new state.

        @param state the new state
        """
        ...

    def find_possible_dig_location(self) -> Optional[Location]:
        """
        Try to get a possible location where the sniffer can dig.

        @return a {@link Location} if found or null
        """
        ...

    def can_dig(self) -> bool:
        """
        Gets whether the sniffer can dig in the current {@link Location} below
        its head.

        @return {@code true} if can dig or {@code false} otherwise
        """
        ...

    class State:
        """
        Represents the current state of the Sniffer.
        """
        IDLING = ...
        FEELING_HAPPY = ...
        SCENTING = ...
        SNIFFING = ...
        SEARCHING = ...
        DIGGING = ...
        RISING = ...
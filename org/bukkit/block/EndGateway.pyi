from typing import Optional
from org.bukkit import Location

class EndGateway(TileState):
    """
    Represents a captured state of an end gateway.
    """

    def get_exit_location(self) -> Optional[Location]:
        """
        Gets the location that entities are teleported to when
        entering the gateway portal.
        <p>
        If this block state is not placed the location's world will be null.

        @return: the gateway exit location
        """
        ...

    def set_exit_location(self, location: Optional[Location]) -> None:
        """
        Sets the exit location that entities are teleported to when
        they enter the gateway portal.
        <p>
        If this block state is not placed the location's world has to be null.

        @param location: the new exit location
        @raises IllegalArgumentException: for differing worlds
        """
        ...

    def is_exact_teleport(self) -> bool:
        """
        Gets whether this gateway will teleport entities directly to
        the exit location instead of finding a nearby location.

        @return: true if the gateway is teleporting to the exact location
        """
        ...

    def set_exact_teleport(self, exact: bool) -> None:
        """
        Sets whether this gateway will teleport entities directly to
        the exit location instead of finding a nearby location.

        @param exact: whether to teleport to the exact location
        """
        ...

    def get_age(self) -> int:
        """
        Gets the age in ticks of the gateway.
        <br>
        If the age is less than 200 ticks a magenta beam will be emitted, whilst
        if it is a multiple of 2400 ticks a purple beam will be emitted.

        @return: age in ticks
        """
        ...

    def set_age(self, age: int) -> None:
        """
        Sets the age in ticks of the gateway.
        <br>
        If the age is less than 200 ticks a magenta beam will be emitted, whilst
        if it is a multiple of 2400 ticks a purple beam will be emitted.

        @param age: new age in ticks
        """
        ...

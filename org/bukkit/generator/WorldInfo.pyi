from uuid import UUID
from org.bukkit import World
from typing import Protocol

class WorldInfo(Protocol):
    """
    Holds various information of a World
    """

    def get_name(self) -> str:
        """
        Gets the unique name of this world

        Returns:
            Name of this world
        """
        ...

    def get_uid(self) -> UUID:
        """
        Gets the Unique ID of this world

        Returns:
            Unique ID of this world.
        """
        ...

    def get_environment(self) -> World.Environment:
        """
        Gets the {@link World.Environment} type of this world

        Returns:
            This worlds Environment type
        """
        ...

    def get_seed(self) -> int:
        """
        Gets the Seed for this world.

        Returns:
            This worlds Seed
        """
        ...

    def get_min_height(self) -> int:
        """
        Gets the minimum height of this world.
        <p>
        If the min height is 0, there are only blocks from y=0.

        Returns:
            Minimum height of the world
        """
        ...

    def get_max_height(self) -> int:
        """
        Gets the maximum height of this world.
        <p>
        If the max height is 100, there are only blocks from y=0 to y=99.

        Returns:
            Maximum height of the world
        """
        ...
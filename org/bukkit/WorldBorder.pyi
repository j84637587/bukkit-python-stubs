from typing import Optional
from enum import Enum

class TimeUnit(Enum):
    """Enum for time units."""
    NANOSECONDS = 1
    MICROSECONDS = 2
    MILLISECONDS = 3
    SECONDS = 4
    MINUTES = 5
    HOURS = 6
    DAYS = 7

class World:
    """Placeholder for World class."""
    pass

class Location:
    """Placeholder for Location class."""
    pass

class WorldBorder:
    """
    Interface representing a world border in a game world.
    """

    def get_world(self) -> Optional[World]:
        """
        Get the World in which the border resides.

        Returns:
            The associated world, or None if this world border is not associated
            with any specific world, such as those created via Server.createWorldBorder().
        """
        ...

    def reset(self) -> None:
        """
        Resets the border to default values.
        """
        ...

    def get_size(self) -> float:
        """
        Gets the current side length of the border.

        Returns:
            The current side length of the border.
        """
        ...

    def set_size(self, new_size: float) -> None:
        """
        Sets the border to a square region with the specified side length in blocks.

        Args:
            new_size: The new size of the border.

        Raises:
            ValueError: if new_size is less than 1.0 or greater than get_max_size().
        """
        ...

    def set_size_with_seconds(self, new_size: float, seconds: int) -> None:
        """
        Sets the border to a square region with the specified side length in blocks.

        Args:
            new_size: The new side length of the border.
            seconds: The time in seconds in which the border grows or shrinks from the previous size to that being set.

        Raises:
            ValueError: if new_size is less than 1.0 or greater than get_max_size().
        """
        ...

    def set_size_with_time_unit(self, new_size: float, unit: TimeUnit, time: int) -> None:
        """
        Sets the border to a square region with the specified side length in blocks.

        Args:
            new_size: The new side length of the border.
            unit: The time unit.
            time: The time in which the border grows or shrinks from the previous size to that being set.

        Raises:
            ValueError: if unit is None or new_size is less than 1.0 or greater than get_max_size().
        """
        ...

    def get_center(self) -> Location:
        """
        Gets the current border center.

        Returns:
            The current border center.
        """
        ...

    def set_center_with_coordinates(self, x: float, z: float) -> None:
        """
        Sets the new border center.

        Args:
            x: The new center x-coordinate.
            z: The new center z-coordinate.

        Raises:
            ValueError: if the absolute value of x or z is higher than get_max_center_coordinate().
        """
        ...

    def set_center_with_location(self, location: Location) -> None:
        """
        Sets the new border center.

        Args:
            location: The new location of the border center. (Only x/z used)

        Raises:
            ValueError: if location is None or the absolute value of Location.getX() or Location.getZ() is higher than get_max_center_coordinate().
        """
        ...

    def get_damage_buffer(self) -> float:
        """
        Gets the current border damage buffer.

        Returns:
            The current border damage buffer.
        """
        ...

    def set_damage_buffer(self, blocks: float) -> None:
        """
        Sets the amount of blocks a player may safely be outside the border before taking damage.

        Args:
            blocks: The amount of blocks. (The default is 5 blocks.)
        """
        ...

    def get_damage_amount(self) -> float:
        """
        Gets the current border damage amount.

        Returns:
            The current border damage amount.
        """
        ...

    def set_damage_amount(self, damage: float) -> None:
        """
        Sets the amount of damage a player takes when outside the border plus the border buffer.

        Args:
            damage: The amount of damage. (The default is 0.2 damage per second per block.)
        """
        ...

    def get_warning_time(self) -> int:
        """
        Gets the current border warning time in seconds.

        Returns:
            The current border warning time in seconds.
        """
        ...

    def set_warning_time(self, seconds: int) -> None:
        """
        Sets the warning time that causes the screen to be tinted red when a contracting border will reach the player within the specified time.

        Args:
            seconds: The amount of time in seconds. (The default is 15 seconds.)
        """
        ...

    def get_warning_distance(self) -> int:
        """
        Gets the current border warning distance.

        Returns:
            The current border warning distance.
        """
        ...

    def set_warning_distance(self, distance: int) -> None:
        """
        Sets the warning distance that causes the screen to be tinted red when the player is within the specified number of blocks from the border.

        Args:
            distance: The distance in blocks. (The default is 5 blocks.)
        """
        ...

    def is_inside(self, location: Location) -> bool:
        """
        Check if the specified location is inside this border.

        Args:
            location: the location to check

        Returns:
            if this location is inside the border or not
        """
        ...

    def get_max_size(self) -> float:
        """
        Gets the maximum possible size of a WorldBorder.

        Returns:
            The maximum size the WorldBorder
        """
        ...

    def get_max_center_coordinate(self) -> float:
        """
        Gets the absolute value of the maximum x/z center coordinate of a WorldBorder.

        Returns:
            The absolute maximum center coordinate of the WorldBorder
        """
        ...
from org.bukkit.entity import Entity
from org.bukkit.util import Vector
from typing import Protocol

class Vehicle(Protocol):
    """
    Represents a vehicle entity.
    """

    def get_velocity(self) -> Vector:
        """
        Gets the vehicle's velocity.

        Returns:
            velocity vector
        """
        ...

    def set_velocity(self, vel: Vector) -> None:
        """
        Sets the vehicle's velocity in meters per tick.

        Args:
            vel: velocity vector
        """
        ...
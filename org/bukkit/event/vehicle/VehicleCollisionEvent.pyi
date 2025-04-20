from org.bukkit.entity import Vehicle
from typing import Any

class VehicleCollisionEvent(VehicleEvent):
    """
    Raised when a vehicle collides.
    """

    def __init__(self, vehicle: Vehicle) -> None:
        ...
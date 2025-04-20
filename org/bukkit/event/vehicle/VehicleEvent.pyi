from org.bukkit.entity import Vehicle
from org.bukkit.event import Event
from typing import Any
from typing import Optional

class VehicleEvent(Event):
    """
    Represents a vehicle-related event.
    """

    vehicle: Vehicle

    def __init__(self, vehicle: Vehicle) -> None:
        """
        Initialize the VehicleEvent with the given vehicle.

        :param vehicle: The vehicle associated with this event.
        """
        ...

    def get_vehicle(self) -> Vehicle:
        """
        Get the vehicle.

        :return: the vehicle
        """
        ...
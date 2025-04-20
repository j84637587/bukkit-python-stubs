# pressure_sensor.pyi

from typing import Protocol

class PressureSensor(Protocol):
    """Interface for a pressure sensor."""

    def is_pressed(self) -> bool:
        """Returns True if the sensor is pressed, False otherwise."""
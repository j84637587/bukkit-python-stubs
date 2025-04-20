from typing import Protocol

class TileState(Protocol):
    pass

class SculkSensor(TileState, Protocol):
    """
    Represents a captured state of a sculk sensor
    """

    def get_last_vibration_frequency(self) -> int:
        """
        Gets the last vibration frequency of this sensor.

        Different activities detected by the sensor will produce different
        frequencies and dictate the output of connected comparators.

        @return frequency between 0-15.
        """
        ...

    def set_last_vibration_frequency(self, last_vibration_frequency: int) -> None:
        """
        Sets the last vibration frequency of this sensor.

        Different activities detected by the sensor will produce different
        frequencies and dictate the output of connected comparators.

        @param last_vibration_frequency frequency between 0-15.
        """
        ...
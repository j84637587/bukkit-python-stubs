from org.bukkit.block.data import AnaloguePowerable
from org.bukkit.block.data import Waterlogged
from typing import Literal, Protocol

class SculkSensor(AnaloguePowerable, Waterlogged):
    """
    'sculk_sensor_phase' indicates the current operational phase of the sensor.
    """

    def get_phase(self) -> 'Phase':
        """
        Gets the value of the 'sculk_sensor_phase' property.

        Returns:
            The 'sculk_sensor_phase' value.
        """
        ...

    def set_phase(self, phase: 'Phase') -> None:
        """
        Sets the value of the 'sculk_sensor_phase' property.

        Args:
            phase: The new 'sculk_sensor_phase' value.
        """
        ...

class Phase(Protocol):
    """
    The Phase of the sensor.
    """
    INACTIVE: Literal['INACTIVE']
    ACTIVE: Literal['ACTIVE']
    COOLDOWN: Literal['COOLDOWN']
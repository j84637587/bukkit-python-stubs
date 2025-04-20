from org.bukkit import World
from org.bukkit.event import Event
from typing import Any
from typing import Type

class WeatherEvent(Event):
    """
    Represents a Weather-related event
    """

    world: World

    def __init__(self, where: World) -> None:
        """
        Initializes the WeatherEvent with the specified World.

        :param where: The World where the event is occurring.
        """
        ...

    def get_world(self) -> World:
        """
        Returns the World where this event is occurring.

        :return: World this event is occurring in.
        """
        ...
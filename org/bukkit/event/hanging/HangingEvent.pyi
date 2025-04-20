from org.bukkit.entity import Hanging
from org.bukkit.event import Event
from typing import Any
from typing import Optional

class HangingEvent(Event):
    """
    Represents a hanging entity-related event.
    """

    hanging: Hanging

    def __init__(self, painting: Hanging) -> None:
        """
        Initializes a HangingEvent with the specified hanging entity.

        :param painting: the hanging entity
        """
        ...

    def get_entity(self) -> Hanging:
        """
        Gets the hanging entity involved in this event.

        :return: the hanging entity
        """
        ...
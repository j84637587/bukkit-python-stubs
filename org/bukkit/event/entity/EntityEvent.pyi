from org.bukkit.entity import Entity
from org.bukkit.entity import EntityType
from org.bukkit.event import Event
from typing import Any
from typing import Type

class EntityEvent(Event):
    """
    Represents an Entity-related event
    """

    entity: Entity

    def __init__(self, what: Entity) -> None:
        """
        Initializes the EntityEvent with the specified Entity.

        :param what: Entity who is involved in this event
        """
        ...

    def get_entity(self) -> Entity:
        """
        Returns the Entity involved in this event

        :return: Entity who is involved in this event
        """
        ...

    def get_entity_type(self) -> EntityType:
        """
        Gets the EntityType of the Entity involved in this event.

        :return: EntityType of the Entity involved in this event
        """
        ...
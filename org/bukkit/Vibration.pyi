from typing import Protocol
import org.bukkit.block import Block
from org.bukkit.entity import Entity
from org.bukkit import Location

class Vibration:
    """
    Represents a vibration from a Skulk sensor.
    """

    def __init__(self, origin: Location, destination: 'Vibration.Destination', arrival_time: int) -> None:
        ...

    def get_origin(self) -> Location:
        """
        Get the origin of the vibration.

        :return: origin
        """
        ...

    def get_destination(self) -> 'Vibration.Destination':
        """
        Get the vibration destination.

        :return: destination
        """
        ...

    def get_arrival_time(self) -> int:
        """
        Get the vibration arrival time in ticks.

        :return: arrival time
        """
        ...


class Destination(Protocol):
    ...


class EntityDestination(Destination):
    def __init__(self, entity: Entity) -> None:
        ...

    def get_entity(self) -> Entity:
        ...


class BlockDestination(Destination):
    def __init__(self, block: Location) -> None:
        ...

    def __init__(self, block: Block) -> None:
        ...

    def get_location(self) -> Location:
        ...

    def get_block(self) -> Block:
        ...
from typing import NoReturn
from org.bukkit.entity import EntitySnapshot
from org.jetbrains.annotations import ApiStatus, NotNull

class EntityFactory:
    """
    Interface for creating entity snapshots.
    """

    def create_entity_snapshot(self, input: str) -> EntitySnapshot:
        """
        Create a new EntitySnapshot with the supplied input.<br>
        Accepts strings in the format output by {@link EntitySnapshot#getAsString()}.

        :param input: the input string
        :return: the created EntitySnapshot
        :raises IllegalArgumentException: if the input string was provided in an invalid or unsupported format
        """
        ...

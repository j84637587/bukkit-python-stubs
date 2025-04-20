from org.bukkit.entity import Entity
from org.bukkit.generator import LimitedRegion
from typing import Protocol

"""
A EntityTransformer is used to modify entities that are spawned by structure.
"""
class EntityTransformer(Protocol):
    """
    A functional interface for transforming entities.
    """

    def transform(
        self,
        region: LimitedRegion,
        x: int,
        y: int,
        z: int,
        entity: Entity,
        allowed_to_spawn: bool
    ) -> bool:
        """
        Transforms a entity in a structure.

        :param region: the accessible region
        :param x: the x position of the entity
        :param y: the y position of the entity
        :param z: the z position of the entity
        :param entity: the entity
        :param allowed_to_spawn: if the entity is allowed to spawn

        :return: True if the entity should be spawned otherwise False
        """
        ...
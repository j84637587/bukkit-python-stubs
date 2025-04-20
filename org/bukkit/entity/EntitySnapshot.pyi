from org.bukkit.Location import Location
from org.bukkit.World import World
from org.bukkit.entity.Entity import Entity
from org.bukkit.entity.EntityType import EntityType
from typing import Protocol
from org.jetbrains.annotations import NotNull, ApiStatus

"""
Represents an immutable copy of an entity's state. Can be used at any time to
create an instance of the stored entity.
"""
class EntitySnapshot(Protocol):

    """
    Creates an entity using this template. Does not spawn the copy in the world.
    <br>

    @param world the world to create the entity in
    @return a copy of this entity.
    """
    def create_entity(self, world: NotNull[World]) -> NotNull[Entity]: ...

    """
    Creates an entity using this template and spawns it at the provided location.

    @param to the location to copy to
    @return the new entity.
    """
    def create_entity(self, to: NotNull[Location]) -> NotNull[Entity]: ...

    """
    Gets the type of entity this template holds.

    @return the type
    """
    def get_entity_type(self) -> NotNull[EntityType]: ...

    """
    Get this EntitySnapshot as an NBT string.
    <p>
    This string should not be relied upon as a serializable value.

    @return the NBT string
    """
        def get_as_string(self) -> NotNull[str]: ...
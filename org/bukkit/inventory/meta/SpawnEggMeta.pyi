from org.bukkit.entity import EntitySnapshot
from org.bukkit.entity import EntityType
from typing import Optional
from org.bukkit.inventory.meta import ItemMeta

"""
Represents a spawn egg and its spawned type.
"""
class SpawnEggMeta(ItemMeta):

    """
    Get the type of entity this egg will spawn.

    @return The entity type. May be None for implementation specific default.
    @deprecated different types are different items
    """
    def get_spawned_type(self) -> Optional[EntityType]:
        ...

    """
    Set the type of entity this egg will spawn.

    @param type The entity type. May be None for implementation specific
    default.
    @deprecated different types are different items
    """
    def set_spawned_type(self, type: Optional[EntityType]) -> None:
        ...

    """
    Gets the EntitySnapshot that will be spawned by this spawn egg or None if no entity
    has been set. 
    All applicable data from the egg will be copied, such as custom name, health,
    and velocity. 

    @return the entity snapshot or None if no entity has been set
    """
    def get_spawned_entity(self) -> Optional[EntitySnapshot]:
        ...

    """
    Sets the EntitySnapshot that will be spawned by this spawn egg. 
    All applicable data from the entity will be copied, such as custom name,
    health, and velocity. 

    @param snapshot the snapshot
    """
    def set_spawned_entity(self, snapshot: EntitySnapshot) -> None:
        ...

    def clone(self) -> 'SpawnEggMeta':
        ...
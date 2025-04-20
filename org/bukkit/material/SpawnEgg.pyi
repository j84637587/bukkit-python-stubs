from org.bukkit import Material
from org.bukkit.entity import EntityType
from org.bukkit.inventory.meta import SpawnEggMeta

"""
Represents a spawn egg that can be used to spawn mobs
@deprecated use {@link SpawnEggMeta}
"""
class SpawnEgg(MaterialData):

    def __init__(self) -> None:
        ...

    """
    @param type the type
    @param data the raw data value
    @deprecated Magic value
    """
    @Deprecated(since="1.6.2")
    def __init__(self, type: Material, data: bytes) -> None:
        ...

    """
    @param data the raw data value
    @deprecated Magic value
    """
    @Deprecated(since="1.6.2")
    def __init__(self, data: bytes) -> None:
        ...

    def __init__(self, type: EntityType) -> None:
        ...

    """
    Get the type of entity this egg will spawn.

    @return The entity type.
    @deprecated This is now stored in {@link SpawnEggMeta}.
    """
    @Deprecated(since="1.9")
    def get_spawned_type(self) -> EntityType:
        ...

    """
    Set the type of entity this egg will spawn.

    @param type The entity type.
    @deprecated This is now stored in {@link SpawnEggMeta}.
    """
    @Deprecated(since="1.9")
    def set_spawned_type(self, type: EntityType) -> None:
        ...

    def __str__(self) -> str:
        ...

    def clone(self) -> 'SpawnEgg':
        ...
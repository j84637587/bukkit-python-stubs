from org.bukkit.Location import Location
from org.bukkit.entity.Item import Item
from org.bukkit.event.entity.EntitySpawnEvent import EntitySpawnEvent
from typing import Any

class ItemSpawnEvent(EntitySpawnEvent):
    """
    Called when an item is spawned into a world
    """

    def __init__(self: "ItemSpawnEvent", spawnee: Item, loc: Location) -> None:
        """
        @Deprecated(since = "1.13.2")
        """
        ...

    def __init__(self: "ItemSpawnEvent", spawnee: Item) -> None:
        ...
    
    def get_entity(self: "ItemSpawnEvent") -> Item:
        ...
from org.bukkit.block import CreatureSpawner
from org.bukkit.entity import Entity
from org.bukkit.event.entity import EntitySpawnEvent
from typing import Any

class SpawnerSpawnEvent(EntitySpawnEvent):
    """
    Called when an entity is spawned into a world by a spawner.
    <p>
    If a Spawner Spawn event is cancelled, the entity will not spawn.
    """

    def __init__(self, spawnee: Entity, spawner: CreatureSpawner) -> None:
        ...

    def get_spawner(self) -> CreatureSpawner:
        ...
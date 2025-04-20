from org.bukkit.block import TrialSpawner
from org.bukkit.entity import Entity
from org.bukkit.event.entity import EntitySpawnEvent
from org.jetbrains.annotations import ApiStatus, NotNull

"""
Called when an entity is spawned into a world by a trial spawner.
<p>
If a Trial Spawner Spawn event is cancelled, the entity will not spawn.
"""
class TrialSpawnerSpawnEvent(EntitySpawnEvent):
    spawner: TrialSpawner

    def __init__(self, spawnee: NotNull[Entity], spawner: NotNull[TrialSpawner]) -> None:
        super().__init__(spawnee)
        self.spawner = spawner

        def get_trial_spawner(self) -> TrialSpawner:
        return self.spawner
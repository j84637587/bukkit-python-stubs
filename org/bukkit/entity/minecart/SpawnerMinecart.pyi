from org.bukkit.entity import Minecart
from org.bukkit.spawner import Spawner

"""
Represents a Minecart with an {@link org.bukkit.block.CreatureSpawner
entity spawner} inside it.
"""
class SpawnerMinecart(Minecart, Spawner):
    pass
from org.bukkit.Chunk import Chunk
from org.bukkit.entity.LivingEntity import LivingEntity
from org.bukkit.event.world.ChunkLoadEvent import ChunkLoadEvent
from typing import Literal, Type
from org.jetbrains.annotations import NotNull

class CreatureSpawnEvent(EntitySpawnEvent):
    """
    Called when a creature is spawned into a world.
    <p>
    If a Creature Spawn event is cancelled, the creature will not spawn.
    """

    spawnReason: 'CreatureSpawnEvent.SpawnReason'

    def __init__(self, spawnee: LivingEntity, spawnReason: 'CreatureSpawnEvent.SpawnReason') -> None:
        super().__init__(spawnee)
        self.spawnReason = spawnReason

        def getEntity(self) -> LivingEntity:
        pass

    """
    Gets the reason for why the creature is being spawned.

    @return A SpawnReason value detailing the reason for the creature being
        spawned
    """
        def getSpawnReason(self) -> 'CreatureSpawnEvent.SpawnReason':
        pass

    class SpawnReason:
        """
        An enum to specify the type of spawning
        """
        NATURAL: Literal['NATURAL']
        JOCKEY: Literal['JOCKEY']
        CHUNK_GEN: Literal['CHUNK_GEN']
        SPAWNER: Literal['SPAWNER']
        TRIAL_SPAWNER: Literal['TRIAL_SPAWNER']
        EGG: Literal['EGG']
        SPAWNER_EGG: Literal['SPAWNER_EGG']
        BUCKET: Literal['BUCKET']
        LIGHTNING: Literal['LIGHTNING']
        BUILD_SNOWMAN: Literal['BUILD_SNOWMAN']
        BUILD_IRONGOLEM: Literal['BUILD_IRONGOLEM']
        BUILD_WITHER: Literal['BUILD_WITHER']
        VILLAGE_DEFENSE: Literal['VILLAGE_DEFENSE']
        VILLAGE_INVASION: Literal['VILLAGE_INVASION']
        BREEDING: Literal['BREEDING']
        SLIME_SPLIT: Literal['SLIME_SPLIT']
        REINFORCEMENTS: Literal['REINFORCEMENTS']
        NETHER_PORTAL: Literal['NETHER_PORTAL']
        DISPENSE_EGG: Literal['DISPENSE_EGG']
        INFECTION: Literal['INFECTION']
        CURED: Literal['CURED']
        OCELOT_BABY: Literal['OCELOT_BABY']
        SILVERFISH_BLOCK: Literal['SILVERFISH_BLOCK']
        MOUNT: Literal['MOUNT']
        TRAP: Literal['TRAP']
        ENDER_PEARL: Literal['ENDER_PEARL']
        SHOULDER_ENTITY: Literal['SHOULDER_ENTITY']
        DROWNED: Literal['DROWNED']
        SHEARED: Literal['SHEARED']
        EXPLOSION: Literal['EXPLOSION']
        RAID: Literal['RAID']
        PATROL: Literal['PATROL']
        BEEHIVE: Literal['BEEHIVE']
        PIGLIN_ZOMBIFIED: Literal['PIGLIN_ZOMBIFIED']
        SPELL: Literal['SPELL']
        FROZEN: Literal['FROZEN']
        METAMORPHOSIS: Literal['METAMORPHOSIS']
        DUPLICATION: Literal['DUPLICATION']
        COMMAND: Literal['COMMAND']
        ENCHANTMENT: Literal['ENCHANTMENT']
        POTION_EFFECT: Literal['POTION_EFFECT']
        CUSTOM: Literal['CUSTOM']
        DEFAULT: Literal['DEFAULT']
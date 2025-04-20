from typing import Collection
from org.bukkit import NamespacedKey, Registry

class GameEvent:
    """
    Represents a generic Mojang game event.
    """
    BLOCK_ACTIVATE: 'GameEvent'
    BLOCK_ATTACH: 'GameEvent'
    BLOCK_CHANGE: 'GameEvent'
    BLOCK_CLOSE: 'GameEvent'
    BLOCK_DEACTIVATE: 'GameEvent'
    BLOCK_DESTROY: 'GameEvent'
    BLOCK_DETACH: 'GameEvent'
    BLOCK_OPEN: 'GameEvent'
    BLOCK_PLACE: 'GameEvent'
    BLOCK_PRESS: 'GameEvent'
    BLOCK_SWITCH: 'GameEvent'
    BLOCK_UNPRESS: 'GameEvent'
    BLOCK_UNSWITCH: 'GameEvent'
    CONTAINER_CLOSE: 'GameEvent'
    CONTAINER_OPEN: 'GameEvent'
    DISPENSE_FAIL: 'GameEvent'
    DRINK: 'GameEvent'
    DRINKING_FINISH: 'GameEvent'
    EAT: 'GameEvent'
    ELYTRA_FREE_FALL: 'GameEvent'
    ELYTRA_GLIDE: 'GameEvent'
    ENTITY_DAMAGE: 'GameEvent'
    ENTITY_DAMAGED: 'GameEvent'
    ENTITY_DIE: 'GameEvent'
    ENTITY_DISMOUNT: 'GameEvent'
    ENTITY_DYING: 'GameEvent'
    ENTITY_INTERACT: 'GameEvent'
    ENTITY_MOUNT: 'GameEvent'
    ENTITY_KILLED: 'GameEvent'
    ENTITY_PLACE: 'GameEvent'
    ENTITY_ACTION: 'GameEvent'
    ENTITY_ROAR: 'GameEvent'
    ENTITY_SHAKE: 'GameEvent'
    EQUIP: 'GameEvent'
    EXPLODE: 'GameEvent'
    FLAP: 'GameEvent'
    FLUID_PICKUP: 'GameEvent'
    FLUID_PLACE: 'GameEvent'
    HIT_GROUND: 'GameEvent'
    INSTRUMENT_PLAY: 'GameEvent'
    ITEM_INTERACT_FINISH: 'GameEvent'
    ITEM_INTERACT_START: 'GameEvent'
    JUKEBOX_PLAY: 'GameEvent'
    JUKEBOX_STOP_PLAY: 'GameEvent'
    LIGHTNING_STRIKE: 'GameEvent'
    MOB_INTERACT: 'GameEvent'
    NOTE_BLOCK_PLAY: 'GameEvent'
    PISTON_CONTRACT: 'GameEvent'
    PISTON_EXTEND: 'GameEvent'
    PRIME_FUSE: 'GameEvent'
    PROJECTILE_LAND: 'GameEvent'
    PROJECTILE_SHOOT: 'GameEvent'
    RAVAGER_ROAR: 'GameEvent'
    RING_BELL: 'GameEvent'
    SCULK_SENSOR_TENDRILS_CLICKING: 'GameEvent'
    SHEAR: 'GameEvent'
    SHRIEK: 'GameEvent'
    SHULKER_CLOSE: 'GameEvent'
    SHULKER_OPEN: 'GameEvent'
    SPLASH: 'GameEvent'
    STEP: 'GameEvent'
    SWIM: 'GameEvent'
    TELEPORT: 'GameEvent'
    UNEQUIP: 'GameEvent'
    WOLF_SHAKING: 'GameEvent'
    RESONATE_1: 'GameEvent'
    RESONATE_2: 'GameEvent'
    RESONATE_3: 'GameEvent'
    RESONATE_4: 'GameEvent'
    RESONATE_5: 'GameEvent'
    RESONATE_6: 'GameEvent'
    RESONATE_7: 'GameEvent'
    RESONATE_8: 'GameEvent'
    RESONATE_9: 'GameEvent'
    RESONATE_10: 'GameEvent'
    RESONATE_11: 'GameEvent'
    RESONATE_12: 'GameEvent'
    RESONATE_13: 'GameEvent'
    RESONATE_14: 'GameEvent'
    RESONATE_15: 'GameEvent'

    def getKey(self) -> NamespacedKey:
        """
        {@inheritDoc}
        @see #getKeyOrThrow()
        @see #isRegistered()
        @deprecated A key might not always be present, use {@link #getKeyOrThrow()} instead.
        """
        pass

    @staticmethod
    def getByKey(namespacedKey: NamespacedKey) -> 'GameEvent':
        """
        Returns a {@link GameEvent} by a {@link NamespacedKey}.
        @param namespacedKey the key
        @return the event or null
        @deprecated Use {@link Registry#get(NamespacedKey)} instead.
        """
        pass

    @staticmethod
    def values() -> Collection['GameEvent']:
        """
        Returns the set of all GameEvents.
        @return the memoryKeys
        @deprecated use {@link Registry#iterator()}.
        """
        pass

    @staticmethod
    def getEvent(key: str) -> 'GameEvent':
        pass
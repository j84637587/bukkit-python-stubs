from typing import Dict, Type, Union, Optional

class GameRule:
    """
    GameRules dictate certain behavior within Minecraft itself
    For more information please visit the
    Minecraft Wiki
    """
    gameRules: Dict[str, 'GameRule'] = {}

    # Boolean rules
    ANNOUNCE_ADVANCEMENTS: 'GameRule[bool]'
    COMMAND_BLOCK_OUTPUT: 'GameRule[bool]'
    DISABLE_PLAYER_MOVEMENT_CHECK: 'GameRule[bool]'
    DISABLE_ELYTRA_MOVEMENT_CHECK: 'GameRule[bool]'
    DO_DAYLIGHT_CYCLE: 'GameRule[bool]'
    DO_ENTITY_DROPS: 'GameRule[bool]'
    DO_FIRE_TICK: 'GameRule[bool]'
    ALLOW_FIRE_TICKS_AWAY_FROM_PLAYER: 'GameRule[bool]'
    DO_LIMITED_CRAFTING: 'GameRule[bool]'
    DO_MOB_LOOT: 'GameRule[bool]'
    PROJECTILES_CAN_BREAK_BLOCKS: 'GameRule[bool]'
    DO_MOB_SPAWNING: 'GameRule[bool]'
    DO_TILE_DROPS: 'GameRule[bool]'
    DO_WEATHER_CYCLE: 'GameRule[bool]'
    KEEP_INVENTORY: 'GameRule[bool]'
    LOG_ADMIN_COMMANDS: 'GameRule[bool]'
    MOB_GRIEFING: 'GameRule[bool]'
    NATURAL_REGENERATION: 'GameRule[bool]'
    REDUCED_DEBUG_INFO: 'GameRule[bool]'
    SEND_COMMAND_FEEDBACK: 'GameRule[bool]'
    SHOW_DEATH_MESSAGES: 'GameRule[bool]'
    SPECTATORS_GENERATE_CHUNKS: 'GameRule[bool]'
    DISABLE_RAIDS: 'GameRule[bool]'
    DO_INSOMNIA: 'GameRule[bool]'
    DO_IMMEDIATE_RESPAWN: 'GameRule[bool]'
    DROWNING_DAMAGE: 'GameRule[bool]'
    FALL_DAMAGE: 'GameRule[bool]'
    FIRE_DAMAGE: 'GameRule[bool]'
    FREEZE_DAMAGE: 'GameRule[bool]'
    DO_PATROL_SPAWNING: 'GameRule[bool]'
    DO_TRADER_SPAWNING: 'GameRule[bool]'
    DO_WARDEN_SPAWNING: 'GameRule[bool]'
    FORGIVE_DEAD_PLAYERS: 'GameRule[bool]'
    UNIVERSAL_ANGER: 'GameRule[bool]'
    BLOCK_EXPLOSION_DROP_DECAY: 'GameRule[bool]'
    MOB_EXPLOSION_DROP_DECAY: 'GameRule[bool]'
    TNT_EXPLOSION_DROP_DECAY: 'GameRule[bool]'
    WATER_SOURCE_CONVERSION: 'GameRule[bool]'
    LAVA_SOURCE_CONVERSION: 'GameRule[bool]'
    GLOBAL_SOUND_EVENTS: 'GameRule[bool]'
    DO_VINES_SPREAD: 'GameRule[bool]'
    ENDER_PEARLS_VANISH_ON_DEATH: 'GameRule[bool]'
    TNT_EXPLODES: 'GameRule[bool]'

    # Numerical rules
    RANDOM_TICK_SPEED: 'GameRule[int]'
    SPAWN_RADIUS: 'GameRule[int]'
    MAX_ENTITY_CRAMMING: 'GameRule[int]'
    MAX_COMMAND_CHAIN_LENGTH: 'GameRule[int]'
    MAX_COMMAND_FORK_COUNT: 'GameRule[int]'
    COMMAND_MODIFICATION_BLOCK_LIMIT: 'GameRule[int]'
    PLAYERS_SLEEPING_PERCENTAGE: 'GameRule[int]'
    SNOW_ACCUMULATION_HEIGHT: 'GameRule[int]'
    PLAYERS_NETHER_PORTAL_DEFAULT_DELAY: 'GameRule[int]'
    PLAYERS_NETHER_PORTAL_CREATIVE_DELAY: 'GameRule[int]'
    MINECART_MAX_SPEED: 'GameRule[int]'
    SPAWN_CHUNK_RADIUS: 'GameRule[int]'

    name: str
    type: Type[Union[bool, int]]

    def __init__(self, name: str, clazz: Type[Union[bool, int]]) -> None:
        ...

    def getName(self) -> str:
        ...

    def getType(self) -> Type[Union[bool, int]]:
        ...

    def equals(self, obj: object) -> bool:
        ...

    def toString(self) -> str:
        ...

    @staticmethod
    def getByName(rule: str) -> Optional['GameRule']:
        ...

    @staticmethod
    def values() -> 'GameRule':
        ...
from typing import Type
from org.bukkit.entity import Entity, TippedArrow, Rabbit, SpawnerMinecart, LivingEntity, Egg, Snowball, EvokerFangs, Hoglin, IronGolem, Ravager, Warden, Zoglin, Tameable, Wolf, Sheep, ExplosiveMinecart, Villager, Witch, ZombieVillager, Firework, Ageable, Squid, Guardian, ArmorStand, Dolphin, Cat, Player, Fox, Goat, Sniffer

class EntityEffect:
    """
    A list of all Effects that can happen to entities.
    """
    ARROW_PARTICLES: 'EntityEffect'
    RABBIT_JUMP: 'EntityEffect'
    RESET_SPAWNER_MINECART_DELAY: 'EntityEffect'
    HURT: 'EntityEffect'
    DEATH: 'EntityEffect'
    EGG_BREAK: 'EntityEffect'
    SNOWBALL_BREAK: 'EntityEffect'
    ENTITY_DEATH: 'EntityEffect'
    FANG_ATTACK: 'EntityEffect'
    HOGLIN_ATTACK: 'EntityEffect'
    IRON_GOLEN_ATTACK: 'EntityEffect'
    RAVAGER_ATTACK: 'EntityEffect'
    WARDEN_ATTACK: 'EntityEffect'
    ZOGLIN_ATTACK: 'EntityEffect'
    WOLF_SMOKE: 'EntityEffect'
    WOLF_HEARTS: 'EntityEffect'
    WOLF_SHAKE: 'EntityEffect'
    SHEEP_EAT: 'EntityEffect'
    SHEEP_EAT_GRASS: 'EntityEffect'
    TNT_MINECART_IGNITE: 'EntityEffect'
    IRON_GOLEM_ROSE: 'EntityEffect'
    VILLAGER_HEART: 'EntityEffect'
    VILLAGER_ANGRY: 'EntityEffect'
    VILLAGER_HAPPY: 'EntityEffect'
    WITCH_MAGIC: 'EntityEffect'
    ZOMBIE_TRANSFORM: 'EntityEffect'
    FIREWORK_EXPLODE: 'EntityEffect'
    LOVE_HEARTS: 'EntityEffect'
    SQUID_ROTATE: 'EntityEffect'
    ENTITY_POOF: 'EntityEffect'
    GUARDIAN_TARGET: 'EntityEffect'
    SHIELD_BLOCK: 'EntityEffect'
    SHIELD_BREAK: 'EntityEffect'
    ARMOR_STAND_HIT: 'EntityEffect'
    THORNS_HURT: 'EntityEffect'
    IRON_GOLEM_SHEATH: 'EntityEffect'
    TOTEM_RESURRECT: 'EntityEffect'
    HURT_DROWN: 'EntityEffect'
    HURT_EXPLOSION: 'EntityEffect'
    DOLPHIN_FED: 'EntityEffect'
    RAVAGER_STUNNED: 'EntityEffect'
    CAT_TAME_FAIL: 'EntityEffect'
    CAT_TAME_SUCCESS: 'EntityEffect'
    VILLAGER_SPLASH: 'EntityEffect'
    PLAYER_BAD_OMEN_RAID: 'EntityEffect'
    HURT_BERRY_BUSH: 'EntityEffect'
    FOX_CHEW: 'EntityEffect'
    TELEPORT_ENDER: 'EntityEffect'
    BREAK_EQUIPMENT_MAIN_HAND: 'EntityEffect'
    BREAK_EQUIPMENT_OFF_HAND: 'EntityEffect'
    BREAK_EQUIPMENT_HELMET: 'EntityEffect'
    BREAK_EQUIPMENT_CHESTPLATE: 'EntityEffect'
    BREAK_EQUIPMENT_LEGGINGS: 'EntityEffect'
    BREAK_EQUIPMENT_BOOTS: 'EntityEffect'
    HONEY_BLOCK_SLIDE_PARTICLES: 'EntityEffect'
    HONEY_BLOCK_FALL_PARTICLES: 'EntityEffect'
    SWAP_HAND_ITEMS: 'EntityEffect'
    WOLF_SHAKE_STOP: 'EntityEffect'
    GOAT_LOWER_HEAD: 'EntityEffect'
    GOAT_RAISE_HEAD: 'EntityEffect'
    SPAWN_DEATH_SMOKE: 'EntityEffect'
    WARDEN_TENDRIL_SHAKE: 'EntityEffect'
    WARDEN_SONIC_ATTACK: 'EntityEffect'
    SNIFFER_DIG: 'EntityEffect'

    data: bytes
    applicable: Type[Entity]

    def __init__(self, data: int, clazz: Type[Entity]) -> None: ...

    def getData(self) -> bytes: ...
    
    def getApplicable(self) -> Type[Entity]: ...

    def isApplicableTo(self, entity: Entity) -> bool: ...

    def isApplicableTo(self, clazz: Type[Entity]) -> bool: ...
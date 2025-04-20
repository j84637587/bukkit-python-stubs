from typing import Dict, Callable, Union
from org.bukkit.Material import Material
from org.bukkit.WorldBorder import WorldBorder
from org.bukkit.damage.DamageSource import DamageSource
from org.bukkit.damage.DamageType import DamageType
from org.bukkit.entity.Entity import Entity
from org.bukkit.entity.Player import Player
from org.bukkit.event.Cancellable import Cancellable
from org.bukkit.event.HandlerList import HandlerList
from org.jetbrains.annotations import NotNull


class EntityDamageEvent(EntityEvent, Cancellable):
    """
    Stores data for damage events
    """

    handlers: HandlerList
    MODIFIERS: list
    ZERO: Callable[[float], float]

    def __init__(self, damagee: Entity, cause: 'DamageCause', damage: float) -> None:
        ...

    def __init__(self, damagee: Entity, cause: 'DamageCause', damageSource: DamageSource, damage: float) -> None:
        ...

    def __init__(self, damagee: Entity, cause: 'DamageCause', modifiers: Dict['DamageModifier', float], 
                 modifierFunctions: Dict['DamageModifier', Callable[[float], float]]) -> None:
        ...

    def __init__(self, damagee: Entity, cause: 'DamageCause', damageSource: DamageSource, 
                 modifiers: Dict['DamageModifier', float], 
                 modifierFunctions: Dict['DamageModifier', Callable[[float], float]]) -> None:
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...

    def getOriginalDamage(self, type: 'DamageModifier') -> float:
        ...

    def setDamage(self, type: 'DamageModifier', damage: float) -> None:
        ...

    def getDamage(self, type: 'DamageModifier') -> float:
        ...

    def isApplicable(self, type: 'DamageModifier') -> bool:
        ...

    def getDamage(self) -> float:
        ...

    def getFinalDamage(self) -> float:
        ...

    def setDamage(self, damage: float) -> None:
        ...

    def getCause(self) -> 'DamageCause':
        ...

    def getDamageSource(self) -> DamageSource:
        ...

    def getHandlers(self) -> HandlerList:
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        ...


class DamageModifier:
    """
    An enum to specify the types of modifier
    """

    BASE: 'DamageModifier'
    FREEZING: 'DamageModifier'
    HARD_HAT: 'DamageModifier'
    BLOCKING: 'DamageModifier'
    ARMOR: 'DamageModifier'
    RESISTANCE: 'DamageModifier'
    MAGIC: 'DamageModifier'
    ABSORPTION: 'DamageModifier'


class DamageCause:
    """
    An enum to specify the cause of the damage
    """

    KILL: 'DamageCause'
    WORLD_BORDER: 'DamageCause'
    CONTACT: 'DamageCause'
    ENTITY_ATTACK: 'DamageCause'
    ENTITY_SWEEP_ATTACK: 'DamageCause'
    PROJECTILE: 'DamageCause'
    SUFFOCATION: 'DamageCause'
    FALL: 'DamageCause'
    FIRE: 'DamageCause'
    FIRE_TICK: 'DamageCause'
    MELTING: 'DamageCause'
    LAVA: 'DamageCause'
    DROWNING: 'DamageCause'
    BLOCK_EXPLOSION: 'DamageCause'
    ENTITY_EXPLOSION: 'DamageCause'
    VOID: 'DamageCause'
    LIGHTNING: 'DamageCause'
    SUICIDE: 'DamageCause'
    STARVATION: 'DamageCause'
    POISON: 'DamageCause'
    MAGIC: 'DamageCause'
    WITHER: 'DamageCause'
    FALLING_BLOCK: 'DamageCause'
    THORNS: 'DamageCause'
    DRAGON_BREATH: 'DamageCause'
    CUSTOM: 'DamageCause'
    FLY_INTO_WALL: 'DamageCause'
    HOT_FLOOR: 'DamageCause'
    CAMPFIRE: 'DamageCause'
    CRAMMING: 'DamageCause'
    DRYOUT: 'DamageCause'
    FREEZE: 'DamageCause'
    SONIC_BOOM: 'DamageCause'
from typing import Dict, Callable
from org.bukkit.damage import DamageSource
from org.bukkit.damage import DamageType
from org.bukkit.entity import Entity
from org.bukkit.event.entity import EntityDamageEvent
from org.bukkit.event.entity import DamageCause
from org.bukkit.event.entity import DamageModifier

class EntityDamageByEntityEvent(EntityDamageEvent):
    """
    Called when an entity is damaged by an entity
    """

    def __init__(self, damager: Entity, damagee: Entity, cause: DamageCause, damage: float) -> None:
        ...

    def __init__(self, damager: Entity, damagee: Entity, cause: DamageCause, damage_source: DamageSource, damage: float) -> None:
        ...

    def __init__(self, damager: Entity, damagee: Entity, cause: DamageCause, modifiers: Dict[DamageModifier, float], modifier_functions: Dict[DamageModifier, Callable[[float], float]]) -> None:
        ...

    def __init__(self, damager: Entity, damagee: Entity, cause: DamageCause, damage_source: DamageSource, modifiers: Dict[DamageModifier, float], modifier_functions: Dict[DamageModifier, Callable[[float], float]]) -> None:
        ...

    def get_damager(self) -> Entity:
        """
        Returns the entity that damaged the defender.

        :return: Entity that damaged the defender.
        """
        ...
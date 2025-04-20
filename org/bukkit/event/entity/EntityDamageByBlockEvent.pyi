from typing import Dict, Callable, Optional
from org.bukkit.block import Block
from org.bukkit.block import BlockState
from org.bukkit.damage import DamageSource
from org.bukkit.damage import DamageType
from org.bukkit.entity import Entity
from org.bukkit.event.entity import EntityDamageEvent
from org.bukkit.event.entity import DamageCause
from org.bukkit.event.entity import DamageModifier
from org.jetbrains.annotations import NotNull, Nullable

class EntityDamageByBlockEvent(EntityDamageEvent):
    """
    Called when an entity is damaged by a block
    """

    def __init__(self,
                 damager: Optional[Block],
                 damagee: Entity,
                 cause: DamageCause,
                 damage: float) -> None:
        ...

    def __init__(self,
                 damager: Optional[Block],
                 damagerState: Optional[BlockState],
                 damagee: Entity,
                 cause: DamageCause,
                 damageSource: DamageSource,
                 damage: float) -> None:
        ...

    def __init__(self,
                 damager: Optional[Block],
                 damagee: Entity,
                 cause: DamageCause,
                 modifiers: Dict[DamageModifier, float],
                 modifierFunctions: Dict[DamageModifier, Callable[[float], float]]) -> None:
        ...

    def __init__(self,
                 damager: Optional[Block],
                 damagerState: Optional[BlockState],
                 damagee: Entity,
                 cause: DamageCause,
                 damageSource: DamageSource,
                 modifiers: Dict[DamageModifier, float],
                 modifierFunctions: Dict[DamageModifier, Callable[[float], float]]) -> None:
        ...

        def getDamager(self) -> Optional[Block]:
        """
        Returns the block that damaged the player.

        @return Block that damaged the player
        """
        ...

        def getDamagerBlockState(self) -> Optional[BlockState]:
        """
        Returns the captured BlockState of the block that damaged the player.

        @return the block state
        """
        ...
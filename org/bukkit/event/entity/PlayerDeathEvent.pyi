from typing import List, Optional
from org.bukkit.damage import DamageSource
from org.bukkit.entity import Player
from org.bukkit.inventory import ItemStack
from org.bukkit.event.entity import EntityDeathEvent

class PlayerDeathEvent(EntityDeathEvent):
    """
    Thrown whenever a {@link Player} dies
    """

    def __init__(self, player: Player, damage_source: DamageSource, drops: List[ItemStack], dropped_exp: int, death_message: Optional[str] = None) -> None:
        ...

    def __init__(self, player: Player, damage_source: DamageSource, drops: List[ItemStack], dropped_exp: int, new_exp: int, death_message: Optional[str] = None) -> None:
        ...

    def __init__(self, player: Player, damage_source: DamageSource, drops: List[ItemStack], dropped_exp: int, new_exp: int, new_total_exp: int, new_level: int, death_message: Optional[str] = None) -> None:
        ...

    def get_entity(self) -> Player:
        ...

    def set_death_message(self, death_message: Optional[str]) -> None:
        ...

    def get_death_message(self) -> Optional[str]:
        ...

    def get_new_exp(self) -> int:
        ...

    def set_new_exp(self, exp: int) -> None:
        ...

    def get_new_level(self) -> int:
        ...

    def set_new_level(self, level: int) -> None:
        ...

    def get_new_total_exp(self) -> int:
        ...

    def set_new_total_exp(self, total_exp: int) -> None:
        ...

    def get_keep_level(self) -> bool:
        ...

    def set_keep_level(self, keep_level: bool) -> None:
        ...

    def set_keep_inventory(self, keep_inventory: bool) -> None:
        ...

    def get_keep_inventory(self) -> bool:
        ...
from org.bukkit.entity import Entity
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable
from org.bukkit.event.entity import EntityUnleashEvent
from org.bukkit.inventory import EquipmentSlot
from typing import Literal

class PlayerUnleashEntityEvent(EntityUnleashEvent, Cancellable):
    """
    Called prior to an entity being unleashed due to a player's action.
    """

    def __init__(self, entity: Entity, player: Player, hand: EquipmentSlot) -> None:
        ...

    @classmethod
    def deprecated_init(cls, entity: Entity, player: Player) -> None:
        ...

    """
    Returns the player who is unleashing the entity.

    @return: The player
    """
    def get_player(self) -> Player:
        ...

    """
    Get the hand used by the player to unleash the entity.

    @return: the hand
    """
    def get_hand(self) -> EquipmentSlot:
        ...

    def is_cancelled(self) -> bool:
        ...

    def set_cancelled(self, cancel: bool) -> None:
        ...
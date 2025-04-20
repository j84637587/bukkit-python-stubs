from org.bukkit.Location import Location
from org.bukkit.block.Block import Block
from org.bukkit.entity.Player import Player
from org.bukkit.event.Cancellable import Cancellable
from org.bukkit.event.HandlerList import HandlerList
from typing import Any

class PlayerBedLeaveEvent(PlayerEvent, Cancellable):
    """
    This event is fired when the player is leaving a bed.
    """

    handlers: HandlerList

    def __init__(self, who: Player, bed: Block, setBedSpawn: bool) -> None:
        ...

    def get_bed(self) -> Block:
        """
        Returns the bed block involved in this event.

        Returns:
            Block: the bed block involved in this event
        """
        ...

    def should_set_spawn_location(self) -> bool:
        """
        Get if this event should set the new spawn location for the
        Player.
        This does not remove any existing spawn location, only prevent it from
        being changed (if true).
        To change a Player's spawn location, use
        Player#setBedSpawnLocation(Location).

        Returns:
            bool: true if the spawn location will be changed
        """
        ...

    def set_spawn_location(self, setBedSpawn: bool) -> None:
        """
        Set if this event should set the new spawn location for the
        Player.
        This will not remove any existing spawn location, only prevent it from
        being changed (if true).
        To change a Player's spawn location, use
        Player#setBedSpawnLocation(Location).

        Args:
            setBedSpawn (bool): true to change the new spawn location
        """
        ...

    def is_cancelled(self) -> bool:
        ...

    def set_cancelled(self, cancelled: bool) -> None:
        ...

    def get_handlers(self) -> HandlerList:
        ...

    @staticmethod
    def get_handler_list() -> HandlerList:
        ...
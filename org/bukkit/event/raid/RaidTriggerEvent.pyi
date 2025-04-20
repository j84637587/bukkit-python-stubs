from org.bukkit.Raid import Raid
from org.bukkit.World import World
from org.bukkit.entity.Player import Player
from org.bukkit.event.Cancellable import Cancellable
from org.bukkit.event.HandlerList import HandlerList
from org.bukkit.event.raid.RaidEvent import RaidEvent
from typing import Any

class RaidTriggerEvent(RaidEvent, Cancellable):
    """
    Called when a {@link Raid} is triggered (e.g: a player with Bad Omen effect
    enters a village).
    """

    handlers: HandlerList

    def __init__(self, raid: Raid, world: World, player: Player) -> None:
        ...

    """
    Returns the player who triggered the raid.

    @return triggering player
    """
    def getPlayer(self) -> Player:
        ...

    def isCancelled(self) -> bool:
        ...

    def setCancelled(self, cancel: bool) -> None:
        ...

    def getHandlers(self) -> HandlerList:
        ...

    @staticmethod
    def getHandlerList() -> HandlerList:
        ...
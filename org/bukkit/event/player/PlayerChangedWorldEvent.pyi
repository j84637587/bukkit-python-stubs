from org.bukkit.World import World
from org.bukkit.entity.Player import Player
from org.bukkit.event.HandlerList import HandlerList
from org.bukkit.event.player.PlayerEvent import PlayerEvent
from typing import Any

class PlayerChangedWorldEvent(PlayerEvent):
    """
    Called when a player switches to another world.
    """

    handlers: HandlerList = HandlerList()
    from_: World

    def __init__(self, player: Player, from_: World) -> None:
        super().__init__(player)
        self.from_ = from_

    """
    Gets the world the player is switching from.

    @return: player's previous world
    """
    def getFrom(self) -> World:
        return self.from_

    def getHandlers(self) -> HandlerList:
        return self.handlers

    @staticmethod
    def getHandlerList() -> HandlerList:
        return PlayerChangedWorldEvent.handlers
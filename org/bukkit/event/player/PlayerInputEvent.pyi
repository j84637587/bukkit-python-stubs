from org.bukkit.Input import Input
from org.bukkit.entity.Player import Player
from org.bukkit.event.HandlerList import HandlerList
from org.bukkit.event.player.PlayerEvent import PlayerEvent
from typing import Any
from org.jetbrains.annotations import ApiStatus, NotNull

class PlayerInputEvent(PlayerEvent):
    """
    This event is called when a player sends updated input to the server.

    @see Player#getCurrentInput()
    """

    handlers: HandlerList = HandlerList()
    input: Input

    def __init__(self: "PlayerInputEvent", player: Player, input: Input) -> None:
        super().__init__(player)
        self.input = input

    """
    Gets the new input received from this player.

    @return the new input
    """
        def getInput(self: "PlayerInputEvent") -> Input:
        ...

        def getHandlers(self: "PlayerInputEvent") -> HandlerList:
        ...

        @staticmethod
    def getHandlerList() -> HandlerList:
        ...
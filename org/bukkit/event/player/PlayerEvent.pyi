from org.bukkit.entity import Player
from org.bukkit.event import Event
from typing import Any

class PlayerEvent(Event):
    """
    Represents a player related event
    """

    player: Player

    def __init__(self, who: Player) -> None:
        ...

    def __init__(self, who: Player, async: bool) -> None:
        ...

    """
    Returns the player involved in this event

    @return Player who is involved in this event
    """
    def get_player(self) -> Player:
        ...
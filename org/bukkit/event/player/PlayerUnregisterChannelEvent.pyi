from org.bukkit.entity import Player
from typing import Final

class PlayerUnregisterChannelEvent(PlayerChannelEvent):
    """
    This is called immediately after a player unregisters for a plugin channel.
    """

    def __init__(self, player: Player, channel: str) -> None:
        ...
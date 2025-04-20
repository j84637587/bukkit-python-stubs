from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import PlayerEvent
from typing import Final

class PlayerChannelEvent(PlayerEvent):
    """
    This event is called after a player registers or unregisters a new plugin
    channel.
    """
    
    handlers: Final[HandlerList] = HandlerList()
    channel: str

    def __init__(self, player: Player, channel: str) -> None:
        super().__init__(player)
        self.channel = channel

    def get_channel(self) -> str:
        """
        :return: The channel associated with this event.
        """
        return self.channel

    def get_handlers(self) -> HandlerList:
        """
        :return: The handler list for this event.
        """
        return self.handlers

    @staticmethod
    def get_handler_list() -> HandlerList:
        """
        :return: The static handler list for this event.
        """
        return PlayerChannelEvent.handlers
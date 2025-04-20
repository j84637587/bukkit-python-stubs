from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from typing import Optional

class PlayerJoinEvent(PlayerEvent):
    """
    Called when a player joins a server
    """

    handlers: HandlerList = HandlerList()
    join_message: Optional[str]

    def __init__(self, player_joined: Player, join_message: Optional[str]) -> None:
        super().__init__(player_joined)
        self.join_message = join_message

    """
    Gets the join message to send to all online players

    @return string join message. Can be null
    """
    def get_join_message(self) -> Optional[str]:
        ...

    """
    Sets the join message to send to all online players

    @param join_message join message. If null, no message will be sent
    """
    def set_join_message(self, join_message: Optional[str]) -> None:
        ...

    def get_handlers(self) -> HandlerList:
        ...

    @staticmethod
    def get_handler_list() -> HandlerList:
        ...
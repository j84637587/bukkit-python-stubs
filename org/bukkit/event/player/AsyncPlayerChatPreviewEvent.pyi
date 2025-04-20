from typing import Set
from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit import Warning

class AsyncPlayerChatEvent:
    def __init__(self, async: bool, who: Player, message: str, players: Set[Player]) -> None:
        ...

class AsyncPlayerChatPreviewEvent(AsyncPlayerChatEvent):
    """
    Used to format chat for chat preview. If this event is used, then the result
    of the corresponding AsyncPlayerChatEvent <b>must</b> be formatted in
    the same way.

    @deprecated chat previews have been removed
    """
    
    handlers: HandlerList

    def __init__(self, async: bool, who: Player, message: str, players: Set[Player]) -> None:
        super().__init__(async, who, message, players)

    def get_handlers(self) -> HandlerList:
        ...

    @staticmethod
    def get_handler_list() -> HandlerList:
        ...
from org.bukkit.entity import Player
from org.bukkit.event import Cancellable, HandlerList
from org.jetbrains.annotations import NotNull

class PlayerToggleSneakEvent(PlayerEvent, Cancellable):
    """
    Called when a player toggles their sneaking state
    """

    handlers: HandlerList = HandlerList()
    is_sneaking: bool
    cancel: bool = False

    def __init__(self, player: NotNull[Player], is_sneaking: bool) -> None:
        ...

    """
    Returns whether the player is now sneaking or not.

    @return: sneaking state
    """
    def is_sneaking(self) -> bool:
        ...

    def is_cancelled(self) -> bool:
        ...

    def set_cancelled(self, cancel: bool) -> None:
        ...

        def get_handlers(self) -> HandlerList:
        ...

        @staticmethod
    def get_handler_list() -> HandlerList:
        ...
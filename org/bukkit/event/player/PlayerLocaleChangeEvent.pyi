from org.bukkit.entity import Player
from org.bukkit.event import HandlerList
from org.bukkit.event.player import PlayerEvent
from typing import Any

class PlayerLocaleChangeEvent(PlayerEvent):
    """
    Called when a player changes their locale in the client settings.
    """

    handlers: HandlerList = HandlerList()
    locale: str

    def __init__(self, who: Player, locale: str) -> None:
        super().__init__(who)
        self.locale = locale

    """
    @return the player's new locale
    @see Player#getLocale()
    """
    def get_locale(self) -> str:
        return self.locale

    def get_handlers(self) -> HandlerList:
        return self.handlers

    @classmethod
    def get_handler_list(cls) -> HandlerList:
        return cls.handlers
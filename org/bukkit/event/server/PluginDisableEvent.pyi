from org.bukkit.event import HandlerList
from org.bukkit.plugin import Plugin
from typing import Any

class PluginDisableEvent:
    """
    Called when a plugin is disabled.
    """

    handlers: HandlerList = HandlerList()

    def __init__(self, plugin: Plugin) -> None:
        ...

    def get_handlers(self) -> HandlerList:
        ...

    @staticmethod
    def get_handler_list() -> HandlerList:
        ...
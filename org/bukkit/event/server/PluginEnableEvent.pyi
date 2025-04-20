from org.bukkit.event import HandlerList
from org.bukkit.plugin import Plugin
from typing import Any

class PluginEnableEvent(PluginEvent):
    """
    Called when a plugin is enabled.
    """

    handlers: HandlerList = HandlerList()

    def __init__(self, plugin: Plugin) -> None:
        super().__init__(plugin)

    def get_handlers(self) -> HandlerList:
        return self.handlers

    @staticmethod
    def get_handler_list() -> HandlerList:
        return PluginEnableEvent.handlers
from org.bukkit.plugin import Plugin
from org.bukkit.event.server import ServerEvent
from typing import Any

class PluginEvent(ServerEvent):
    """
    Used for plugin enable and disable events
    """

    def __init__(self, plugin: Plugin) -> None:
        """
        Initializes the PluginEvent with the given plugin.

        :param plugin: The plugin involved in this event
        """
        ...

    def get_plugin(self) -> Plugin:
        """
        Gets the plugin involved in this event

        :return: Plugin for this event
        """
        ...
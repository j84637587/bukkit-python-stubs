from typing import List, Dict, Any
from org.bukkit import Bukkit
from org.bukkit.plugin import Plugin
from org.jetbrains.annotations import NotNull

class PluginCommandYamlParser:
    @staticmethod
        def parse(plugin: Plugin) -> List['Command']:
        """Parses the commands defined in the plugin's YAML description.

        Args:
            plugin (Plugin): The plugin to parse commands from.

        Returns:
            List[Command]: A list of parsed commands.
        """
        ...
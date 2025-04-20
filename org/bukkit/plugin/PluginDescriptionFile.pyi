from typing import List, Map, Optional, Set, Union
import re
from io import InputStream, Reader, Writer
from org.bukkit.command import Command
from org.bukkit.command import CommandExecutor
from org.bukkit.command import CommandSender
from org.bukkit.command import PluginCommand
from org.bukkit.command import TabCompleter
from org.bukkit.permissions import Permissible
from org.bukkit.permissions import Permission
from org.bukkit.permissions import PermissionDefault
from org.bukkit.plugin.java import JavaPlugin
from org.yaml.snakeyaml import DumperOptions
from org.yaml.snakeyaml import LoaderOptions
from org.yaml.snakeyaml import Yaml
from org.yaml.snakeyaml.constructor import AbstractConstruct
from org.yaml.snakeyaml.constructor import SafeConstructor
from org.yaml.snakeyaml.nodes import Node
from org.yaml.snakeyaml.nodes import Tag
from org.yaml.snakeyaml.representer import Representer

class PluginDescriptionFile:
    """
    This type is the runtime-container for the information in the plugin.yml.
    All plugins must have a respective plugin.yml. For plugins written in java
    using the standard plugin loader, this file must be in the root of the jar
    file.
    ...
    """

    VALID_NAME: re.Pattern
    YAML: ThreadLocal[Yaml]

    def __init__(self, stream: InputStream) -> None:
        """
        Initializes the PluginDescriptionFile from the specified input stream.

        :param stream: The input stream
        :raises InvalidDescriptionException: If the PluginDescriptionFile is invalid
        """
        ...

    def __init__(self, reader: Reader) -> None:
        """
        Loads a PluginDescriptionFile from the specified reader.

        :param reader: The reader
        :raises InvalidDescriptionException: If the PluginDescriptionFile is invalid
        """
        ...

    def __init__(self, plugin_name: str, plugin_version: str, main_class: str) -> None:
        """
        Creates a new PluginDescriptionFile with the given details.

        :param plugin_name: Name of this plugin
        :param plugin_version: Version of this plugin
        :param main_class: Full location of the main class of this plugin
        """
        ...

    def get_name(self) -> str:
        """
        Gives the name of the plugin. This name is a unique identifier for plugins.
        ...
        """
        ...

    def get_provides(self) -> List[str]:
        """
        Gives the list of other plugin APIs which this plugin provides.
        ...
        """
        ...

    def get_version(self) -> str:
        """
        Gives the version of the plugin.
        ...
        """
        ...

    def get_main(self) -> str:
        """
        Gives the fully qualified name of the main class for a plugin.
        ...
        """
        ...

    def get_description(self) -> Optional[str]:
        """
        Gives a human-friendly description of the functionality the plugin provides.
        ...
        """
        ...

    def get_load(self) -> 'PluginLoadOrder':
        """
        Gives the phase of server startup that the plugin should be loaded.
        ...
        """
        ...

    def get_authors(self) -> List[str]:
        """
        Gives the list of authors for the plugin.
        ...
        """
        ...

    def get_contributors(self) -> List[str]:
        """
        Gives the list of contributors for the plugin.
        ...
        """
        ...

    def get_website(self) -> Optional[str]:
        """
        Gives the plugin's or plugin's author's website.
        ...
        """
        ...

    def get_depend(self) -> List[str]:
        """
        Gives a list of other plugins that the plugin requires.
        ...
        """
        ...

    def get_soft_depend(self) -> List[str]:
        """
        Gives a list of other plugins that the plugin requires for full functionality.
        ...
        """
        ...

    def get_load_before(self) -> List[str]:
        """
        Gets the list of plugins that should consider this plugin a soft-dependency.
        ...
        """
        ...

    def get_prefix(self) -> Optional[str]:
        """
        Gives the token to prefix plugin-specific logging messages with.
        ...
        """
        ...

    def get_commands(self) -> Map[str, Map[str, Union[str, List[str]]]]:
        """
        Gives the map of command-name to command-properties.
        ...
        """
        ...

    def get_permissions(self) -> List[Permission]:
        """
        Gives the list of permissions the plugin will register at runtime.
        ...
        """
        ...

    def get_permission_default(self) -> PermissionDefault:
        """
        Gives the default state of permissions registered for the plugin.
        ...
        """
        ...

    def get_awareness(self) -> Set['PluginAwareness']:
        """
        Gives a set of every PluginAwareness for a plugin.
        ...
        """
        ...

    def get_full_name(self) -> str:
        """
        Returns the name of a plugin, including the version.
        ...
        """
        ...

    def get_api_version(self) -> Optional[str]:
        """
        Gives the API version which this plugin is designed to support.
        ...
        """
        ...

    def get_libraries(self) -> List[str]:
        """
        Gets the libraries this plugin requires.
        ...
        """
        ...

    def get_class_loader_of(self) -> Optional[str]:
        """
        @return: unused
        @deprecated: unused
        """
        ...

    def save(self, writer: Writer) -> None:
        """
        Saves this PluginDescriptionFile to the given writer.

        :param writer: Writer to output this file to
        """
        ...

    def load_map(self, map: Map) -> None:
        """
        Loads the plugin description from a map.
        
        :param map: The map containing the plugin description
        :raises InvalidDescriptionException: If the description is invalid
        """
        ...

    @staticmethod
    def make_plugin_name_list(map: Map, key: str) -> List[str]:
        """
        Creates a list of plugin names from the map.

        :param map: The map containing the plugin description
        :param key: The key to look for in the map
        :raises InvalidDescriptionException: If the key is of the wrong type
        """
        ...

    def save_map(self) -> Map[str, Union[str, List[str], Map[str, Map[str, Union[str, List[str]]]]]]:
        """
        Saves the plugin description to a map.
        """
        ...

    def as_map(self, object: object) -> Map:
        """
        Converts an object to a map.

        :param object: The object to convert
        :raises InvalidDescriptionException: If the object is not a map
        """
        ...

    def get_raw_name(self) -> str:
        """
        @return: internal use
        @apiNote: Internal use
        """
        ...
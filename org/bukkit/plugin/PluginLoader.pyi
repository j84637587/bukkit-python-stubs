from typing import Dict, Set, Pattern, Type, Any
from org.bukkit.event import Event, Listener
from org.bukkit.plugin import Plugin, PluginDescriptionFile, RegisteredListener
from org.bukkit.plugin import InvalidPluginException, UnknownDependencyException, InvalidDescriptionException

"""
Represents a plugin loader, which handles direct access to specific types
of plugins
"""
class PluginLoader:

    """
    Loads the plugin contained in the specified file

    @param file File to attempt to load
    @return Plugin that was contained in the specified file, or None if
        unsuccessful
    @raises InvalidPluginException Thrown when the specified file is not a
        plugin
    @raises UnknownDependencyException If a required dependency could not
        be found
    """
    def load_plugin(self, file: File) -> Plugin:
        ...

    """
    Loads a PluginDescriptionFile from the specified file

    @param file File to attempt to load from
    @return A new PluginDescriptionFile loaded from the plugin.yml in the
        specified file
    @raises InvalidDescriptionException If the plugin description file
        could not be created
    """
    def get_plugin_description(self, file: File) -> PluginDescriptionFile:
        ...

    """
    Returns a list of all filename filters expected by this PluginLoader

    @return The filters
    """
    def get_plugin_file_filters(self) -> List[Pattern]:
        ...

    """
    Creates and returns registered listeners for the event classes used in
    this listener

    @param listener The object that will handle the eventual call back
    @param plugin The plugin to use when creating registered listeners
    @return The registered listeners.
    """
    def create_registered_listeners(self, listener: Listener, plugin: Plugin) -> Dict[Type[Event], Set[RegisteredListener]]:
        ...

    """
    Enables the specified plugin
    <p>
    Attempting to enable a plugin that is already enabled will have no
    effect

    @param plugin Plugin to enable
    """
    def enable_plugin(self, plugin: Plugin) -> None:
        ...

    """
    Disables the specified plugin
    <p>
    Attempting to disable a plugin that is not enabled will have no effect

    @param plugin Plugin to disable
    """
    def disable_plugin(self, plugin: Plugin) -> None:
        ...
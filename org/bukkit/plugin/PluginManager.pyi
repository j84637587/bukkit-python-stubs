from typing import Set, Optional, Type
from java.io import File
from org.bukkit.event import Event
from org.bukkit.event import EventPriority
from org.bukkit.event import Listener
from org.bukkit.permissions import Permissible
from org.bukkit.permissions import Permission
from org.bukkit.plugin import Plugin
from org.bukkit.plugin import PluginLoader
from org.bukkit.plugin import InvalidPluginException
from org.bukkit.plugin import InvalidDescriptionException
from org.bukkit.plugin import UnknownDependencyException

"""
Handles all plugin management from the Server
"""
class PluginManager:

    """
    Registers the specified plugin loader

    @param loader Class name of the PluginLoader to register
    @raises IllegalArgumentException Thrown when the given Class is not a
        valid PluginLoader
    """
    def register_interface(self, loader: Type[PluginLoader]) -> None:
        ...

    """
    Checks if the given plugin is loaded and returns it when applicable
    Please note that the name of the plugin is case-sensitive

    @param name Name of the plugin to check
    @return Plugin if it exists, otherwise None
    """
    def get_plugin(self, name: str) -> Optional[Plugin]:
        ...

    """
    Gets a list of all currently loaded plugins

    @return Array of Plugins
    """
    def get_plugins(self) -> list[Plugin]:
        ...

    """
    Checks if the given plugin is enabled or not
    Please note that the name of the plugin is case-sensitive.

    @param name Name of the plugin to check
    @return True if the plugin is enabled, otherwise False
    """
    def is_plugin_enabled(self, name: str) -> bool:
        ...

    """
    Checks if the given plugin is enabled or not

    @param plugin Plugin to check
    @return True if the plugin is enabled, otherwise False
    """
    def is_plugin_enabled(self, plugin: Optional[Plugin]) -> bool:
        ...

    """
    Loads the plugin in the specified file
    File must be valid according to the current enabled Plugin interfaces

    @param file File containing the plugin to load
    @return The Plugin loaded, or None if it was invalid
    @raises InvalidPluginException Thrown when the specified file is not a
        valid plugin
    @raises InvalidDescriptionException Thrown when the specified file
        contains an invalid description
    @raises UnknownDependencyException If a required dependency could not
        be resolved
    """
    def load_plugin(self, file: File) -> Optional[Plugin]:
        ...

    """
    Loads the plugins contained within the specified directory

    @param directory Directory to check for plugins
    @return A list of all plugins loaded
    """
    def load_plugins(self, directory: File) -> list[Plugin]:
        ...

    """
    Loads the plugins in the list of the files

    @param files List of files containing plugins to load
    @return A list of all plugins loaded
    """
    def load_plugins(self, files: list[File]) -> list[Plugin]:
        ...

    """
    Disables all the loaded plugins
    """
    def disable_plugins(self) -> None:
        ...

    """
    Disables and removes all plugins
    """
    def clear_plugins(self) -> None:
        ...

    """
    Calls an event with the given details

    @param event Event details
    @raises IllegalStateException Thrown when an asynchronous event is
        fired from synchronous code.
        Note: This is best-effort basis, and should not be used to test
        synchronized state. This is an indicator for flawed flow logic.
    """
    def call_event(self, event: Event) -> None:
        ...

    """
    Registers all the events in the given listener class

    @param listener Listener to register
    @param plugin Plugin to register
    """
    def register_events(self, listener: Listener, plugin: Plugin) -> None:
        ...

    """
    Registers the specified executor to the given event class

    @param event Event type to register
    @param listener Listener to register
    @param priority Priority to register this event at
    @param executor EventExecutor to register
    @param plugin Plugin to register
    """
    def register_event(self, event: Type[Event], listener: Listener, priority: EventPriority, executor: 'EventExecutor', plugin: Plugin) -> None:
        ...

    """
    Registers the specified executor to the given event class

    @param event Event type to register
    @param listener Listener to register
    @param priority Priority to register this event at
    @param executor EventExecutor to register
    @param plugin Plugin to register
    @param ignoreCancelled Whether to pass cancelled events or not
    """
    def register_event(self, event: Type[Event], listener: Listener, priority: EventPriority, executor: 'EventExecutor', plugin: Plugin, ignoreCancelled: bool) -> None:
        ...

    """
    Enables the specified plugin
    Attempting to enable a plugin that is already enabled will have no
    effect

    @param plugin Plugin to enable
    """
    def enable_plugin(self, plugin: Plugin) -> None:
        ...

    """
    Disables the specified plugin
    Attempting to disable a plugin that is not enabled will have no effect

    @param plugin Plugin to disable
    """
    def disable_plugin(self, plugin: Plugin) -> None:
        ...

    """
    Gets a Permission from its fully qualified name

    @param name Name of the permission
    @return Permission, or None if none
    """
    def get_permission(self, name: str) -> Optional[Permission]:
        ...

    """
    Adds a Permission to this plugin manager.
    If a permission is already defined with the given name of the new
    permission, an exception will be thrown.

    @param perm Permission to add
    @raises IllegalArgumentException Thrown when a permission with the same
        name already exists
    """
    def add_permission(self, perm: Permission) -> None:
        ...

    """
    Removes a Permission registration from this plugin manager.
    If the specified permission does not exist in this plugin manager,
    nothing will happen.
    Removing a permission registration will not remove the
    permission from any Permissibles that have it.

    @param perm Permission to remove
    """
    def remove_permission(self, perm: Permission) -> None:
        ...

    """
    Removes a Permission registration from this plugin manager.
    If the specified permission does not exist in this plugin manager,
    nothing will happen.
    Removing a permission registration will not remove the
    permission from any Permissibles that have it.

    @param name Permission to remove
    """
    def remove_permission(self, name: str) -> None:
        ...

    """
    Gets the default permissions for the given op status

    @param op Which set of default permissions to get
    @return The default permissions
    """
    def get_default_permissions(self, op: bool) -> Set[Permission]:
        ...

    """
    Recalculates the defaults for the given Permission.
    This will have no effect if the specified permission is not registered
    here.

    @param perm Permission to recalculate
    """
    def recalculate_permission_defaults(self, perm: Permission) -> None:
        ...

    """
    Subscribes the given Permissible for information about the requested
    Permission, by name.
    If the specified Permission changes in any form, the Permissible will
    be asked to recalculate.

    @param permission Permission to subscribe to
    @param permissible Permissible subscribing
    """
    def subscribe_to_permission(self, permission: str, permissible: Permissible) -> None:
        ...

    """
    Unsubscribes the given Permissible for information about the requested
    Permission, by name.

    @param permission Permission to unsubscribe from
    @param permissible Permissible subscribing
    """
    def unsubscribe_from_permission(self, permission: str, permissible: Permissible) -> None:
        ...

    """
    Gets a set containing all subscribed Permissibles to the given
    permission, by name

    @param permission Permission to query for
    @return Set containing all subscribed permissions
    """
    def get_permission_subscriptions(self, permission: str) -> Set[Permissible]:
        ...

    """
    Subscribes to the given Default permissions by operator status
    If the specified defaults change in any form, the Permissible will
    be asked to recalculate.

    @param op Default list to subscribe to
    @param permissible Permissible subscribing
    """
    def subscribe_to_default_perms(self, op: bool, permissible: Permissible) -> None:
        ...

    """
    Unsubscribes from the given Default permissions by operator status

    @param op Default list to unsubscribe from
    @param permissible Permissible subscribing
    """
    def unsubscribe_from_default_perms(self, op: bool, permissible: Permissible) -> None:
        ...

    """
    Gets a set containing all subscribed Permissibles to the given
    default list, by op status

    @param op Default list to query for
    @return Set containing all subscribed permissions
    """
    def get_default_perm_subscriptions(self, op: bool) -> Set[Permissible]:
        ...

    """
    Gets a set of all registered permissions.
    This set is a copy and will not be modified live.

    @return Set containing all current registered permissions
    """
    def get_permissions(self) -> Set[Permission]:
        ...

    """
    Returns whether or not timing code should be used for event calls

    @return True if event timings are to be used
    """
    def use_timings(self) -> bool:
        ...
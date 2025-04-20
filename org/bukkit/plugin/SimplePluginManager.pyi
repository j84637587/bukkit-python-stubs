from typing import List, Dict, Set, Collection, Optional, Pattern
from java.io import File
from java.lang.reflect import Constructor, Method
from java.util import ArrayList, HashMap, HashSet, LinkedHashMap, LinkedHashSet, LinkedList, Map, Set, Iterator
from java.util.logging import Level
from org.bukkit import Server, World
from org.bukkit.command import Command, PluginCommandYamlParser, SimpleCommandMap
from org.bukkit.event import Event, EventPriority, HandlerList, Listener
from org.bukkit.permissions import Permissible, Permission, PermissionDefault
from org.bukkit.util import FileUtil
from org.jetbrains.annotations import NotNull, Nullable

class SimplePluginManager(PluginManager):
    """
    Handles all plugin management from the Server
    """

    def __init__(self: 'SimplePluginManager', instance: Server, command_map: SimpleCommandMap) -> None:
        """
        Initializes the SimplePluginManager with the specified server instance and command map.

        :param instance: The server instance.
        :param command_map: The command map.
        """
        ...

    def registerInterface(self: 'SimplePluginManager', loader: Type[PluginLoader]) -> None:
        """
        Registers the specified plugin loader.

        :param loader: Class name of the PluginLoader to register.
        :raises IllegalArgumentException: Thrown when the given Class is not a valid PluginLoader.
        """
        ...

    def loadPlugins(self: 'SimplePluginManager', directory: File) -> List[Plugin]:
        """
        Loads the plugins contained within the specified directory.

        :param directory: Directory to check for plugins.
        :return: A list of all plugins loaded.
        """
        ...

    def loadPlugins(self: 'SimplePluginManager', files: List[File]) -> List[Plugin]:
        """
        Loads the plugins in the list of the files.

        :param files: List of files containing plugins to load.
        :return: A list of all plugins loaded.
        """
        ...

    def loadPlugin(self: 'SimplePluginManager', file: File) -> Optional[Plugin]:
        """
        Loads the plugin in the specified file.

        :param file: File containing the plugin to load.
        :return: The Plugin loaded, or None if it was invalid.
        :raises InvalidPluginException: Thrown when the specified file is not a valid plugin.
        :raises UnknownDependencyException: If a required dependency could not be found.
        """
        ...

    def getPlugin(self: 'SimplePluginManager', name: str) -> Optional[Plugin]:
        """
        Checks if the given plugin is loaded and returns it when applicable.

        :param name: Name of the plugin to check.
        :return: Plugin if it exists, otherwise None.
        """
        ...

    def getPlugins(self: 'SimplePluginManager') -> List[Plugin]:
        """
        Returns all loaded plugins.

        :return: An array of loaded plugins.
        """
        ...

    def isPluginEnabled(self: 'SimplePluginManager', name: str) -> bool:
        """
        Checks if the given plugin is enabled or not.

        :param name: Name of the plugin to check.
        :return: True if the plugin is enabled, otherwise False.
        """
        ...

    def enablePlugin(self: 'SimplePluginManager', plugin: Plugin) -> None:
        """
        Enables the specified plugin.

        :param plugin: The plugin to enable.
        """
        ...

    def disablePlugins(self: 'SimplePluginManager') -> None:
        """
        Disables all loaded plugins.
        """
        ...

    def disablePlugin(self: 'SimplePluginManager', plugin: Plugin) -> None:
        """
        Disables the specified plugin.

        :param plugin: The plugin to disable.
        """
        ...

    def clearPlugins(self: 'SimplePluginManager') -> None:
        """
        Clears all loaded plugins.
        """
        ...

    def callEvent(self: 'SimplePluginManager', event: Event) -> None:
        """
        Calls an event with the given details.

        :param event: Event details.
        """
        ...

    def registerEvents(self: 'SimplePluginManager', listener: Listener, plugin: Plugin) -> None:
        """
        Registers the specified listener for events.

        :param listener: The listener to register.
        :param plugin: The plugin registering the listener.
        """
        ...

    def registerEvent(self: 'SimplePluginManager', event: Type[Event], listener: Listener, priority: EventPriority, executor: EventExecutor, plugin: Plugin, ignoreCancelled: bool = False) -> None:
        """
        Registers the given event to the specified listener using a directly passed EventExecutor.

        :param event: Event class to register.
        :param listener: Listener to register.
        :param priority: Priority of this event.
        :param executor: EventExecutor to register.
        :param plugin: Plugin to register.
        :param ignoreCancelled: Do not call executor if event was already cancelled.
        """
        ...

    def getPermission(self: 'SimplePluginManager', name: str) -> Optional[Permission]:
        """
        Gets the permission with the specified name.

        :param name: The name of the permission.
        :return: The permission if it exists, otherwise None.
        """
        ...

    def addPermission(self: 'SimplePluginManager', perm: Permission) -> None:
        """
        Adds a permission.

        :param perm: The permission to add.
        """
        ...

    def removePermission(self: 'SimplePluginManager', name: str) -> None:
        """
        Removes a permission.

        :param name: The name of the permission to remove.
        """
        ...

    def getDefaultPermissions(self: 'SimplePluginManager', op: bool) -> Set[Permission]:
        """
        Gets the default permissions for the specified operation level.

        :param op: True for operator permissions, False for non-operator permissions.
        :return: A set of default permissions.
        """
        ...

    def subscribeToPermission(self: 'SimplePluginManager', permission: str, permissible: Permissible) -> None:
        """
        Subscribes a permissible to a permission.

        :param permission: The permission to subscribe to.
        :param permissible: The permissible to subscribe.
        """
        ...

    def unsubscribeFromPermission(self: 'SimplePluginManager', permission: str, permissible: Permissible) -> None:
        """
        Unsubscribes a permissible from a permission.

        :param permission: The permission to unsubscribe from.
        :param permissible: The permissible to unsubscribe.
        """
        ...

    def getPermissionSubscriptions(self: 'SimplePluginManager', permission: str) -> Set[Permissible]:
        """
        Gets the subscriptions for a permission.

        :param permission: The permission to check.
        :return: A set of permissible that are subscribed to the permission.
        """
        ...

    def useTimings(self: 'SimplePluginManager') -> bool:
        """
        Checks if per event timing code should be used.

        :return: True if per event timing code should be used, otherwise False.
        """
        ...

    def useTimings(self: 'SimplePluginManager', use: bool) -> None:
        """
        Sets whether or not per event timing code should be used.

        :param use: True if per event timing code should be used.
        """
        ...
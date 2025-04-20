from typing import List, Pattern, Map, Set, Collection, Callable, Any
from java.io import File, FileNotFoundException, IOException, InputStream
from java.lang.reflect import InvocationTargetException, Method
from java.util import Arrays, HashMap, HashSet, List as JavaList
from java.util.concurrent import CopyOnWriteArrayList
from java.util.jar import JarEntry, JarFile
from java.util.logging import Level
from java.util.regex import Pattern
from org.bukkit import Server, Warning, WarningState
from org.bukkit.configuration.serialization import ConfigurationSerializable, ConfigurationSerialization
from org.bukkit.event import Event, EventException, EventHandler, Listener
from org.bukkit.event.server import PluginDisableEvent, PluginEnableEvent
from org.bukkit.plugin import AuthorNagException, EventExecutor, InvalidDescriptionException, InvalidPluginException, Plugin, PluginDescriptionFile, PluginLoader, RegisteredListener, SimplePluginManager, TimedRegisteredListener, UnknownDependencyException
from org.jetbrains.annotations import NotNull, Nullable
from org.yaml.snakeyaml.error import YAMLException

class JavaPluginLoader(PluginLoader):
    """
    Represents a Java plugin loader, allowing plugins in the form of .jar
    """
    server: Server
    fileFilters: List[Pattern]
    loaders: List['PluginClassLoader']
    libraryLoader: 'LibraryLoader'

    def __init__(self, instance: Server) -> None:
        """
        This class was not meant to be constructed explicitly

        :param instance: the server instance
        """
        ...

    def loadPlugin(self, file: File) -> Plugin:
        """
        Load a plugin from the specified file.

        :param file: the file to load the plugin from
        :raises InvalidPluginException: if the plugin cannot be loaded
        :return: the loaded plugin
        """
        ...

    def getPluginDescription(self, file: File) -> PluginDescriptionFile:
        """
        Get the plugin description from the specified file.

        :param file: the file to get the plugin description from
        :raises InvalidDescriptionException: if the description cannot be read
        :return: the plugin description
        """
        ...

    def getPluginFileFilters(self) -> List[Pattern]:
        """
        Get the file filters for plugins.

        :return: the file filters
        """
        ...

    def getClassByName(self, name: str, resolve: bool, description: PluginDescriptionFile) -> Nullable[type]:
        """
        Get a class by its name.

        :param name: the name of the class
        :param resolve: whether to resolve the class
        :param description: the plugin description
        :return: the class, or None if not found
        """
        ...

    def setClass(self, name: str, clazz: type) -> None:
        """
        Set a class for serialization.

        :param name: the name of the class
        :param clazz: the class to set
        """
        ...

    def removeClass(self, clazz: type) -> None:
        """
        Remove a class from serialization.

        :param clazz: the class to remove
        """
        ...

    def createRegisteredListeners(self, listener: Listener, plugin: Plugin) -> Map[type, Set[RegisteredListener]]:
        """
        Create registered listeners for the specified listener and plugin.

        :param listener: the listener to register
        :param plugin: the plugin to register the listener for
        :return: a map of event classes to registered listeners
        """
        ...

    def enablePlugin(self, plugin: Plugin) -> None:
        """
        Enable the specified plugin.

        :param plugin: the plugin to enable
        """
        ...

    def disablePlugin(self, plugin: Plugin) -> None:
        """
        Disable the specified plugin.

        :param plugin: the plugin to disable
        """
        ...
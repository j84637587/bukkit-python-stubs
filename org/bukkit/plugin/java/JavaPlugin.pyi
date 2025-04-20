from typing import List, Optional
from java.io import File, FileOutputStream, IOException, InputStream, InputStreamReader, OutputStream, Reader
from java.net import URL, URLConnection
from java.util import Locale
from java.util.logging import Level, Logger
from org.bukkit import Server
from org.bukkit.command import Command, CommandSender, PluginCommand
from org.bukkit.configuration.file import FileConfiguration, YamlConfiguration
from org.bukkit.generator import BiomeProvider, ChunkGenerator
from org.bukkit.plugin import PluginBase, PluginDescriptionFile, PluginLoader, PluginLogger
from org.jetbrains.annotations import NotNull, Nullable

"""
Represents a Java plugin and its main class. It contains fundamental methods
and fields for a plugin to be loaded and work properly. This is an indirect
implementation of {@link org.bukkit.plugin.Plugin}.
"""
class JavaPlugin(PluginBase):
    def __init__(self) -> None:
        """
        Initializes the JavaPlugin.
        """
        ...

    def __init__(self, loader: NotNull, description: NotNull, dataFolder: NotNull, file: NotNull) -> None:
        """
        Initializes the JavaPlugin with the specified loader, description, data folder, and file.
        """
        ...

        def getDataFolder(self) -> File:
        """
        Returns the folder that the plugin data's files are located in. The
        folder may not yet exist.

        @return The folder.
        """
        ...

        def getPluginLoader(self) -> PluginLoader:
        """
        Gets the associated PluginLoader responsible for this plugin

        @return PluginLoader that controls this plugin
        """
        ...

        def getServer(self) -> Server:
        """
        Returns the Server instance currently running this plugin

        @return Server running this plugin
        """
        ...

    def isEnabled(self) -> bool:
        """
        Returns a value indicating whether or not this plugin is currently
        enabled

        @return true if this plugin is enabled, otherwise false
        """
        ...

        def getFile(self) -> File:
        """
        Returns the file which contains this plugin

        @return File containing this plugin
        """
        ...

        def getDescription(self) -> PluginDescriptionFile:
        """
        Returns the plugin.yaml file containing the details for this plugin

        @return Contents of the plugin.yaml file
        """
        ...

        def getConfig(self) -> FileConfiguration:
        ...

        def getTextResource(self, file: NotNull[str]) -> Optional[Reader]:
        """
        Provides a reader for a text file located inside the jar.
        <p>
        The returned reader will read text with the UTF-8 charset.

        @param file the filename of the resource to load
        @return null if {@link #getResource(String)} returns null
        @throws IllegalArgumentException if file is null
        @see ClassLoader#getResourceAsStream(String)
        """
        ...

    def reloadConfig(self) -> None:
        ...

    def saveConfig(self) -> None:
        ...

    def saveDefaultConfig(self) -> None:
        ...

    def saveResource(self, resourcePath: NotNull[str], replace: bool) -> None:
        ...

        def getResource(self, filename: NotNull[str]) -> Optional[InputStream]:
        ...

        def getClassLoader(self) -> ClassLoader:
        """
        Returns the ClassLoader which holds this plugin

        @return ClassLoader holding this plugin
        """
        ...

    def setEnabled(self, enabled: bool) -> None:
        """
        Sets the enabled state of this plugin

        @param enabled true if enabled, otherwise false
        """
        ...

    def init(self, loader: NotNull[PluginLoader], server: NotNull[Server], description: NotNull[PluginDescriptionFile], dataFolder: NotNull[File], file: NotNull[File], classLoader: NotNull[ClassLoader]) -> None:
        ...

    def onCommand(self, sender: NotNull[CommandSender], command: NotNull[Command], label: NotNull[str], args: NotNull[list[str]]) -> bool:
        """
        {@inheritDoc}
        """
        ...

        def onTabComplete(self, sender: NotNull[CommandSender], command: NotNull[Command], alias: NotNull[str], args: NotNull[list[str]]) -> Optional[List[str]]:
        """
        {@inheritDoc}
        """
        ...

        def getCommand(self, name: NotNull[str]) -> Optional[PluginCommand]:
        """
        Gets the command with the given name, specific to this plugin. Commands
        need to be registered in the {@link PluginDescriptionFile#getCommands()
        PluginDescriptionFile} to exist at runtime.

        @param name name or alias of the command
        @return the plugin command if found, otherwise null
        """
        ...

    def onLoad(self) -> None:
        ...

    def onDisable(self) -> None:
        ...

    def onEnable(self) -> None:
        ...

        def getDefaultWorldGenerator(self, worldName: NotNull[str], id: Optional[str]) -> Optional[ChunkGenerator]:
        ...

        def getDefaultBiomeProvider(self, worldName: NotNull[str], id: Optional[str]) -> Optional[BiomeProvider]:
        ...

    def isNaggable(self) -> bool:
        ...

    def setNaggable(self, canNag: bool) -> None:
        ...

        def getLogger(self) -> Logger:
        ...

        def __str__(self) -> str:
        ...

        @staticmethod
    def getPlugin(clazz: NotNull[Class[T]]) -> T:
        """
        This method provides fast access to the plugin that has {@link
        #getProvidingPlugin(Class) provided} the given plugin class, which is
        usually the plugin that implemented it.
        <p>
        An exception to this would be if plugin's jar that contained the class
        does not extend the class, where the intended plugin would have
        resided in a different jar / classloader.

        @param <T> a class that extends JavaPlugin
        @param clazz the class desired
        @return the plugin that provides and implements said class
        @throws IllegalArgumentException if clazz is null
        @throws IllegalArgumentException if clazz does not extend {@link
            JavaPlugin}
        @throws IllegalStateException if clazz was not provided by a plugin,
            for example, if called with
            <code>JavaPlugin.getPlugin(JavaPlugin.class)</code>
        @throws IllegalStateException if called from the static initializer for
            given JavaPlugin
        @throws ClassCastException if plugin that provided the class does not
            extend the class
        """
        ...

        @staticmethod
    def getProvidingPlugin(clazz: NotNull[Class]) -> JavaPlugin:
        """
        This method provides fast access to the plugin that has provided the
        given class.

        @param clazz a class belonging to a plugin
        @return the plugin that provided the class
        @throws IllegalArgumentException if the class is not provided by a
            JavaPlugin
        @throws IllegalArgumentException if class is null
        @throws IllegalStateException if called from the static initializer for
            given JavaPlugin
        """
        ...
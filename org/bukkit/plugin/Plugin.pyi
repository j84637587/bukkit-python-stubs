from typing import Optional
from pathlib import Path
from io import BytesIO
import logging
from org.bukkit import Server
from org.bukkit.command import TabExecutor
from org.bukkit.configuration.file import FileConfiguration
from org.bukkit.generator import BiomeProvider, ChunkGenerator

class Plugin(TabExecutor):
    """
    Represents a Plugin
    <p>
    The use of {@link PluginBase} is recommended for actual Implementation
    """

    def get_data_folder(self) -> Path:
        """
        Returns the folder that the plugin data's files are located in. The
        folder may not yet exist.

        @return The folder
        """
        ...

    def get_description(self) -> 'PluginDescriptionFile':
        """
        Returns the plugin.yaml file containing the details for this plugin

        @return Contents of the plugin.yaml file
        """
        ...

    def get_config(self) -> FileConfiguration:
        """
        Gets a {@link FileConfiguration} for this plugin, read through
        "config.yml"
        <p>
        If there is a default config.yml embedded in this plugin, it will be
        provided as a default for this Configuration.

        @return Plugin configuration
        """
        ...

    def get_resource(self, filename: str) -> Optional[BytesIO]:
        """
        Gets an embedded resource in this plugin

        @param filename Filename of the resource
        @return File if found, otherwise null
        """
        ...

    def save_config(self) -> None:
        """
        Saves the {@link FileConfiguration} retrievable by {@link #getConfig()}.
        """
        ...

    def save_default_config(self) -> None:
        """
        Saves the raw contents of the default config.yml file to the location
        retrievable by {@link #getConfig()}.
        <p>
        This should fail silently if the config.yml already exists.
        """
        ...

    def save_resource(self, resource_path: str, replace: bool) -> None:
        """
        Saves the raw contents of any resource embedded with a plugin's .jar
        file assuming it can be found using {@link #getResource(String)}.
        <p>
        The resource is saved into the plugin's data folder using the same
        hierarchy as the .jar file (subdirectories are preserved).

        @param resourcePath the embedded resource path to look for within the
            plugin's .jar file. (No preceding slash).
        @param replace if true, the embedded resource will overwrite the
            contents of an existing file.
        @throws IllegalArgumentException if the resource path is null, empty,
            or points to a nonexistent resource.
        """
        ...

    def reload_config(self) -> None:
        """
        Discards any data in {@link #getConfig()} and reloads from disk.
        """
        ...

    def get_plugin_loader(self) -> 'PluginLoader':
        """
        Gets the associated PluginLoader responsible for this plugin

        @return PluginLoader that controls this plugin
        """
        ...

    def get_server(self) -> Server:
        """
        Returns the Server instance currently running this plugin

        @return Server running this plugin
        """
        ...

    def is_enabled(self) -> bool:
        """
        Returns a value indicating whether or not this plugin is currently
        enabled

        @return true if this plugin is enabled, otherwise false
        """
        ...

    def on_disable(self) -> None:
        """
        Called when this plugin is disabled
        """
        ...

    def on_load(self) -> None:
        """
        Called after a plugin is loaded but before it has been enabled.
        <p>
        When multiple plugins are loaded, the onLoad() for all plugins is
        called before any onEnable() is called.
        """
        ...

    def on_enable(self) -> None:
        """
        Called when this plugin is enabled
        """
        ...

    def is_naggable(self) -> bool:
        """
        Simple boolean if we can still nag to the logs about things

        @return boolean whether we can nag
        """
        ...

    def set_naggable(self, can_nag: bool) -> None:
        """
        Set naggable state

        @param canNag is this plugin still naggable?
        """
        ...

    def get_default_world_generator(self, world_name: str, id: Optional[str]) -> Optional[ChunkGenerator]:
        """
        Gets a {@link ChunkGenerator} for use in a default world, as specified
        in the server configuration

        @param worldName Name of the world that this will be applied to
        @param id Unique ID, if any, that was specified to indicate which
            generator was requested
        @return ChunkGenerator for use in the default world generation
        """
        ...

    def get_default_biome_provider(self, world_name: str, id: Optional[str]) -> Optional[BiomeProvider]:
        """
        Gets a {@link BiomeProvider} for use in a default world, as specified
        in the server configuration

        @param worldName Name of the world that this will be applied to
        @param id Unique ID, if any, that was specified to indicate which
            biome provider was requested
        @return BiomeProvider for use in the default world generation
        """
        ...

    def get_logger(self) -> logging.Logger:
        """
        Returns the plugin logger associated with this server's logger. The
        returned logger automatically tags all log messages with the plugin's
        name.

        @return Logger associated with this plugin
        """
        ...

    def get_name(self) -> str:
        """
        Returns the name of the plugin.
        <p>
        This should return the bare name of the plugin and should be used for
        comparison.

        @return name of the plugin
        """
        ...
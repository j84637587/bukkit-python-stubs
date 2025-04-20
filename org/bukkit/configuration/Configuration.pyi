from typing import Dict, Optional
from org.bukkit.configuration import ConfigurationSection
from org.jetbrains.annotations import NotNull, Nullable

"""
Represents a source of configurable options and settings
"""
class Configuration(ConfigurationSection):
    """
    Sets the default value of the given path as provided.
    <p>
    If no source {@link Configuration} was provided as a default
    collection, then a new {@link MemoryConfiguration} will be created to
    hold the new default value.
    <p>
    If value is null, the value will be removed from the default
    Configuration source.
    
    @param path Path of the value to set.
    @param value Value to set the default to.
    @raises IllegalArgumentException Thrown if path is null.
    """
    def add_default(self: "Configuration", path: str, value: Optional[object]) -> None: ...

    """
    Sets the default values of the given paths as provided.
    <p>
    If no source {@link Configuration} was provided as a default
    collection, then a new {@link MemoryConfiguration} will be created to
    hold the new default values.
    
    @param defaults A map of Path{@literal ->}Values to add to defaults.
    @raises IllegalArgumentException Thrown if defaults is null.
    """
    def add_defaults(self: "Configuration", defaults: Dict[str, object]) -> None: ...

    """
    Sets the default values of the given paths as provided.
    <p>
    If no source {@link Configuration} was provided as a default
    collection, then a new {@link MemoryConfiguration} will be created to
    hold the new default value.
    <p>
    This method will not hold a reference to the specified Configuration,
    nor will it automatically update if that Configuration ever changes. If
    you require this, you should set the default source with {@link
    #setDefaults(org.bukkit.configuration.Configuration)}.
    
    @param defaults A configuration holding a list of defaults to copy.
    @raises IllegalArgumentException Thrown if defaults is null or this.
    """
    def add_defaults(self: "Configuration", defaults: "Configuration") -> None: ...

    """
    Sets the source of all default values for this {@link Configuration}.
    <p>
    If a previous source was set, or previous default values were defined,
    then they will not be copied to the new source.
    
    @param defaults New source of default values for this configuration.
    @raises IllegalArgumentException Thrown if defaults is null or this.
    """
    def set_defaults(self: "Configuration", defaults: "Configuration") -> None: ...

    """
    Gets the source {@link Configuration} for this configuration.
    <p>
    If no configuration source was set, but default values were added, then
    a {@link MemoryConfiguration} will be returned. If no source was set
    and no defaults were set, then this method will return null.
    
    @return Configuration source for default values, or null if none exist.
    """
    def get_defaults(self: "Configuration") -> Optional["Configuration"]: ...

    """
    Gets the {@link ConfigurationOptions} for this {@link Configuration}.
    <p>
    All setters through this method are chainable.
    
    @return Options for this configuration
    """
    def options(self: "Configuration") -> "ConfigurationOptions": ...
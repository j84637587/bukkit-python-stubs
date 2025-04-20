from typing import Dict, Optional
from org.bukkit.configuration import Configuration, MemorySection, ConfigurationSection, MemoryConfigurationOptions
from com.google.common.base import Preconditions

"""
This is a {@link Configuration} implementation that does not save or load
from any source, and stores all values in memory only.
This is useful for temporary Configurations for providing defaults.
"""
class MemoryConfiguration(MemorySection, Configuration):
    defaults: Optional[Configuration]
    options: Optional[MemoryConfigurationOptions]

    """
    Creates an empty {@link MemoryConfiguration} with no default values.
    """
    def __init__(self) -> None: ...

    """
    Creates an empty {@link MemoryConfiguration} using the specified {@link
    Configuration} as a source for all default values.

    @param defaults Default value provider
    @raises IllegalArgumentException Thrown if defaults is null
    """
    def __init__(self, defaults: Optional[Configuration]) -> None: ...

    def add_default(self, path: str, value: Optional[object]) -> None: ...

    def add_defaults(self, defaults: Dict[str, object]) -> None: ...

    def add_defaults(self, defaults: Configuration) -> None: ...

    def set_defaults(self, defaults: Configuration) -> None: ...

    def get_defaults(self) -> Optional[Configuration]: ...

    def get_parent(self) -> Optional[ConfigurationSection]: ...

    def options(self) -> MemoryConfigurationOptions: ...
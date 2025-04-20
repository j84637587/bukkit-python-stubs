from org.bukkit.configuration import ConfigurationOptions
from org.jetbrains.annotations import NotNull

class MemoryConfigurationOptions(ConfigurationOptions):
    """
    Various settings for controlling the input and output of a {@link
    MemoryConfiguration}
    """

    def __init__(self, configuration: NotNull['MemoryConfiguration']) -> None:
        ...

        def configuration(self) -> 'MemoryConfiguration':
        ...

        def copy_defaults(self, value: bool) -> 'MemoryConfigurationOptions':
        ...

        def path_separator(self, value: str) -> 'MemoryConfigurationOptions':
        ...
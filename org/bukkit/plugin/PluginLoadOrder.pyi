from enum import Enum

class PluginLoadOrder(Enum):
    """Represents the order in which a plugin should be initialized and enabled"""

    STARTUP = ...  # Indicates that the plugin will be loaded at startup
    POSTWORLD = ...  # Indicates that the plugin will be loaded after the first/default world was created
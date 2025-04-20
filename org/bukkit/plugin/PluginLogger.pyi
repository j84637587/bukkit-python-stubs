from typing import Any
from logging import Logger, LogRecord, Level
from org.bukkit.plugin import Plugin

class PluginLogger(Logger):
    """
    The PluginLogger class is a modified Logger that prepends all
    logging calls with the name of the plugin doing the logging. The API for
    PluginLogger is exactly the same as Logger.

    @see Logger
    """

    def __init__(self, context: Plugin) -> None:
        """
        Creates a new PluginLogger that extracts the name from a plugin.

        @param context: A reference to the plugin
        """
        ...

    def log(self, logRecord: LogRecord) -> None:
        ...
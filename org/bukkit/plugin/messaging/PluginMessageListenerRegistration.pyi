from org.bukkit.plugin import Plugin
from org.bukkit.plugin.messaging import Messenger, PluginMessageListener
from typing import Any

class PluginMessageListenerRegistration:
    """
    Contains information about a {@link Plugin}s registration to a plugin
    channel.
    """

    def __init__(self, messenger: Messenger, plugin: Plugin, channel: str, listener: PluginMessageListener) -> None:
        """
        Initializes a new PluginMessageListenerRegistration.

        :param messenger: The messenger associated with this registration.
        :param plugin: The plugin associated with this registration.
        :param channel: The channel associated with this registration.
        :param listener: The listener associated with this registration.
        :raises ValueError: If any of the parameters are None.
        """
        ...

    def get_channel(self) -> str:
        """
        Gets the plugin channel that this registration is about.

        :return: Plugin channel.
        """
        ...

    def get_listener(self) -> PluginMessageListener:
        """
        Gets the registered listener described by this registration.

        :return: Registered listener.
        """
        ...

    def get_plugin(self) -> Plugin:
        """
        Gets the plugin that this registration is for.

        :return: Registered plugin.
        """
        ...

    def is_valid(self) -> bool:
        """
        Checks if this registration is still valid.

        :return: True if this registration is still valid, otherwise false.
        """
        ...

    def __eq__(self, obj: Any) -> bool:
        """
        Checks if this registration is equal to another object.

        :param obj: The object to compare.
        :return: True if equal, otherwise false.
        """
        ...

    def __hash__(self) -> int:
        """
        Returns the hash code for this registration.

        :return: Hash code.
        """
        ...
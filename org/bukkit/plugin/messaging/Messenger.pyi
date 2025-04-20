from typing import Set
from org.bukkit import NamespacedKey
from org.bukkit.entity import Player
from org.bukkit.plugin import Plugin
from org.jetbrains.annotations import NotNull

class Messenger:
    """
    A class responsible for managing the registrations of plugin channels and
    their listeners.

    Channel names must contain a colon separator and consist of only [a-z0-9/._-]
    - i.e. they MUST be valid {@link NamespacedKey}. The "BungeeCord" channel is
    an exception and may only take this form.
    """

    MAX_MESSAGE_SIZE: int = 1048576
    MAX_CHANNEL_SIZE: int = 64

    def is_reserved_channel(self, channel: str) -> bool:
        """
        Checks if the specified channel is a reserved name.
        <br>
        All channels within the "minecraft" namespace except for
        "minecraft:brand" are reserved.

        :param channel: Channel name to check.
        :return: True if the channel is reserved, otherwise false.
        :raises IllegalArgumentException: Thrown if channel is null.
        """
        ...

    def register_outgoing_plugin_channel(self, plugin: Plugin, channel: str) -> None:
        """
        Registers the specific plugin to the requested outgoing plugin channel,
        allowing it to send messages through that channel to any clients.

        :param plugin: Plugin that wishes to send messages through the channel.
        :param channel: Channel to register.
        :raises IllegalArgumentException: Thrown if plugin or channel is null.
        """
        ...

    def unregister_outgoing_plugin_channel(self, plugin: Plugin, channel: str) -> None:
        """
        Unregisters the specific plugin from the requested outgoing plugin
        channel, no longer allowing it to send messages through that channel to
        any clients.

        :param plugin: Plugin that no longer wishes to send messages through the
            channel.
        :param channel: Channel to unregister.
        :raises IllegalArgumentException: Thrown if plugin or channel is null.
        """
        ...

    def unregister_outgoing_plugin_channel(self, plugin: Plugin) -> None:
        """
        Unregisters the specific plugin from all outgoing plugin channels, no
        longer allowing it to send any plugin messages.

        :param plugin: Plugin that no longer wishes to send plugin messages.
        :raises IllegalArgumentException: Thrown if plugin is null.
        """
        ...

    def register_incoming_plugin_channel(self, plugin: Plugin, channel: str, listener: 'PluginMessageListener') -> NotNull:
        """
        Registers the specific plugin for listening on the requested incoming
        plugin channel, allowing it to act upon any plugin messages.

        :param plugin: Plugin that wishes to register to this channel.
        :param channel: Channel to register.
        :param listener: Listener to receive messages on.
        :return: The resulting registration that was made as a result of this
            method.
        :raises IllegalArgumentException: Thrown if plugin, channel or listener
            is null, or the listener is already registered for this channel.
        """
        ...

    def unregister_incoming_plugin_channel(self, plugin: Plugin, channel: str, listener: 'PluginMessageListener') -> None:
        """
        Unregisters the specific plugin's listener from listening on the
        requested incoming plugin channel, no longer allowing it to act upon
        any plugin messages.

        :param plugin: Plugin that wishes to unregister from this channel.
        :param channel: Channel to unregister.
        :param listener: Listener to stop receiving messages on.
        :raises IllegalArgumentException: Thrown if plugin, channel or listener
            is null.
        """
        ...

    def unregister_incoming_plugin_channel(self, plugin: Plugin, channel: str) -> None:
        """
        Unregisters the specific plugin from listening on the requested
        incoming plugin channel, no longer allowing it to act upon any plugin
        messages.

        :param plugin: Plugin that wishes to unregister from this channel.
        :param channel: Channel to unregister.
        :raises IllegalArgumentException: Thrown if plugin or channel is null.
        """
        ...

    def unregister_incoming_plugin_channel(self, plugin: Plugin) -> None:
        """
        Unregisters the specific plugin from listening on all plugin channels
        through all listeners.

        :param plugin: Plugin that wishes to unregister from this channel.
        :raises IllegalArgumentException: Thrown if plugin is null.
        """
        ...

    def get_outgoing_channels(self) -> NotNull[Set[str]]:
        """
        Gets a set containing all the outgoing plugin channels.

        :return: List of all registered outgoing plugin channels.
        """
        ...

    def get_outgoing_channels(self, plugin: Plugin) -> NotNull[Set[str]]:
        """
        Gets a set containing all the outgoing plugin channels that the
        specified plugin is registered to.

        :param plugin: Plugin to retrieve channels for.
        :return: List of all registered outgoing plugin channels that a plugin
            is registered to.
        :raises IllegalArgumentException: Thrown if plugin is null.
        """
        ...

    def get_incoming_channels(self) -> NotNull[Set[str]]:
        """
        Gets a set containing all the incoming plugin channels.

        :return: List of all registered incoming plugin channels.
        """
        ...

    def get_incoming_channels(self, plugin: Plugin) -> NotNull[Set[str]]:
        """
        Gets a set containing all the incoming plugin channels that the
        specified plugin is registered for.

        :param plugin: Plugin to retrieve channels for.
        :return: List of all registered incoming plugin channels that the plugin
            is registered for.
        :raises IllegalArgumentException: Thrown if plugin is null.
        """
        ...

    def get_incoming_channel_registrations(self, plugin: Plugin) -> NotNull[Set['PluginMessageListenerRegistration']]:
        """
        Gets a set containing all the incoming plugin channel registrations
        that the specified plugin has.

        :param plugin: Plugin to retrieve registrations for.
        :return: List of all registrations that the plugin has.
        :raises IllegalArgumentException: Thrown if plugin is null.
        """
        ...

    def get_incoming_channel_registrations(self, channel: str) -> NotNull[Set['PluginMessageListenerRegistration']]:
        """
        Gets a set containing all the incoming plugin channel registrations
        that are on the requested channel.

        :param channel: Channel to retrieve registrations for.
        :return: List of all registrations that are on the channel.
        :raises IllegalArgumentException: Thrown if channel is null.
        """
        ...

    def get_incoming_channel_registrations(self, plugin: Plugin, channel: str) -> NotNull[Set['PluginMessageListenerRegistration']]:
        """
        Gets a set containing all the incoming plugin channel registrations
        that the specified plugin has on the requested channel.

        :param plugin: Plugin to retrieve registrations for.
        :param channel: Channel to filter registrations by.
        :return: List of all registrations that the plugin has.
        :raises IllegalArgumentException: Thrown if plugin or channel is null.
        """
        ...

    def is_registration_valid(self, registration: 'PluginMessageListenerRegistration') -> bool:
        """
        Checks if the specified plugin message listener registration is valid.
        <p>
        A registration is considered valid if it has not be unregistered and
        that the plugin is still enabled.

        :param registration: Registration to check.
        :return: True if the registration is valid, otherwise false.
        """
        ...

    def is_incoming_channel_registered(self, plugin: Plugin, channel: str) -> bool:
        """
        Checks if the specified plugin has registered to receive incoming
        messages through the requested channel.

        :param plugin: Plugin to check registration for.
        :param channel: Channel to test for.
        :return: True if the channel is registered, else false.
        """
        ...

    def is_outgoing_channel_registered(self, plugin: Plugin, channel: str) -> bool:
        """
        Checks if the specified plugin has registered to send outgoing messages
        through the requested channel.

        :param plugin: Plugin to check registration for.
        :param channel: Channel to test for.
        :return: True if the channel is registered, else false.
        """
        ...

    def dispatch_incoming_message(self, source: Player, channel: str, message: bytes) -> None:
        """
        Dispatches the specified incoming message to any registered listeners.

        :param source: Source of the message.
        :param channel: Channel that the message was sent by.
        :param message: Raw payload of the message.
        """
        ...
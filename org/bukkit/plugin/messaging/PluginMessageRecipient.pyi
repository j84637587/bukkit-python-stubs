from typing import Set
from org.bukkit.plugin import Plugin
from org.jetbrains.annotations import NotNull

"""
Represents a possible recipient for a Plugin Message.
"""
class PluginMessageRecipient:
    """
    Sends this recipient a Plugin Message on the specified outgoing
    channel.
    <p>
    The message may not be larger than {@link Messenger#MAX_MESSAGE_SIZE}
    bytes, and the plugin must be registered to send messages on the
    specified channel.

    @param source The plugin that sent this message.
    @param channel The channel to send this message on.
    @param message The raw message to send.
    @raises IllegalArgumentException Thrown if the source plugin is
        disabled.
    @raises IllegalArgumentException Thrown if source, channel or message
        is null.
    @raises MessageTooLargeException Thrown if the message is too big.
    @raises ChannelNotRegisteredException Thrown if the channel is not
        registered for this plugin.
    """
    def send_plugin_message(self, source: NotNull[Plugin], channel: NotNull[str], message: NotNull[bytes]) -> None:
        ...

    """
    Gets a set containing all the Plugin Channels that this client is
    listening on.

    @return Set containing all the channels that this client may accept.
    """
        def get_listening_plugin_channels(self) -> Set[str]:
        ...
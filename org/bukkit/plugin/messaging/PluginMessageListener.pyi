from org.bukkit.entity import Player
from typing import Protocol

class PluginMessageListener(Protocol):
    """
    A listener for a specific Plugin Channel, which will receive notifications
    of messages sent from a client.
    """

    def on_plugin_message_received(self, channel: str, player: Player, message: bytes) -> None:
        """
        A method that will be thrown when a PluginMessageSource sends a plugin
        message on a registered channel.

        :param channel: Channel that the message was sent through.
        :param player: Source of the message.
        :param message: The raw message that was sent.
        """
        ...
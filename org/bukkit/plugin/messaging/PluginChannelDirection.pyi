# org/bukkit/plugin/messaging/PluginChannelDirection.pyi

"""
Represents the different directions a plugin channel may go.
"""

from enum import Enum

class PluginChannelDirection(Enum):
    """
    The plugin channel is being sent to the server from a client.
    """
    INCOMING: PluginChannelDirection

    """
    The plugin channel is being sent to a client from the server.
    """
    OUTGOING: PluginChannelDirection
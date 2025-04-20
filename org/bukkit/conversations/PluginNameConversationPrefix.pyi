from org.bukkit.ChatColor import ChatColor
from org.bukkit.plugin.Plugin import Plugin
from org.bukkit.conversations.ConversationPrefix import ConversationPrefix
from org.bukkit.conversations.ConversationContext import ConversationContext
from typing import Literal

class PluginNameConversationPrefix(ConversationPrefix):
    """
    PluginNameConversationPrefix is a {@link ConversationPrefix} implementation
    that displays the plugin name in front of conversation output.
    """

    def __init__(self, plugin: Plugin) -> None:
        ...

    def __init__(self, plugin: Plugin, separator: str, prefix_color: ChatColor) -> None:
        ...

    /**
     * Prepends each conversation message with the plugin name.
     *
     * @param context Context information about the conversation.
     * @return An empty string.
     */
    def get_prefix(self, context: ConversationContext) -> str:
        ...